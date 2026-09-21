#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
deep_semantic_audit.py — 进阶深度质检脚本

检查细项：
1. fam 规范格式校验: 必须包含词性标签 (n./v./adj./adv. 等)
2. pat 与 patZh 对齐度: 句子与翻译均不能为空，且长度合理
3. c 核心搭配双语格式: 英文 + 中文释义是否成对
4. dif 辨析丰富度: 长度 >= 10 个字符，不能有敷衍回答
5. syn 近义词有效性: 不应包含单词自身，且元素为非空字符串
6. 故事正文标记复核: 单篇故事内同词重复标记提示
"""

import json
import os
import re

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

def audit_deep():
    total_issues = 0
    unit_reports = {}

    for u in range(1, 21):
        json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
        if not os.path.exists(json_path):
            continue

        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)

        words = D.get("words") or []
        stories = D.get("stories") or []

        issues = {
            "fam_format": [],
            "c_format": [],
            "dif_short": [],
            "syn_self": [],
            "pat_mismatch": [],
            "story_repeat_tags": []
        }

        # 1. 检查故事内重复标记
        for st in stories:
            sid = st.get("id")
            seen = {}
            for p in st.get("ps") or []:
                for m in MARKER.finditer(p.get("en") or ""):
                    base = (m.group(2) or m.group(1)).strip()
                    seen[base] = seen.get(base, 0) + 1
            repeats = [k for k, v in seen.items() if v > 1]
            if repeats:
                issues["story_repeat_tags"].append((sid, repeats))

        # 2. 检查单词卡片细项
        for x in words:
            w = (x.get("w") or "").strip()
            c = x.get("c") or []
            syn = x.get("syn") or []
            fam = x.get("fam") or []
            dif = (x.get("dif") or "").strip()
            pat = (x.get("pat") or "").strip()
            patZh = (x.get("patZh") or "").strip()

            # fam 格式检查 (应带有词性如 n. v. adj. adv.)
            for item in fam:
                if not re.search(r"\b(n|v|vt|vi|adj|adv|prep|conj|pron|num|art|abbr)\.", item):
                    issues["fam_format"].append((w, f"fam 缺少标准词性: '{item}'"))

            # c 格式检查 (应有英文与中文)
            for item in c:
                if not re.search(r"[\u4e00-\u9fff]", item):
                    issues["c_format"].append((w, f"搭配缺少中文译文: '{item}'"))

            # dif 辨析太短
            if len(dif) < 10:
                issues["dif_short"].append((w, f"辨析过短 ({len(dif)}字): '{dif}'"))

            # syn 包含自身
            for s_item in syn:
                if s_item.strip().lower() == w.lower():
                    issues["syn_self"].append((w, f"近义词包含自身: '{s_item}'"))

            # pat / patZh 长度或空
            if len(pat) < 15 or len(patZh) < 5:
                issues["pat_mismatch"].append((w, f"例句或译文过短: pat='{pat}', patZh='{patZh}'"))

        unit_issues_cnt = sum(len(v) for v in issues.values())
        if unit_issues_cnt > 0:
            unit_reports[u] = issues
            total_issues += unit_issues_cnt

    print(f"=== 进阶深度质检完成！共排查 20 个 Unit，发现 {total_issues} 处细节可优化项 ===")
    for u, iss in unit_reports.items():
        print(f"\n--- Unit {u:02d} ---")
        for k, v in iss.items():
            if v:
                print(f"  [{k}] ({len(v)} 处):")
                for item in v[:5]:
                    print(f"    - {item}")
                if len(v) > 5:
                    print(f"    ... 另有 {len(v) - 5} 处")

if __name__ == "__main__":
    audit_deep()
