import os
import sys
import glob
import re
import csv
import gc
import json
import asyncio
import fitz
from PIL import Image, ImageDraw, ImageFont
import winrt.windows.media.ocr as ocr
import winrt.windows.graphics.imaging as imaging
import winrt.windows.storage.streams as streams

sys.stdout.reconfigure(encoding='utf-8')

DPI = 180
SCALE = DPI / 72.0
MATRIX = fitz.Matrix(SCALE, SCALE)

COL_DIVIDER = 152.16

PDF_DIR = r"D:\xinyi\codespace\WowStory\原始单词本"
OUTPUT_CSV = r"D:\xinyi\codespace\WowStory\红宝书必考词_全量汇总.csv"
PROGRESS_FILE = r"D:\xinyi\codespace\WowStory\.extraction_progress.json"

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
            
    if not rows:
        return []

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
            
        # 2. Right cell translation lines in reading order
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

async def main():
    # PDF files mapping to initial unit number
    pdf_configs = [
        ("必考词1-5.pdf", 1),
        ("必考词6-10.pdf", 6),
        ("必考词11-15.pdf", 11),
        ("必考词16-20.pdf", 16),
        ("必考词U21-26.pdf", 21),
    ]
    
    engine = ocr.OcrEngine.try_create_from_user_profile_languages()
    
    # Check existing progress
    processed_pages = set()
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                processed_pages = set(json.load(f))
        except Exception:
            processed_pages = set()
            
    # Open CSV for appending if exists, else write header
    csv_exists = os.path.exists(OUTPUT_CSV)
    f_csv = open(OUTPUT_CSV, 'a', newline='', encoding='utf-8-sig')
    writer = csv.DictWriter(f_csv, fieldnames=['单元', '单词名', '单词中文翻译', '常考含义'])
    if not csv_exists or os.path.getsize(OUTPUT_CSV) == 0:
        writer.writeheader()
        f_csv.flush()
        
    total_extracted = 0
    print(f"=== 开始全量自动化抽取（共 5 个文件，70 页，26 个单元）===")
    print(f"输出目标: {OUTPUT_CSV}")
    
    for pdf_idx, (pdf_filename, start_unit) in enumerate(pdf_configs, 1):
        pdf_path = os.path.join(PDF_DIR, pdf_filename)
        if not os.path.exists(pdf_path):
            print(f"[警告] 找不到文件: {pdf_path}")
            continue
            
        doc = fitz.open(pdf_path)
        current_unit_num = start_unit - 1
        current_unit_str = f"Unit {start_unit}"
        
        print(f"\n>> [{pdf_idx}/5] 正在处理: {pdf_filename} ({len(doc)} 页)...")
        
        for page_idx in range(len(doc)):
            page_key = f"{pdf_filename}__page_{page_idx}"
            if page_key in processed_pages:
                print(f"  - 第 {page_idx+1:2d}/{len(doc)} 页已在历史记录中，跳过。")
                continue
                
            page = doc[page_idx]
            drawings = page.get_drawings()
            
            # Detect if this page has a green unit header
            greens = [d['rect'] for d in drawings if is_green_header(d)]
            is_start = len(greens) > 0
            if is_start:
                current_unit_num += 1
                current_unit_str = f"Unit {current_unit_num}"
                
            # Check if this is an empty/cover page (e.g. page 14 of 6-10.pdf)
            hlines = get_hlines(drawings)
            if len(hlines) < 2:
                print(f"  - 第 {page_idx+1:2d}/{len(doc)} 页为空白/无表格页，跳过。")
                processed_pages.add(page_key)
                with open(PROGRESS_FILE, 'w', encoding='utf-8') as pf:
                    json.dump(list(processed_pages), pf)
                continue
                
            words = await process_page(engine, page, current_unit_str, is_unit_start=is_start)
            
            if words:
                writer.writerows(words)
                f_csv.flush()
                total_extracted += len(words)
                print(f"  [OK] 第 {page_idx+1:2d}/{len(doc)} 页 ({current_unit_str}) 成功提取 {len(words)} 词 | 累计: {total_extracted} 词")
            else:
                print(f"  - 第 {page_idx+1:2d}/{len(doc)} 页未提取到词。")
                
            # Record progress
            processed_pages.add(page_key)
            with open(PROGRESS_FILE, 'w', encoding='utf-8') as pf:
                json.dump(list(processed_pages), pf)
                
            # Periodic garbage collection
            gc.collect()
            
    f_csv.close()
    print(f"\n==========================================")
    print(f"  全量自动化提取完成！")
    print(f"  总计提取词数: {total_extracted}")
    print(f"  保存路径: {OUTPUT_CSV}")
    print(f"==========================================")

if __name__ == '__main__':
    asyncio.run(main())
