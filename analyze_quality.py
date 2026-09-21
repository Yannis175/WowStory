# -*- coding: utf-8 -*-
# 质量分析脚本：只读分析 CSV，不修改任何数据
import csv, re, collections

path = r"D:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_重跑.csv"
with open(path, encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

R = []
A = R.append
A(f"总词条数: {len(rows)}")
A("")

# ---------- 1. 完整性 ----------
A("=" * 50)
A("1. 完整性（空字段）")
A("=" * 50)
empty_word = [(i+2, r) for i, r in enumerate(rows) if not r['单词名'].strip()]
empty_trans = [(i+2, r) for i, r in enumerate(rows) if not r['单词中文翻译'].strip()]
empty_hl = [(i+2, r) for i, r in enumerate(rows) if not r['常考含义'].strip()]
A(f"空单词名: {len(empty_word)} 行")
for ln, r in empty_word:
    A(f"  行{ln} [{r['单元']}] 翻译: {r['单词中文翻译'][:45]}")
A(f"空翻译: {len(empty_trans)} 行")
for ln, r in empty_trans[:10]:
    A(f"  行{ln} [{r['单元']}] {r['单词名']}")
A(f"空常考含义: {len(empty_hl)} 行")
for ln, r in empty_hl:
    A(f"  行{ln} [{r['单元']}] {r['单词名']}")
A("")

# ---------- 2. 单词名质量 ----------
A("=" * 50)
A("2. 单词名字段")
A("=" * 50)
bad_chars = [(i+2, r['单元'], r['单词名']) for i, r in enumerate(rows)
             if r['单词名'] and not re.fullmatch(r'[a-z][a-z\-]*', r['单词名'])]
short = [(i+2, r['单元'], r['单词名']) for i, r in enumerate(rows)
         if r['单词名'] and len(r['单词名']) <= 2]
long_ = [(i+2, r['单元'], r['单词名']) for i, r in enumerate(rows)
         if len(r['单词名']) >= 16]
A(f"含非法字符(非纯小写字母/连字符): {len(bad_chars)}")
for x in bad_chars[:15]: A(f"  行{x[0]} [{x[1]}] '{x[2]}'")
A(f"过短(<=2字符): {len(short)}")
for x in short: A(f"  行{x[0]} [{x[1]}] '{x[2]}'")
A(f"过长(>=16字符, 疑似两词粘连): {len(long_)}")
for x in long_: A(f"  行{x[0]} [{x[1]}] '{x[2]}'")

words = [r['单词名'] for r in rows if r['单词名']]
dup = {w: c for w, c in collections.Counter(words).items() if c > 1}
A(f"重复单词: {len(dup)} 个")
for w, c in sorted(dup.items()):
    locs = [(i+2, rows[i]['单元']) for i in range(len(rows)) if rows[i]['单词名'] == w]
    same_unit = len(set(u for _, u in locs)) < len(locs)
    A(f"  '{w}' x{c} -> {locs}" + ("  <-- 同单元内重复, 疑似拆行" if same_unit else ""))
A("")

# ---------- 3. 单元内字母序 ----------
A("=" * 50)
A("3. 单元内字母序逆序（疑似拆行/串行）")
A("=" * 50)
inv = []
for i in range(len(rows) - 1):
    a, b = rows[i], rows[i+1]
    if a['单元'] == b['单元'] and a['单词名'] and b['单词名']:
        if b['单词名'] < a['单词名']:
            inv.append((i+2, a['单元'], a['单词名'], b['单词名']))
A(f"逆序对: {len(inv)}")
for x in inv: A(f"  行{x[0]} [{x[1]}] '{x[2]}' -> '{x[3]}'")
A("")

# ---------- 4. 翻译乱码 ----------
A("=" * 50)
A("4. 翻译乱码")
A("=" * 50)
all_trans = ''.join(r['单词中文翻译'] for r in rows)
freq = collections.Counter(all_trans)
rare_cjk = {c for c, n in freq.items() if 0x4E00 <= ord(c) <= 0x9FFF and n <= 2}
A(f"全库出现<=2次的汉字共 {len(rare_cjk)} 个: {''.join(sorted(rare_cjk))}")
rare_rows = []
for i, r in enumerate(rows):
    hit = sorted({c for c in r['单词中文翻译'] if c in rare_cjk})
    if hit:
        rare_rows.append((i+2, r['单元'], r['单词名'], ''.join(hit)))
A(f"含低频怪字的行: {len(rare_rows)}")
for x in rare_rows[:25]: A(f"  行{x[0]} [{x[1]}] {x[2]}: 怪字[{x[3]}]")
A("")

quotes = [(i+2, r['单元'], r['单词名']) for i, r in enumerate(rows)
          if '““' in r['单词中文翻译'] or '””' in r['单词中文翻译']]
A(f"含连续双引号(““/””, 即「把……称为」被OCR吃掉省略号): {len(quotes)}")
for x in quotes[:15]: A(f"  行{x[0]} [{x[1]}] {x[2]}")
A("")

unbal = [(i+2, r['单元'], r['单词名']) for i, r in enumerate(rows)
         if r['单词中文翻译'].count('（') != r['单词中文翻译'].count('）')
         or r['单词中文翻译'].count('(') != r['单词中文翻译'].count(')')]
A(f"翻译括号不配对: {len(unbal)}")
for x in unbal[:15]: A(f"  行{x[0]} [{x[1]}] {x[2]}")

hl_unbal = [(i+2, r['单元'], r['单词名'], r['常考含义']) for i, r in enumerate(rows)
            if r['常考含义'].count('（') != r['常考含义'].count('）')
            or r['常考含义'].count('(') != r['常考含义'].count(')')]
A(f"常考含义括号不配对: {len(hl_unbal)}")
for x in hl_unbal[:15]: A(f"  行{x[0]} [{x[1]}] {x[2]}: {x[3][:40]}")
A("")

# ---------- 5. 翻译中的英文残留 ----------
A("=" * 50)
A("5. 翻译中的英文残留（除词性标记外）")
A("=" * 50)
POS = set('n v vt vi adj adv prep conj pron num art int aux abbr pl sing usu esp etc sb sth as to of in on at by for with or from uk us eg ie mf'.split())
latin_rows = []
latin_freq = collections.Counter()
for i, r in enumerate(rows):
    toks = re.findall(r'[a-zA-Z]{2,}', r['单词中文翻译'])
    bad = [t for t in toks if t.lower().rstrip('.') not in POS]
    if bad:
        latin_rows.append((i+2, r['单元'], r['单词名'], bad[:5], r['单词中文翻译'][:50]))
        for t in bad: latin_freq[t] += 1
A(f"含可疑英文残留的行: {len(latin_rows)}")
for x in latin_rows[:20]: A(f"  行{x[0]} [{x[1]}] {x[2]}: {x[3]} | {x[4]}")
A("")

# ---------- 6. 常考含义 vs 翻译一致性 ----------
A("=" * 50)
A("6. 常考含义与翻译的一致性")
A("=" * 50)
def norm(s):
    return re.sub(r'[\s，。；：、（）()·“”‘’\.\[\]〖〗\-]', '', s)

mismatch = []
for i, r in enumerate(rows):
    hl = r['常考含义'].strip()
    if not hl:
        continue
    t = norm(r['单词中文翻译'])
    bad_segs = [seg for seg in hl.split('；') if seg and norm(seg) not in t]
    if bad_segs:
        mismatch.append((i+2, r['单元'], r['单词名'], bad_segs[:3], r['单词中文翻译'][:45]))
A(f"高亮段在翻译中找不到原文的行: {len(mismatch)}")
for x in mismatch[:25]: A(f"  行{x[0]} [{x[1]}] {x[2]}: 高亮{x[3]} | 翻译: {x[4]}")
A("")

# ---------- 7. 翻译过短 ----------
A("=" * 50)
A("7. 翻译过短(<=5字符, 疑似截断)")
A("=" * 50)
short_t = [(i+2, r['单元'], r['单词名'], r['单词中文翻译']) for i, r in enumerate(rows)
           if r['单词中文翻译'] and len(r['单词中文翻译']) <= 5]
A(f"共 {len(short_t)} 行")
for x in short_t: A(f"  行{x[0]} [{x[1]}] {x[2]}: '{x[3]}'")

with open(r"D:\xinyi\codespace\WowStory\.workbuddy\quality_report.txt", 'w', encoding='utf-8') as f:
    f.write('\n'.join(R))
print("REPORT WRITTEN, lines:", len(R))
