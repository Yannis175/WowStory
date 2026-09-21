#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
triple_check_units.py — 对 Unit 01 ~ Unit 20 进行反复 3 轮深查

第 1 轮 (Pass 1)：拼写、编码、特殊字符与隐藏字符校验
第 2 轮 (Pass 2)：CSV 全量对齐校验（词数、词名、不可遗漏或多词）
第 3 轮 (Pass 3)：数据结构、故事引用 (s)、标记映射 (base) 与 Markdown 派生一致性
"""

import csv
import json
import os
import re
import sys

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
csv_path = r"d:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv"
dict_path = r"d:\xinyi\codespace\WowStory\_words_alpha.txt"

MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

def load_dict():
    valid = set()
    if os.path.exists(dict_path):
        with open(dict_path, "r", encoding="utf-8") as f:
            for l in f:
                w = l.strip().lower()
                if w:
                    valid.add(w)
    return valid

def load_csv():
    units_csv = {}
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            u_str = (r.get("单元") or "").strip()
            m = re.search(r"\d+", u_str)
            if not m:
                continue
            u_num = int(m.group(0))
            w = (r.get("单词名") or "").strip()
            if u_num not in units_csv:
                units_csv[u_num] = []
            units_csv[u_num].append(w)
    return units_csv

def pass1_spelling_and_encoding(unit_num, D, valid_words):
    issues = []
    words = D.get("words") or []
    stories = D.get("stories") or []

    for w_obj in words:
        w = w_obj.get("w", "")
        # 隐藏不可见字符检查
        for k, v in w_obj.items():
            if isinstance(v, str):
                if "\u200b" in v or "\u200c" in v or "\ufeff" in v:
                    issues.append(f"单词 '{w}' 字段 '{k}' 含有不可见特殊 Unicode 字符")
                if "  " in v and k != "pat":
                    issues.append(f"单词 '{w}' 字段 '{k}' 含有连续多余空格")
        
        # 英文词拼写检查
        w_lower = w.lower()
        if valid_words and not re.search(r"[\s\-]", w_lower) and w_lower not in valid_words:
            issues.append(f"单词 '{w}' 不在标准词典中")

    for st in stories:
        for p in st.get("ps") or []:
            en = p.get("en", "")
            zh = p.get("zh", "")
            if "\u200b" in en or "\ufeff" in en:
                issues.append(f"故事 {st.get('id')} 英文正文含有不可见字符")
            if "\u200b" in zh or "\ufeff" in zh:
                issues.append(f"故事 {st.get('id')} 中文正文含有不可见字符")

    return issues

def pass2_csv_alignment(unit_num, D, csv_words):
    issues = []
    json_words = [w.get("w", "").strip() for w in D.get("words", [])]
    set_csv = set(csv_words)
    set_json = set(json_words)

    if len(json_words) != len(set_json):
        dups = [w for w in set_json if json_words.count(w) > 1]
        issues.append(f"JSON 内部包含重复词条: {dups}")

    missing = sorted(set_csv - set_json)
    extra = sorted(set_json - set_csv)

    if missing:
        issues.append(f"相比 CSV 漏掉 {len(missing)} 词: {missing}")
    if extra:
        issues.append(f"相比 CSV 多出 {len(extra)} 词: {extra}")

    return issues

def pass3_structure_and_linking(unit_num, D):
    issues = []
    stories = D.get("stories") or []
    words = D.get("words") or []
    sids = {st.get("id") for st in stories if st.get("id")}
    json_word_set = {w.get("w", "").strip() for w in words}

    # 1. 所属故事引用
    for w_obj in words:
        w = w_obj.get("w")
        sid = w_obj.get("s")
        if sid not in sids:
            issues.append(f"单词 '{w}' 的 s='{sid}' 指向不存在的故事 ID")

    # 2. 正文标记还原形存在性与全词覆盖
    covered = set()
    for st in stories:
        sid = st.get("id")
        for p in st.get("ps") or []:
            for m in MARKER.finditer(p.get("en") or ""):
                surface = m.group(1).strip()
                base = (m.group(2) or m.group(1)).strip()
                if base not in json_word_set:
                    issues.append(f"故事 {sid} 标记 [[{surface}|{base}]] 的 base 不在 words[] 中")
                else:
                    covered.add(base)

    not_covered = sorted(json_word_set - covered)
    if not_covered:
        issues.append(f"正文未标记覆盖 {len(not_covered)} 词: {not_covered}")

    return issues

def main():
    print("==================================================")
    print("   启动 Unit 01 ~ Unit 20 全量【反复 3 轮深查】机制")
    print("==================================================\n")

    valid_words = load_dict()
    all_csv_data = load_csv()

    total_pass1_errs = 0
    total_pass2_errs = 0
    total_pass3_errs = 0

    for u in range(1, 21):
        json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
        if not os.path.exists(json_path):
            print(f"❌ Unit {u:02d}: JSON 文件缺失")
            continue

        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)

        csv_words = all_csv_data.get(u, [])

        p1_res = pass1_spelling_and_encoding(u, D, valid_words)
        p2_res = pass2_csv_alignment(u, D, csv_words)
        p3_res = pass3_structure_and_linking(u, D)

        n1 = len(p1_res)
        n2 = len(p2_res)
        n3 = len(p3_res)

        total_pass1_errs += n1
        total_pass2_errs += n2
        total_pass3_errs += n3

        status = "完美通过" if (n1 + n2 + n3 == 0) else "有关注项"
        print(f"Unit {u:02d} (共 {len(D.get('words', []))} 词): [{status}]")
        print(f"  - 第1轮(拼写/编码): {n1} 问题 | 第2轮(CSV对齐): {n2} 问题 | 第3轮(标记/引用): {n3} 问题")

        if p1_res:
            for item in p1_res[:3]:
                print(f"    [P1] {item}")
        if p2_res:
            for item in p2_res[:3]:
                print(f"    [P2] {item}")
        if p3_res:
            for item in p3_res[:3]:
                print(f"    [P3] {item}")

    print("\n==================================================")
    print("【3 轮反复深查汇总结果】")
    print(f"  第 1 轮 拼写/编码异常总数 : {total_pass1_errs}")
    print(f"  第 2 轮 CSV 对齐异常总数  : {total_pass2_errs}")
    print(f"  第 3 轮 标记/引用异常总数  : {total_pass3_errs}")
    print("==================================================")

if __name__ == "__main__":
    main()
