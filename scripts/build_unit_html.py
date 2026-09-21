# -*- coding: utf-8 -*-
"""
从 UnitNN.json 生成对应 UnitNN.html 独立单页应用。
支持指定单单元 (如 python scripts/build_unit_html.py 2) 或生成全量 1~26 单元。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
APP_DIR = os.path.join(PROJ, "单词故事本")
TEMPLATE_PATH = os.path.join(APP_DIR, "Unit01.html")

def build_unit_html(unit_num):
    json_path = os.path.join(APP_DIR, f"Unit{unit_num:02d}.json")
    pt_path = os.path.join(APP_DIR, "pt_data", f"_pt_u{unit_num:02d}.json")
    out_html_path = os.path.join(APP_DIR, f"Unit{unit_num:02d}.html")

    if not os.path.exists(json_path):
        print(f"[错误] 找不到数据文件: {json_path}")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        unit_data = json.load(f)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    stories_cnt = len(unit_data.get("stories", []))
    words_cnt = len(unit_data.get("words", []))

    # 1. 替换 DATA 变量
    # 找到 var DATA = { ... }; 块
    data_js = "var DATA = " + json.dumps(unit_data, ensure_ascii=False, indent=2) + ";"
    pattern = r"var DATA = \{[\s\S]*?\n\};"
    html = re.sub(pattern, data_js, template, count=1)

    # 2. 替换 PT 时间轴变量
    if os.path.exists(pt_path):
        with open(pt_path, "r", encoding="utf-8") as f:
            pt_data = json.load(f)
        pt_js = "var PT = " + json.dumps(pt_data, ensure_ascii=False, indent=2) + ";"
        pt_pattern = r"var PT = \{[\s\S]*?\n\};"
        html = re.sub(pt_pattern, pt_js, html, count=1)

    # 3. 替换标题与 Badge 与 页脚
    html = html.replace("<title>S T O R Y · Unit 1</title>", f"<title>S T O R Y · Unit {unit_num}</title>")
    html = re.sub(r'<span id="badgeText">Unit \d+ · \d+ 篇 · \d+ 词</span>', f'<span id="badgeText">Unit {unit_num} · {stories_cnt} 篇 · {words_cnt} 词</span>', html)
    html = re.sub(r'<div class="foot" id="footText">Unit \d+ 已收录 \d+ / \d+ 词', f'<div class="foot" id="footText">Unit {unit_num} 已收录 {words_cnt} / {words_cnt} 词', html)
    html = html.replace('<span style="font-size:12px;color:var(--clay2);font-weight:600" id="headerUnitTag">Unit 1</span>', f'<span style="font-size:12px;color:var(--clay2);font-weight:600" id="headerUnitTag">Unit {unit_num}</span>')

    with open(out_html_path, "w", encoding="utf-8", newline="") as f:
        f.write(html)

    print(f"[成功] 已生成 Unit{unit_num:02d}.html ({stories_cnt} 故事, {words_cnt} 考点词, {os.path.getsize(out_html_path)} 字节)")
    return True

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "2"
    if target.lower() == "all":
        for u in range(1, 27):
            build_unit_html(u)
    else:
        u_num = int(target)
        build_unit_html(u_num)

if __name__ == "__main__":
    main()
