#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
word-storybook-generation / inspect_progress.py

写作过程中的**增量自检**——与 validate_unit.py 的分工：

    validate_unit.py    交卷前的正式裁判（ERROR / WARN，退出码）
    inspect_progress.py 打草稿时的进度表（JSON 还完整吗？还差哪些卡片？）

区别在于：本脚本在 words[] 只写了一部分时也能跑，不报错、只给清单。
大单元（80+ 词）必须分批写 JSON，每批之后跑一次它，能立刻发现：
  - 手滑打坏的 JSON（比如数组里多一个逗号）
  - 正文标了某个词、words[] 里却忘了建卡片（最常犯的错）
  - 建了卡片、正文却没标（反向漏标）

用法：
  python inspect_progress.py --json Unit03.json
"""
import argparse
import json
import re
import sys

MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, dest="json_path")
    a = ap.parse_args()

    try:
        D = json.load(open(a.json_path, encoding="utf-8"))
    except Exception as e:
        print("JSON 解析失败 —— 先修语法：%s" % e)
        return 1

    stories = D.get("stories") or []
    words = D.get("words") or []

    print("unit %s ｜ stories %d ｜ words %d" % (D.get("unit"), len(stories), len(words)))

    covered = set()
    for st in stories:
        n = 0
        for p in st.get("ps") or []:
            for m in MARKER.finditer(p.get("en") or ""):
                covered.add((m.group(2) or m.group(1)).strip())
                n += 1
        print("  %-4s %-24s 标记 %d" % (st.get("id"), st.get("en"), n))

    have = set(w.get("w") for w in words if w.get("w"))
    miss = sorted(covered - have)      # 正文标了，卡片没建
    extra = sorted(have - covered)     # 卡片建了，正文没标

    print("标记原形 %d 个 ｜ 已建卡片 %d 个" % (len(covered), len(have)))
    if miss:
        print("还差 %d 张卡片: %s" % (len(miss), " ".join(miss)))
    else:
        print("卡片已补齐 ✓")
    if extra:
        print("有 %d 张卡但正文没标（E41 会报）: %s" % (len(extra), " ".join(extra)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
