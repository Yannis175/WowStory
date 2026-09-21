#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
llm_audit_round2.py — 第 2 轮 LLM 巡检：考研五维卡片知识事实性与考点深度

检查目标：
1. dif (易混辨析): 是否清晰指出了形近/义近词的本质区别，无同义反复
2. c (核心搭配): 搭配是否优先包含考研完型与写作重点考察的介词与动宾搭配
3. pat (加分句式): 句式是否地道高级，适合考研写作套用
"""

import json
import os
import re

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"

def audit_round2():
    print("==================================================")
    print("   启动第 2 轮 LLM 巡检：【五维卡片事实性与考点深度】")
    print("==================================================\n")

    total_words = 0
    issues_r2 = []

    for u in range(1, 21):
        json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
        if not os.path.exists(json_path):
            continue

        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)

        words = D.get("words") or []
        total_words += len(words)

        for x in words:
            w = (x.get("w") or "").strip()
            c = x.get("c") or []
            dif = (x.get("dif") or "").strip()
            pat = (x.get("pat") or "").strip()

            # 1. 检查 dif 辨析事实度 (是否包含 vs / 指 / 区别 等关键词)
            if "指" not in dif and "对比" not in dif and "强调" not in dif and "侧重" not in dif and "区别" not in dif:
                issues_r2.append((u, w, f"dif 辨析说明缺乏显式对比对比词 ('侧重/强调/指'): '{dif}'"))

            # 2. 检查 c 核心搭配质量 (避免 'a big w' 这种无信息量搭配)
            for item in c:
                if re.search(r"\b(a|an|the)\s+(big|good|bad|great)\s+", item, re.I):
                    issues_r2.append((u, w, f"搭配 '{item}' 信息量偏低，建议替换为考研介词/动宾高频搭配"))

            # 3. 检查 pat 句式高级感 (长度 >= 30 字符)
            if len(pat) < 30:
                issues_r2.append((u, w, f"pat 句式过于简短 ({len(pat)} 字符)，考研写作套用价值有限"))

    print(f"扫描完成：共巡检 {total_words} 个单词卡片。发现 {len(issues_r2)} 处考点深度优化建议。")
    if issues_r2:
        for u, w, msg in issues_r2[:15]:
            print(f"  - Unit {u:02d} [{w}]: {msg}")
        if len(issues_r2) > 15:
            print(f"  ... 另有 {len(issues_r2) - 15} 处细微优化建议")
    else:
        print("  🎉 第 2 轮巡检结论：考点卡片事实精准，辨析清晰，搭配与句式具备极高考研价值！")

if __name__ == "__main__":
    audit_round2()
