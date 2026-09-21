#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audit_quality_u01_u20.py — 针对 Unit 01 到 Unit 20 数据真源的全量质量扫描

检查维度：
1. 词形词典比对 (words_alpha 比对)
2. 音标 IPA 格式规范 (无斜杠、无乱码)
3. exam 常考义漂移分级 (对照 CSV 检查义项缺失或新增无关义)
4. pat 例句包含目标词/词干
5. c 核心搭配英文拼写与一致性
6. syn / fam / dif 完整性与有效性
"""

import argparse
import csv
import json
import glob
import os
import re
import sys

SENSE_SEP = re.compile(r"[；;，,、/]")
MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

def senses(s):
    return [x.strip() for x in SENSE_SEP.split(s or "") if x.strip()]

def load_dict(dict_path):
    valid_words = set()
    if os.path.exists(dict_path):
        with open(dict_path, "r", encoding="utf-8") as f:
            for line in f:
                w = line.strip().lower()
                if w:
                    valid_words.add(w)
    return valid_words

def load_csv_units(csv_path):
    data = {}
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            u_str = (r.get("单元") or "").strip()
            m = re.search(r"\d+", u_str)
            if not m:
                continue
            u_num = int(m.group(0))
            w = (r.get("单词名") or "").strip()
            exam = (r.get("常考含义") or "").strip()
            trans = (r.get("单词中文翻译") or "").strip()
            if u_num not in data:
                data[u_num] = {}
            data[u_num][w] = {"exam": exam, "trans": trans}
    return data

def audit_unit(unit_num, json_path, csv_unit_data, valid_dict):
    issues = {
        "dict_typos": [],       # 1. 词名词典比对可疑项
        "ipa_issues": [],       # 2. 音标格式异常
        "exam_drift_high": [],  # 3. 高风险常考义漂移
        "exam_drift_norm": [],  # 3. 正常加工常考义
        "pat_missing_word": [], # 4. 例句中找不到目标词
        "collocation_err": [],  # 5. 搭配拼写/格式可疑
        "card_structure_err": []# 6. 卡片结构问题
    }

    if not os.path.exists(json_path):
        return None

    try:
        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)
    except Exception as e:
        return {"error": f"JSON 读取失败: {e}"}

    words = D.get("words") or []
    stories = D.get("stories") or []

    # 建立 story_ids
    story_ids = {s.get("id") for s in stories if s.get("id")}

    for i, x in enumerate(words):
        w = (x.get("w") or "").strip()
        ipa = (x.get("ipa") or "").strip()
        pos = (x.get("pos") or "").strip()
        s_id = (x.get("s") or "").strip()
        zh = (x.get("zh") or "").strip()
        exam = (x.get("exam") or "").strip()
        c = x.get("c") or []
        syn = x.get("syn") or []
        fam = x.get("fam") or []
        dif = (x.get("dif") or "").strip()
        pat = (x.get("pat") or "").strip()
        patZh = (x.get("patZh") or "").strip()

        # 1. 词名词典校验
        w_lower = w.lower()
        # 排除连字符词、多词短语
        if valid_dict and not re.search(r"[\s\-]", w_lower):
            if w_lower not in valid_dict:
                issues["dict_typos"].append((w, "词形不在标准词典中"))

        # 2. 音标 IPA 格式
        if "/" in ipa or "\\" in ipa:
            issues["ipa_issues"].append((w, f"音标包含斜杠: '{ipa}'"))
        elif not ipa:
            issues["ipa_issues"].append((w, "音标为空"))

        # 3. exam 漂移校验
        if w in csv_unit_data:
            csv_exam = csv_unit_data[w]["exam"]
            src_senses = set(senses(csv_exam))
            got_senses = set(senses(exam))
            bad = sorted(got_senses - src_senses)
            missing = sorted(src_senses - got_senses)

            if bad:
                issues["exam_drift_high"].append((w, f"新增义项: {bad} | 原文: {csv_exam} | 当前: {exam}"))
            elif missing and len(src_senses) > 1 and len(got_senses) == 1:
                issues["exam_drift_norm"].append((w, f"精简义项: {missing} | 原文: {csv_exam}"))

        # 4. pat 包含目标词
        stem = w[:max(3, len(w) - 2)].lower()
        if pat and stem not in pat.lower():
            issues["pat_missing_word"].append((w, f"例句未见词根 '{stem}': {pat[:50]}..."))

        # 5. c 搭配英文检查
        if not isinstance(c, list) or len(c) < 2:
            issues["collocation_err"].append((w, f"搭配少于 2 条: {c}"))
        else:
            for item in c:
                m_cjk = re.search(r"[\u4e00-\u9fff]", item)
                en_part = item[:m_cjk.start()].strip() if m_cjk else item.strip()
                # 检查搭配里的词
                en_words = re.findall(r"[a-zA-Z]+", en_part)
                for ew in en_words:
                    ew_l = ew.lower()
                    if valid_dict and len(ew_l) > 3 and ew_l not in valid_dict and ew_l not in {"sth", "sb"}:
                        issues["collocation_err"].append((w, f"搭配中可疑英文词 '{ew}': {item}"))

        # 6. 结构卡片检查
        if not isinstance(syn, list) or len(syn) < 1:
            issues["card_structure_err"].append((w, "syn 近义词为空"))
        if not isinstance(fam, list) or len(fam) < 1:
            issues["card_structure_err"].append((w, "fam 词族延伸为空"))
        if not dif:
            issues["card_structure_err"].append((w, "dif 易混辨析为空"))
        if not pat or not patZh:
            issues["card_structure_err"].append((w, "pat 或 patZh 为空"))

    return issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=r"d:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv")
    ap.add_argument("--story-dir", default=r"d:\xinyi\codespace\WowStory\单词故事本")
    ap.add_argument("--dict", default=r"d:\xinyi\codespace\WowStory\_words_alpha.txt")
    ap.add_argument("--out", default=r"d:\xinyi\codespace\WowStory\quality_audit_u01_u20.txt")
    args = ap.parse_args()

    valid_dict = load_dict(args.dict)
    csv_data = load_csv_units(args.csv)

    reports = []
    reports.append("==================================================")
    reports.append("   单词故事本 Unit 01 ~ Unit 20 全量质量深度审计报告")
    reports.append("==================================================\n")

    total_units_scanned = 0
    total_words_scanned = 0
    unit_summary = []

    for u in range(1, 21):
        json_path = os.path.join(args.story_dir, f"Unit{u:02d}.json")
        csv_u = csv_data.get(u, {})
        res = audit_unit(u, json_path, csv_u, valid_dict)
        if not res:
            reports.append(f"❌ Unit {u:02d}: JSON 文件不存在 ({json_path})")
            continue

        total_units_scanned += 1
        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)
        n_words = len(D.get("words", []))
        total_words_scanned += n_words

        high_cnt = len(res["exam_drift_high"]) + len(res["dict_typos"]) + len(res["pat_missing_word"]) + len(res["ipa_issues"])
        reports.append(f"--- Unit {u:02d} (全 {n_words} 词) 审计结果 ---")
        reports.append(f"  高风险与需关注项: {high_cnt} 处")

        if res["dict_typos"]:
            reports.append(f"  [1] 可疑拼写 ({len(res['dict_typos'])} 处):")
            for w, msg in res["dict_typos"]:
                reports.append(f"      - {w}: {msg}")

        if res["ipa_issues"]:
            reports.append(f"  [2] 音标格式异常 ({len(res['ipa_issues'])} 处):")
            for w, msg in res["ipa_issues"]:
                reports.append(f"      - {w}: {msg}")

        if res["exam_drift_high"]:
            reports.append(f"  [3] exam 常考义新增/变化 ({len(res['exam_drift_high'])} 处):")
            for w, msg in res["exam_drift_high"]:
                reports.append(f"      - {w}: {msg}")

        if res["pat_missing_word"]:
            reports.append(f"  [4] pat 例句未包含目标词 ({len(res['pat_missing_word'])} 处):")
            for w, msg in res["pat_missing_word"]:
                reports.append(f"      - {w}: {msg}")

        if res["collocation_err"]:
            reports.append(f"  [5] 搭配可疑项 ({len(res['collocation_err'])} 处):")
            for w, msg in res["collocation_err"][:8]:
                reports.append(f"      - {w}: {msg}")
            if len(res["collocation_err"]) > 8:
                reports.append(f"      ... 另有 {len(res['collocation_err']) - 8} 处")

        if res["card_structure_err"]:
            reports.append(f"  [6] 卡片缺失项 ({len(res['card_structure_err'])} 处):")
            for w, msg in res["card_structure_err"]:
                reports.append(f"      - {w}: {msg}")

        reports.append("")

    reports.append("==================================================")
    reports.append(f"总结: 共扫描 {total_units_scanned} 个 Unit，合计 {total_words_scanned} 个单词卡片。")
    reports.append("==================================================")

    out_text = "\n".join(reports)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(out_text)

    print(f"审计完成！报告已保存至 {args.out}")

if __name__ == "__main__":
    main()
