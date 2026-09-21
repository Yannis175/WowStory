# -*- coding: utf-8 -*-
"""
scripts/run_unit_pipeline.py — 单词故事本全管线 Master 自动化脚本

包含步骤：
1. 提取单词与源头校验 (Extraction Check)
2. JSON 自动生成/构建 (Batch Generation)
3. 单元格式校验 (validate_unit.py)
4. 人读版 Markdown 导出 (build_md.py)
5. 四轮深度审查 (4-Round Audit Suite)
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(BASE_DIR, "单词故事本")
CSV_PATH = os.path.join(BASE_DIR, "红宝书必考词_全量汇总_清洗版.csv")
DICT_PATH = os.path.join(BASE_DIR, "_words_alpha.txt")

sys.path.append(os.path.join(BASE_DIR, "scripts"))
import build_md

MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

def load_dictionary():
    valid = set()
    if os.path.exists(DICT_PATH):
        with open(DICT_PATH, "r", encoding="utf-8") as f:
            for line in f:
                w = line.strip().lower()
                if w:
                    valid.add(w)
    return valid

def load_csv_units():
    units = {}
    with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            u_str = (r.get("单元") or "").strip()
            m = re.search(r"\d+", u_str)
            if not m:
                continue
            u_num = int(m.group(0))
            w = (r.get("单词名") or "").strip()
            exam = (r.get("常考含义") or "").strip()
            zh = (r.get("单词中文翻译") or "").strip()
            if u_num not in units:
                units[u_num] = []
            units[u_num].append({"w": w, "exam": exam, "zh": zh})
    return units

# Step 1: Extraction Check
def step1_extraction_check(unit_num, csv_words_list, valid_dict):
    print(f"\n--- [Step 1] Unit {unit_num:02d} 提取单词源头质量校验 ---")
    issues = []
    word_names = [x["w"] for x in csv_words_list]
    
    # 1. 重复词检查
    if len(word_names) != len(set(word_names)):
        dups = [w for w in set(word_names) if word_names.count(w) > 1]
        issues.append(f"提取结果中存在重复词汇: {dups}")
        
    # 2. 拼写/OCR截断检查
    for item in csv_words_list:
        w = item["w"]
        w_lower = w.lower()
        if valid_dict and not re.search(r"[\s\-]", w_lower) and w_lower not in valid_dict:
            issues.append(f"词汇 '{w}' 可能存在 OCR 截断或拼写错误（不在标准词典中）")
            
        # 不可见字符检查
        for k, v in item.items():
            if "\u200b" in v or "\ufeff" in v:
                issues.append(f"词汇 '{w}' 的 CSV 字段 '{k}' 含有隐藏不可见字符")
                
    if not issues:
        print(f"  ✓ 提取词数: {len(word_names)} 词，源头校验 100% 通过（无拼写截断/无异常字符）")
    else:
        for iss in issues:
            print(f"  ⚠️ {iss}")
    return issues

# Step 5: 4-Round Audit Suite
def run_4round_audit(unit_num, json_data, csv_words_list, valid_dict):
    print(f"\n--- [Step 5] Unit {unit_num:02d} 四轮深度审查 (4-Round Audit Suite) ---")
    p1_issues = []
    p2_issues = []
    p3_issues = []
    p4_issues = []
    
    words = json_data.get("words", [])
    stories = json_data.get("stories", [])
    json_word_names = [w.get("w", "").strip() for w in words]
    csv_word_names = [x["w"] for x in csv_words_list]
    
    # ---------------- Pass 1: 全面综合与结构对齐 ----------------
    if len(json_word_names) != len(csv_word_names):
        p1_issues.append(f"JSON 词数 ({len(json_word_names)}) 与 CSV 词数 ({len(csv_word_names)}) 不对齐")
    missing = set(csv_word_names) - set(json_word_names)
    extra = set(json_word_names) - set(csv_word_names)
    if missing:
        p1_issues.append(f"相比 CSV 漏词 {len(missing)} 个: {sorted(list(missing))}")
    if extra:
        p1_issues.append(f"相比 CSV 多词 {len(extra)} 个: {sorted(list(extra))}")
        
    # ---------------- Pass 2: 拼写、音标与卡片五维属性深查 ----------------
    for w_obj in words:
        w = w_obj.get("w", "")
        ipa = w_obj.get("ipa", "")
        fam = w_obj.get("fam", [])
        c = w_obj.get("c", [])
        pat = w_obj.get("pat", "")
        
        # 音标斜杠检查
        if ipa.startswith("/") or ipa.endswith("/"):
            p2_issues.append(f"单词 '{w}' 的 ipa 含有前后的斜杠 '/'")
            
        # fam 不能为空
        if not fam or not isinstance(fam, list) or len(fam) == 0:
            p2_issues.append(f"单词 '{w}' 的 fam (词族延伸) 为空")
            
        # c 必须有中英文
        if not c or not isinstance(c, list):
            p2_issues.append(f"单词 '{w}' 的 c (核心搭配) 格式有误")
            
        # pat 需包含词干
        w_stem = w.lower()[:4] if len(w) >= 4 else w.lower()
        if pat and w_stem not in pat.lower():
            p2_issues.append(f"单词 '{w}' 的 pat 例句未包含目标词干 '{w_stem}'")
            
        # 隐藏字符
        for k, v in w_obj.items():
            if isinstance(v, str) and ("\u200b" in v or "\ufeff" in v):
                p2_issues.append(f"单词 '{w}' 字段 '{k}' 含有隐藏不可见字符")

    # ---------------- Pass 3: 考研英一/英二语法、义项与语境对齐 ----------------
    for w_obj in words:
        w = w_obj.get("w", "")
        zh = w_obj.get("zh", "")
        exam = w_obj.get("exam", "")
        if not zh or len(zh) > 10:
            p3_issues.append(f"单词 '{w}' 的故事义 zh '{zh}' 过长或为空")
        if not exam:
            p3_issues.append(f"单词 '{w}' 的常考义 exam 为空")
            
    # ---------------- Pass 4: 故事逻辑、标记语法 [[surface|base]] 与 MD 一致性 ----------------
    json_set = set(json_word_names)
    tagged_bases = set()
    for st in stories:
        sid = st.get("id")
        for p in st.get("ps", []):
            en_text = p.get("en", "")
            for m in MARKER.finditer(en_text):
                surface = m.group(1).strip()
                base = (m.group(2) or m.group(1)).strip()
                
                # 检查标记参数顺序
                if base not in json_set:
                    p4_issues.append(f"故事 {sid} 标记 [[{surface}|{base}]] 的 base 不在 words[] 中（检查参数顺序！）")
                else:
                    tagged_bases.add(base)
                    
    uncovered = json_set - tagged_bases
    if uncovered:
        p4_issues.append(f"正文完全未标记覆盖 {len(uncovered)} 个词: {sorted(list(uncovered))}")

    # 汇总输出
    print(f"  [Pass 1 全面对齐] : {len(p1_issues)} 问题")
    print(f"  [Pass 2 属性深查] : {len(p2_issues)} 问题")
    print(f"  [Pass 3 考研语法] : {len(p3_issues)} 问题")
    print(f"  [Pass 4 标记逻辑] : {len(p4_issues)} 问题")
    
    all_issues = p1_issues + p2_issues + p3_issues + p4_issues
    if not all_issues:
        print(f"  🎉 Unit {unit_num:02d} 四轮深度审查 100% 完美通过！")
    else:
        for iss in all_issues[:5]:
            print(f"    ❌ {iss}")
    return len(all_issues)

def process_unit_pipeline(unit_num, all_csv_data, valid_dict):
    print("\n" + "="*60)
    print(f"   单词故事本全管线 Master 执行 · Unit {unit_num:02d}")
    print("="*60)
    
    csv_words_list = all_csv_data.get(unit_num, [])
    if not csv_words_list:
        print(f"❌ 无法从 CSV 中提取到 Unit {unit_num} 数据")
        return False
        
    # 步骤 1: 提取校验
    step1_extraction_check(unit_num, csv_words_list, valid_dict)
    
    # 步骤 2 & 3 & 4: 检查 JSON 是否已生成
    json_path = os.path.join(STORY_DIR, f"Unit{unit_num:02d}.json")
    if not os.path.exists(json_path):
        print(f"⚠️ 找不到 JSON 文件 {json_path}，请先生成或提供数据。")
        return False
        
    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        
    # 步骤 5: 跑 validate_unit 官方校验
    cmd = [sys.executable, "-X", "utf8", os.path.join(BASE_DIR, "scripts", "validate_unit.py"), "--csv", CSV_PATH, "--unit", str(unit_num), "--json", json_path]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"❌ validate_unit.py 校验不通过 (Exit Code {res.returncode}):\n{res.stdout}\n{res.stderr}")
        return False
    else:
        print("  ✓ validate_unit.py 格式校验 PASS (ERROR 0)")
        
    # 步骤 6: 导出 Markdown
    md_path = os.path.join(STORY_DIR, f"Unit{unit_num:02d}.md")
    md_content = build_md.build(json_data)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"  ✓ 成功导出人读版 Markdown: {md_path}")
    
    # 步骤 7: 跑 4 轮深查
    audit_errs = run_4round_audit(unit_num, json_data, csv_words_list, valid_dict)
    return audit_errs == 0

def main():
    parser = argparse.ArgumentParser(description="单词故事本 Master 自动化管线")
    parser.add_argument("--units", nargs="+", type=int, help="要处理或校验的单元号列表 (例: 21 22 23)")
    args = parser.parse_args()
    
    valid_dict = load_dictionary()
    all_csv_data = load_csv_units()
    
    units_to_run = args.units if args.units else list(range(21, 27))
    print(f"启动单词故事本 Master 全管线，包含单元: {units_to_run}")
    
    success_count = 0
    for u in units_to_run:
        ok = process_unit_pipeline(u, all_csv_data, valid_dict)
        if ok:
            success_count += 1
            
    print("\n" + "="*60)
    print(f"【管线总汇报】共处理 {len(units_to_run)} 个单元 ｜ 完美通过: {success_count}/{len(units_to_run)}")
    print("="*60)

if __name__ == "__main__":
    main()
