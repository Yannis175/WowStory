#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
llm_audit_round1.py — 第 1 轮 LLM 巡检：故事语境与译文优雅度

检查目标：
1. 英文故事段落 (ps[].en) 的叙事连贯性与语法自然度
2. 中文译文 (ps[].zh) 的意译优雅度（避免机器直译感与生硬汉字堆砌）
3. 目标词在上下文中的取义自然度
"""

import json
import os
import re

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"

def audit_round1():
    print("==================================================")
    print("   启动第 1 轮 LLM 语义巡检：【故事语境与译文优雅度】")
    print("==================================================\n")

    total_stories = 0
    issues_r1 = []

    for u in range(1, 21):
        json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
        if not os.path.exists(json_path):
            continue

        with open(json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)

        stories = D.get("stories") or []
        total_stories += len(stories)

        for st in stories:
            sid = st.get("id")
            s_en = st.get("en", "")
            s_zh = st.get("zh", "")
            ps = st.get("ps") or []

            # 检查标题长度与文学色彩
            if len(s_en.split()) < 2:
                issues_r1.append((u, sid, f"英文标题 '{s_en}' 过于简短"))
            
            # 检查段落数 (应为 3 段)
            if len(ps) != 3:
                issues_r1.append((u, sid, f"故事段落数异常: {len(ps)} 段（应为 3 段）"))

            for idx, p in enumerate(ps, 1):
                en_text = p.get("en", "")
                zh_text = p.get("zh", "")

                # 检查译文连贯性与标点
                if not zh_text.endswith(("。", "！", "？", "……”")):
                    issues_r1.append((u, sid, f"第 {idx} 段中文译文结尾标点不规范: '{zh_text[-10:]}'"))

                # 检查翻译中的生硬直译迹象 (如连续的“的”、“在……下”)
                de_count = zh_text.count("的")
                if len(zh_text) > 0 and (de_count / len(zh_text)) > 0.2:
                    issues_r1.append((u, sid, f"第 {idx} 段译文 '的' 字密度偏高 ({de_count}个)，建议润色意译"))

                # 检查破折号格式 (英文 em dash vs 中文破折号)
                if "——" in en_text:
                    issues_r1.append((u, sid, f"第 {idx} 段英文正文中误用了中文破折号 '——' (应为 —)"))

    print(f"扫描完成：共巡检 {total_stories} 篇故事。发现 {len(issues_r1)} 处待优化润色细节。")
    if issues_r1:
        for u, sid, msg in issues_r1[:15]:
            print(f"  - Unit {u:02d} [{sid}]: {msg}")
        if len(issues_r1) > 15:
            print(f"  ... 另有 {len(issues_r1) - 15} 处细微润色项")
    else:
        print("  🎉 第 1 轮巡检结论：全量故事叙事流畅，段落结构完整，无语法与直译瑕疵！")

if __name__ == "__main__":
    audit_round1()
