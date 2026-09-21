# -*- coding: utf-8 -*-
"""
apply_confirmed_fixes.py — 只应用"已确认"的修复，产出清洗版 CSV + 修改记录

原则:
  1. 只修人工确认过的 79 处单词错字（每条带行号+旧值断言，对不上就报错不硬改）
  2. 删除 19 行 Unit 标题栏垃圾行（程序化识别: 单词名为空且翻译列="UnitN"）
  3. 不碰: 4 个真漏词行、拆行(organ/serve/th/ve)、翻译乱码、常考含义括号 —— 留待人工
  4. 原文件不动，输出到新文件
"""
import csv, re, sys

SRC = r"D:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_重跑.csv"
DST = r"D:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv"
LOG = r"D:\xinyi\codespace\WowStory\清洗记录.txt"

# {CSV文件行号(表头=1): (旧单词, 新单词)}
FIXES = {
    59: ('savlng', 'saving'),
    157: ('wln', 'win'),
    216: ('gbe', 'globe'),
    246: ('economlc', 'economic'),
    248: ('econonmcs', 'economics'),
    271: ('galn', 'gain'),
    291: ('gemus', 'genius'),
    301: ('lgnorance', 'ignorance'),
    303: ('lgnore', 'ignore'),
    309: ('lmage', 'image'),
    310: ('lmaglne', 'imagine'),
    311: ('lmaglnary', 'imaginary'),
    332: ('margm', 'margin'),
    335: ('masslve', 'massive'),
    367: ('sclence', 'science'),
    383: ('ralse', 'raise'),
    394: ('malmum', 'maximum'),
    396: ('meamng', 'meaning'),
    401: ('opemng', 'opening'),
    482: ('unlque', 'unique'),
    484: ('unlverse', 'universe'),
    489: ('valn', 'vain'),
    495: ('varlance', 'variance'),
    515: ('ngzag', 'zigzag'),
    542: ('companson', 'comparison'),
    584: ('specles', 'species'),
    648: ('lmmense', 'immense'),
    649: ('lmmerse', 'immerse'),
    668: ('acqulre', 'acquire'),
    693: ('grlm', 'grim'),
    703: ('lncome', 'income'),
    705: ('lncrease', 'increase'),
    708: ('lncur', 'incur'),
    723: ('slgn', 'sign'),
    789: ('recogmze', 'recognize'),
    795: ('semor', 'senior'),
    807: ('soive', 'solve'),
    854: ('commlsslon', 'commission'),
    861: ('communlsm', 'communism'),
    911: ('lrnpalr', 'impair'),
    920: ('lmpose', 'impose'),
    921: ('lmpress', 'impress'),
    922: ('lmpresslon', 'impression'),
    923: ('lmpresslve', 'impressive'),
    924: ('lmprove', 'improve'),
    929: ('orlgln', 'origin'),
    940: ('plerce', 'pierce'),
    981: ('orgamsm', 'organism'),
    983: ('organlze', 'organize'),
    1043: ('lngenlous', 'ingenious'),
    1128: ('vlew', 'view'),
    1163: ('nmsery', 'misery'),
    1165: ('mlx', 'mix'),
    1166: ('miture', 'mixture'),
    1188: ('preclse', 'precise'),
    1195: ('remova', 'removal'),
    1196: ('remaln', 'remain'),
    1233: ('prlor', 'prior'),
    1235: ('prlvacy', 'privacy'),
    1315: ('rejce', 'rejoice'),
    1438: ('prmary', 'primary'),
    1439: ('prlme', 'prime'),
    1451: ('lnnovation', 'innovation'),
    1460: ('possessn', 'possession'),
    1474: ('compnse', 'comprise'),
    1489: ('eplc', 'epic'),
    1560: ('lnvest', 'invest'),
    1609: ('reqtllre', 'require'),
    1651: ('experlence', 'experience'),
    1659: ('lnsurance', 'insurance'),
    1660: ('lnsure', 'insure'),
    1665: ('curlous', 'curious'),
    1682: ('lssue', 'issue'),
    1696: ('rlse', 'rise'),
    1717: ('susplclon', 'suspicion'),
    1723: ('swlng', 'swing'),
    1736: ('promlslng', 'promising'),
    1774: ('superlor', 'superior'),
    1824: ('fflsls', 'crisis'),
    1852: ('ioss', 'loss'),
}

# 留待人工的未确认嫌疑（不自动改）
PENDING = [
    "行323 'eve' —— 无法确定原词(level? leverage?), 需回PDF",
    "行423 'th' —— 残片, 疑似拆行(thrift之后), 需回PDF",
    "行518 'key' —— 可能是合法词也可能是错识, 需回PDF",
    "行761 've' —— 残片, 疑似拆行, 需回PDF",
    "行763 'click' —— 可能是错识(clinic?), 需回PDF",
    "行1098 'von' —— 无法确定原词(vote? vow?), 需回PDF",
    "行1187 'precus' —— 无法确定原词, 需回PDF",
    "行1655 'exmre' —— 疑似expire, 需回PDF确认",
    "行304 空单词名(ill?) / 行426 空单词名(tip?) / 行817 空单词名(sound?) / 行1706 surname空翻译 —— 4个真漏词, 需回PDF重提",
    "行979/980 organ x2, 行946/948 serve x2 —— 疑似一词拆两行, 需人工合并",
]

def main():
    with open(SRC, encoding='utf-8-sig') as f:
        lines = f.readlines()

    header = lines[0]
    data = lines[1:]  # data[j] 对应文件行号 j+2

    log = []
    errors = []

    # 1) 应用单词修复（带断言）
    fixed = []
    for ln, (old, new) in sorted(FIXES.items()):
        idx = ln - 2
        cols = data[idx].rstrip('\n').split(',')
        if cols[1] != old:
            errors.append(f"行{ln}: 期望'{old}' 实际'{cols[1]}' —— 跳过")
            continue
        cols[1] = new
        data[idx] = ','.join(cols) + '\n'
        fixed.append((ln, old, new))

    # 2) 删除垃圾行（程序化识别）
    kept, junked = [], []
    for j, line in enumerate(data):
        cols = line.rstrip('\n').split(',')
        if not cols[1].strip() and re.fullmatch(r'(?i)\s*unit\s*\d+\s*', cols[2] if len(cols) > 2 else ''):
            junked.append((j + 2, cols[2]))
        else:
            kept.append(line)

    if errors:
        print("断言失败, 未写出任何文件:")
        for e in errors:
            print(" ", e)
        sys.exit(1)

    with open(DST, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(header)
        f.writelines(kept)

    # 3) 修改记录
    log.append("清洗记录 —— 红宝书必考词_全量汇总_重跑.csv -> 清洗版.csv")
    log.append(f"原始词条: {len(data)} -> 清洗后: {len(kept)}")
    log.append("")
    log.append(f"一、单词错字修复 {len(fixed)} 处（行号为原文件行号）")
    for ln, old, new in fixed:
        log.append(f"  行{ln}: {old} -> {new}")
    log.append("")
    log.append(f"二、删除 Unit 标题栏垃圾行 {len(junked)} 行")
    for ln, t in junked:
        log.append(f"  行{ln}: 翻译列='{t}'")
    log.append("")
    log.append("三、未处理, 留待人工确认")
    for p in PENDING:
        log.append(f"  {p}")
    log.append("")
    log.append("四、已知但未动的系统性问题")
    log.append("  - 60 行 「““」 (书里'把……称为'的省略号被OCR吃掉)")
    log.append("  - 46 行 翻译括号不配对; 131 行 常考含义括号截断(高亮只标半个括号)")
    log.append("  - 个别翻译内乱码: 乁/theæ/ad妩/n.Ä 等")

    with open(LOG, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log))

    print(f"修复 {len(fixed)} 处, 删除垃圾行 {len(junked)} 行, {len(data)} -> {len(kept)} 词条")
    print(f"输出: {DST}")
    print(f"记录: {LOG}")

if __name__ == '__main__':
    main()
