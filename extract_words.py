import sys, os, re, asyncio, fitz
from PIL import Image, ImageDraw, ImageFont
import winrt.windows.media.ocr as ocr
import winrt.windows.graphics.imaging as imaging
import winrt.windows.storage.streams as streams

sys.stdout.reconfigure(encoding='utf-8')

DPI = 180
SCALE = DPI / 72.0
MATRIX = fitz.Matrix(SCALE, SCALE)

COL_DIVIDER = 152.16

def is_green_header(d):
    f = d.get('fill')
    if not f: return False
    return abs(f[0] - 0.89) < 0.05 and abs(f[1] - 0.94) < 0.05 and d['rect'].width > 300

def is_orange_highlight(d):
    f = d.get('fill')
    if not f: return False
    return abs(f[0] - 0.984) < 0.03 and abs(f[1] - 0.898) < 0.03 and abs(f[2] - 0.835) < 0.03

def get_hlines(drawings):
    y_lines = set()
    for d in drawings:
        r = d['rect']
        if r.height < 3 and r.width > 200:
            y_lines.add(round(r.y0, 1))
    return sorted(list(y_lines))

async def ocr_image(engine, pix):
    png_bytes = pix.tobytes('png')
    stream = streams.InMemoryRandomAccessStream()
    writer = streams.DataWriter(stream)
    writer.write_bytes(png_bytes)
    await writer.store_async()
    stream.seek(0)
    decoder = await imaging.BitmapDecoder.create_async(stream)
    bitmap = await decoder.get_software_bitmap_async()
    res = await engine.recognize_async(bitmap)
    return res

async def fallback_word_ocr(engine, page, y0, y1):
    pix = page.get_pixmap(matrix=MATRIX, clip=fitz.Rect(65, y0 + 1, COL_DIVIDER - 2, y1 - 1))
    import io
    img = Image.open(io.BytesIO(pix.tobytes('png')))
    canvas = Image.new('RGB', (img.width + 120, max(img.height, 50)), (255, 255, 255))
    try:
        font = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', 22)
    except:
        font = None
    draw = ImageDraw.Draw(canvas)
    draw.text((10, 12), '词语', font=font, fill=(0, 0, 0))
    canvas.paste(img, (75, 0))
    
    buf = io.BytesIO()
    canvas.save(buf, format='PNG')
    stream = streams.InMemoryRandomAccessStream()
    writer = streams.DataWriter(stream)
    writer.write_bytes(buf.getvalue())
    await writer.store_async()
    stream.seek(0)
    decoder = await imaging.BitmapDecoder.create_async(stream)
    bitmap = await decoder.get_software_bitmap_async()
    res = await engine.recognize_async(bitmap)
    words = []
    for l in res.lines:
        t = l.text.replace('词语', '').replace('词', '').strip()
        if t: words.append(t)
    return ''.join(words)

async def process_page(engine, page, unit_name, is_unit_start=False):
    drawings = page.get_drawings()
    highlights = [d['rect'] for d in drawings if is_orange_highlight(d)]
    hlines = get_hlines(drawings)
    if len(hlines) < 2:
        return []
        
    start_idx = 1 if is_unit_start else 0
    rows = []
    for i in range(start_idx, len(hlines) - 1):
        y0, y1 = hlines[i], hlines[i+1]
        if 15 <= (y1 - y0) <= 150:
            rows.append((y0, y1))
            
    pix = page.get_pixmap(matrix=MATRIX)
    page_res = await ocr_image(engine, pix)
    
    ocr_lines = []
    for line in page_res.lines:
        words = list(line.words)
        if not words: continue
        y_coords = [w.bounding_rect.y / SCALE for w in words]
        x_coords = [w.bounding_rect.x / SCALE for w in words]
        avg_y = sum(y_coords) / len(y_coords)
        min_x = min(x_coords)
        ocr_lines.append({
            'avg_y': avg_y,
            'min_x': min_x,
            'words': words
        })
        
    results = []
    for idx, (y0, y1) in enumerate(rows):
        # 1. Left cell word tokens
        word_parts = []
        for line in ocr_lines:
            if y0 - 3 <= line['avg_y'] <= y1 + 3:
                for w in line['words']:
                    pdf_x = w.bounding_rect.x / SCALE
                    if pdf_x < COL_DIVIDER:
                        word_parts.append(w.text)
                        
        word_str = ''.join(word_parts).replace(' ', '').lower()
        word_str = re.sub(r'[^a-zA-Z\-]', '', word_str)
        
        # Fallback if empty
        if not word_str:
            fallback = await fallback_word_ocr(engine, page, y0, y1)
            word_str = re.sub(r'[^a-zA-Z\-]', '', fallback.replace(' ', '').lower())
            
        # 2. Right cell translation lines in reading order (line clustering by y, then sort by x)
        row_lines = []
        for line in ocr_lines:
            if y0 - 3 <= line['avg_y'] <= y1 + 3:
                right_words = [w for w in line['words'] if (w.bounding_rect.x / SCALE) >= COL_DIVIDER]
                if right_words:
                    w_ys = [w.bounding_rect.y / SCALE for w in right_words]
                    w_xs = [w.bounding_rect.x / SCALE for w in right_words]
                    row_lines.append({
                        'avg_y': sum(w_ys) / len(w_ys),
                        'min_x': min(w_xs),
                        'words': right_words
                    })
                    
        # Group lines that have roughly the same line height (within 8pt)
        # Sort lines: primary key is line bucket (round(avg_y / 10)), secondary key is min_x
        row_lines.sort(key=lambda l: (round((l['avg_y'] - y0) / 10), l['min_x']))
        
        trans_line_strings = []
        trans_words_with_rects = []
        for rl in row_lines:
            text = ''.join([w.text for w in rl['words']])
            if text:
                trans_line_strings.append(text)
            for w in rl['words']:
                wr = w.bounding_rect
                pdf_rect = fitz.Rect(
                    wr.x / SCALE,
                    wr.y / SCALE,
                    (wr.x + wr.width) / SCALE,
                    (wr.y + wr.height) / SCALE
                )
                trans_words_with_rects.append((w.text, pdf_rect))
                
        full_trans = ' '.join(trans_line_strings)
        
        # 3. Highlights in this row
        row_hl = sorted([h for h in highlights if h.y0 >= y0 - 3 and h.y1 <= y1 + 3], key=lambda r: (round((r.y0 - y0) / 10), r.x0))
        
        phrases = []
        for h in row_hl:
            matched = []
            for text, r in trans_words_with_rects:
                inter = r & h
                if not inter.is_empty and (inter.get_area() / r.get_area() > 0.25):
                    matched.append((r.x0, text))
            if matched:
                matched.sort(key=lambda x: x[0])
                phrase = ''.join([c[1] for c in matched]).strip('，；、。 ：:,.()（）')
                if phrase and phrase not in phrases:
                    phrases.append(phrase)
                    
        if row_hl and not phrases:
            for h in row_hl:
                h_exp = fitz.Rect(h.x0 - 2, h.y0 - 2, h.x1 + 2, h.y1 + 2)
                matched = []
                for text, r in trans_words_with_rects:
                    inter = r & h_exp
                    if not inter.is_empty and (inter.get_area() / r.get_area() > 0.15):
                        matched.append((r.x0, text))
                if matched:
                    matched.sort(key=lambda x: x[0])
                    phrase = ''.join([c[1] for c in matched]).strip('，；、。 ：:,.()（）')
                    if phrase and phrase not in phrases:
                        phrases.append(phrase)
                        
        hl_str = '；'.join(phrases)
        results.append({
            '单元': unit_name,
            '单词名': word_str,
            '单词中文翻译': full_trans,
            '常考含义': hl_str
        })
        
    return results

async def test():
    doc = fitz.open(r"D:\xinyi\codespace\WowStory\原始单词本\必考词1-5.pdf")
    engine = ocr.OcrEngine.try_create_from_user_profile_languages()
    
    p1 = await process_page(engine, doc[0], 'Unit 1', is_unit_start=True)
    p2 = await process_page(engine, doc[1], 'Unit 1', is_unit_start=False)
    all_words = p1 + p2
    print(f'Total words: {len(all_words)}')
    
    import csv
    out = r"D:\xinyi\codespace\WowStory\unit1_sample.csv"
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['单元', '单词名', '单词中文翻译', '常考含义'])
        w.writeheader()
        w.writerows(all_words)
    print("Done writing", out)

asyncio.run(test())
