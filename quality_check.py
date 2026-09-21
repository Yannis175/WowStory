# -*- coding: utf-8 -*-
"""
quality_check.py — OCR 词表/表格 CSV 质量检查（只读，不修改数据）

用法:
    python quality_check.py <csv路径> [--out 报告路径] [--word-col 单词名] [--trans-col 单词中文翻译] [--hl-col 常考含义] [--group-col 单元]

检查维度:
    1. 完整性      —— 空字段统计 + Unit 标题栏垃圾行检测
    2. 单词名字段  —— 非法字符 / 过短 / 过长 / 重复
    3. 单词错字候选 —— 启发式规则（i->l、m->rn 等 OCR 系统性误识），输出"候选"需人工或词典确认
    4. 组内逆序    —— 注意: 仅当数据应按字母序排列时才是缺陷信号; 对按词族排列的词表, 其价值是暴露错词
    5. 翻译乱码    —— 连续引号 / 括号不配对 / 低频怪字 / 可疑英文残留
    6. 高亮一致性  —— 常考含义每段是否为翻译的子串（衡量提取管线可靠性）

已知误报（脚本会自动豁免）:
    - 合法含 'ln' 的词: illness, vulnerable 等（跨音节 l+n）
    - 合法含 'ffs' 的词: offset, offspring
"""
import argparse, csv, re, collections, sys

# 合法豁免表（启发式规则的已知误报）
WHITELIST = {'illness', 'vulnerable', 'offset', 'offspring', 'illnesses'}


def check(csv_path, out_path, wc, tc, hc, gc):
    with open(csv_path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))

    R = []
    A = R.append
    A(f"文件: {csv_path}")
    A(f"总词条数: {len(rows)}")
    A("")

    # ---------- 1. 完整性 ----------
    A("=" * 50)
    A("1. 完整性（空字段 / 垃圾行）")
    A("=" * 50)
    junk = [(i + 2, r) for i, r in enumerate(rows)
            if not r[wc].strip() and re.fullmatch(r'(?i)\s*unit\s*\d+\s*', r[tc] or '')]
    empty_word = [(i + 2, r) for i, r in enumerate(rows)
                  if not r[wc].strip() and not re.fullmatch(r'(?i)\s*unit\s*\d+\s*', r[tc] or '')]
    empty_trans = [(i + 2, r) for i, r in enumerate(rows) if not r[tc].strip()]
    empty_hl = [(i + 2, r) for i, r in enumerate(rows) if hc and not r[hc].strip()]
    A(f"垃圾行（标题栏被当成词条, 应删除）: {len(junk)}")
    for ln, r in junk:
        A(f"  行{ln} [{r[gc]}] 翻译列='{r[tc]}'")
    A(f"真空单词名（标题垃圾行除外）: {len(empty_word)}")
    for ln, r in empty_word:
        A(f"  行{ln} [{r[gc]}] 翻译: {r[tc][:45]}")
    A(f"空翻译: {len(empty_trans)}")
    for ln, r in empty_trans:
        A(f"  行{ln} [{r[gc]}] {r[wc]}")
    if hc:
        real_empty_hl = [(ln, r) for ln, r in empty_hl if r[wc].strip()]
        A(f"空常考含义: {len(empty_hl)} (其中含垃圾行 {len(empty_hl) - len(real_empty_hl)} 行)")
        for ln, r in real_empty_hl:
            A(f"  行{ln} [{r[gc]}] {r[wc]}")
    A("")

    # ---------- 2. 单词名字段 ----------
    A("=" * 50)
    A("2. 单词名字段")
    A("=" * 50)
    bad_chars = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows)
                 if r[wc] and not re.fullmatch(r'[a-z][a-z\-]*', r[wc])]
    short = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows)
             if r[wc] and len(r[wc]) <= 2]
    long_ = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows) if len(r[wc]) >= 16]
    A(f"含非法字符: {len(bad_chars)}")
    for x in bad_chars[:15]:
        A(f"  行{x[0]} [{x[1]}] '{x[2]}'")
    A(f"过短(<=2字符, 疑似残片): {len(short)}")
    for x in short:
        A(f"  行{x[0]} [{x[1]}] '{x[2]}'")
    A(f"过长(>=16字符, 疑似粘连): {len(long_)}")
    for x in long_:
        A(f"  行{x[0]} [{x[1]}] '{x[2]}'")
    words = [r[wc] for r in rows if r[wc]]
    dup = {w: c for w, c in collections.Counter(words).items() if c > 1}
    A(f"重复单词: {len(dup)}")
    for w, c in sorted(dup.items()):
        locs = [(i + 2, rows[i][gc]) for i in range(len(rows)) if rows[i][wc] == w]
        same = len(set(u for _, u in locs)) < len(locs)
        A(f"  '{w}' x{c} -> {locs}" + ("  <-- 同组内重复, 疑似拆行" if same else ""))
    A("")

    # ---------- 3. 单词错字候选（启发式，下界） ----------
    A("=" * 50)
    A("3. 单词错字候选（启发式; 需人工/词典确认）")
    A("=" * 50)
    suspects = []
    for i, r in enumerate(rows):
        w = r[wc]
        if not w or w in WHITELIST:
            continue
        reasons = []
        if re.match(r'^l[b-df-hj-np-tvwxz]', w):
            reasons.append('l+辅音开头(疑似i->l)')
        if 'ln' in w:
            reasons.append('含ln(疑似i->l; 注意illness/vulnerable类合法词)')
        if 'mng' in w:
            reasons.append('含mng(疑似i->l)')
        if re.search(r'[bcdfghjklmnpqrstvwxz]rn[bcdfghjklmnpqrstvwxz]', w):
            reasons.append('辅音+rn+辅音(疑似m->rn)')
        if re.search(r'q[^u]', w):
            reasons.append('q后非u')
        if w.startswith('tl'):
            reasons.append('tl开头')
        if 'sls' in w or 'ffs' in w:
            reasons.append('含sls/ffs(注意offset/offspring类合法词)')
        if w.endswith('sn') and len(w) > 5:
            reasons.append('词尾sn(疑似-sion漏i)')
        if reasons:
            suspects.append((i + 2, r[gc], w, ';'.join(reasons)))
    A(f"候选数: {len(suspects)} (仅为下界; 词中间的 i->l 如 varlance 抓不到, 全量需词典比对)")
    for ln, u, w, why in suspects:
        A(f"  行{ln} [{u}] '{w}' -- {why}")
    A("")

    # ---------- 4. 组内逆序 ----------
    A("=" * 50)
    A("4. 组内逆序（按词族排列的词表中不是缺陷, 主要用于肉眼暴露错词）")
    A("=" * 50)
    inv = []
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        if a[gc] == b[gc] and a[wc] and b[wc] and b[wc] < a[wc]:
            inv.append((i + 2, a[gc], a[wc], b[wc]))
    A(f"逆序对: {len(inv)}（逐条列于完整报告, 此处略）" if len(inv) > 40 else f"逆序对: {len(inv)}")
    if len(inv) <= 40:
        for x in inv:
            A(f"  行{x[0]} [{x[1]}] '{x[2]}' -> '{x[3]}'")
    A("")

    # ---------- 5. 翻译乱码 ----------
    A("=" * 50)
    A("5. 翻译乱码")
    A("=" * 50)
    quotes = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows)
              if '““' in r[tc] or '””' in r[tc]]
    A(f"连续双引号(““/””, 省略号被OCR吃掉): {len(quotes)}")
    for x in quotes[:20]:
        A(f"  行{x[0]} [{x[1]}] {x[2]}")
    unbal = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows)
             if r[tc].count('（') != r[tc].count('）') or r[tc].count('(') != r[tc].count(')')]
    A(f"翻译括号不配对: {len(unbal)}")
    for x in unbal[:20]:
        A(f"  行{x[0]} [{x[1]}] {x[2]}")
    all_trans = ''.join(r[tc] for r in rows)
    freq = collections.Counter(all_trans)
    rare_cjk = {c for c, n in freq.items() if 0x4E00 <= ord(c) <= 0x9FFF and n == 1}
    rare_rows = []
    for i, r in enumerate(rows):
        hit = sorted({c for c in r[tc] if c in rare_cjk})
        if hit:
            rare_rows.append((i + 2, r[gc], r[wc], ''.join(hit)))
    A(f"含仅出现1次的汉字的行: {len(rare_rows)}（多为合法生僻字, 供抽查; 真乱码如 乁/讠 也在这里面）")
    for x in rare_rows[:20]:
        A(f"  行{x[0]} [{x[1]}] {x[2]}: [{x[3]}]")
    POS = set('n v vt vi adj adv prep conj pron num art int aux abbr pl sing usu esp etc sb sth '
              'as to of in on at by for with or from uk us eg ie mf'.split())
    latin_rows = []
    for i, r in enumerate(rows):
        toks = re.findall(r'[a-zA-Z]{2,}', r[tc])
        bad = [t for t in toks if t.lower().rstrip('.') not in POS]
        if bad:
            latin_rows.append((i + 2, r[gc], r[wc], bad[:5]))
    A(f"可疑英文残留（除词性/惯用标记外; 含动词变形等合法情况, 需人工甄别）: {len(latin_rows)}")
    for x in latin_rows[:20]:
        A(f"  行{x[0]} [{x[1]}] {x[2]}: {x[3]}")
    A("")

    # ---------- 6. 高亮一致性 ----------
    if hc:
        A("=" * 50)
        A("6. 常考含义与翻译的一致性（衡量提取管线可靠性）")
        A("=" * 50)
        def norm(s):
            return re.sub(r'[\s，。；：、（）()·“”‘’\.\[\]〖〗\-]', '', s)
        mismatch = []
        for i, r in enumerate(rows):
            hl = r[hc].strip()
            if not hl:
                continue
            t = norm(r[tc])
            bad_segs = [seg for seg in hl.split('；') if seg and norm(seg) not in t]
            if bad_segs:
                mismatch.append((i + 2, r[gc], r[wc], bad_segs[:3]))
        A(f"高亮段在翻译中找不到原文的行: {len(mismatch)}")
        for x in mismatch[:25]:
            A(f"  行{x[0]} [{x[1]}] {x[2]}: {x[3]}")
        hl_unbal = [(i + 2, r[gc], r[wc]) for i, r in enumerate(rows)
                    if r[hc].count('（') != r[hc].count('）') or r[hc].count('(') != r[hc].count(')')]
        A(f"常考含义括号不配对: {len(hl_unbal)}（高亮只标半个括号的系统性artifact, 非OCR错误）")
        A("")

    report = '\n'.join(R)
    if out_path:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"报告已写入: {out_path}")
    else:
        sys.stdout.reconfigure(encoding='utf-8')
        print(report)


def main():
    ap = argparse.ArgumentParser(description='OCR 词表/表格 CSV 质量检查（只读）')
    ap.add_argument('csv', help='待检查的 CSV 路径')
    ap.add_argument('--out', default=None, help='报告输出路径（缺省打印到 stdout）')
    ap.add_argument('--word-col', default='单词名')
    ap.add_argument('--trans-col', default='单词中文翻译')
    ap.add_argument('--hl-col', default='常考含义')
    ap.add_argument('--group-col', default='单元')
    args = ap.parse_args()
    check(args.csv, args.out, args.word_col, args.trans_col, args.hl_col, args.group_col)


if __name__ == '__main__':
    main()
