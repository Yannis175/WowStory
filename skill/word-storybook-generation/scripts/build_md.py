#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
word-storybook-generation / build_md.py

把 UnitNN.json 排成 UnitNN.md（人读版）。
不创作、不判断，只做版式——内容一律来自 JSON，避免第二处真源。

用法：
  python build_md.py --json Unit02.json --out Unit02.md
"""
import argparse
import io
import json
import re

MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
CJK = re.compile(r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]")


def bold_markers(text):
    """[[surface|base]] / [[word]] -> **surface**"""
    return MARKER.sub(lambda m: "**%s**" % m.group(1), text)


def split_bilingual(item):
    """'an investigative journalist 调查记者' -> ('an investigative journalist', '调查记者')"""
    m = CJK.search(item)
    if not m:
        return item.strip(), ""
    return item[:m.start()].strip(), item[m.start():].strip()


def bare_phrase(en):
    for art in ("a ", "an ", "the "):
        if en.lower().startswith(art):
            return en[len(art):]
    return en


def build(D):
    unit = D["unit"]
    stories = D["stories"]
    words = D["words"]
    by_story = {}
    for w in words:
        by_story.setdefault(w.get("s"), []).append(w)

    themes = []
    for st in stories:
        if st.get("theme") and st["theme"] not in themes:
            themes.append(st["theme"])

    L = []
    A = L.append
    A("# 单词故事本 · Unit %s" % unit)
    A("")
    A("> 取材：红宝书必考词 Unit %s（全 %d 词）　|　题材方向：考研英语二（%s）"
      % (unit, len(words), " · ".join(themes)))
    A("> 共 %d 篇故事，每篇 %s 词，故事内加粗词即目标词。"
      % (len(stories), "／".join(str(len(by_story.get(st["id"], []))) for st in stories)))
    A("")
    A("**怎么用**")
    A("")
    A("1. 先只读英文故事，遇到加粗的词，先猜意思，别急着往下翻。")
    A("2. 读完整篇，再逐张看考点卡片——**核心搭配**是重点，考研完形和作文就扣在这里。")
    A("3. 想核对理解时，翻到文末展开中文译文。")
    A("4. 每篇末尾有「本故事词表」，用来快速自测：看词说义，说不出的回卡片重看。")
    A("")
    A("**本篇目录**")
    A("")
    A("| 篇 | 标题 | 题材 | 收录 |")
    A("|---|---|---|---|")
    for i, st in enumerate(stories, 1):
        A("| %02d | %s｜%s | %s | %d 词 |"
          % (i, st["en"], st["zh"], st.get("theme", ""), len(by_story.get(st["id"], []))))
    A("")
    A("---")
    A("")

    idx = 0
    for i, st in enumerate(stories, 1):
        ws = by_story.get(st["id"], [])
        A("## %02d · %s｜%s" % (i, st["en"], st["zh"]))
        A("")
        A("**题材** %s　　**收录** %d 词：%s"
          % (st.get("theme", ""), len(ws), " · ".join(w["w"] for w in ws)))
        A("")
        A("### 英文故事")
        A("")
        for p in st["ps"]:
            A(bold_markers(p["en"]))
            A("")
        A("### 考点卡片")
        A("")
        for w in ws:
            idx += 1
            A("#### %02d · %s　`/%s/`　*%s*" % (idx, w["w"], w["ipa"], w["pos"]))
            A("")
            A("> 故事义 %s　·　常考义 %s" % (w["zh"], w["exam"]))
            A("")
            cis = []
            for c in w["c"]:
                en, zh = split_bilingual(c)
                cis.append("`%s`%s" % (en, (" " + zh) if zh else ""))
            A("- **核心搭配**　%s" % "　·　".join(cis))
            A("- **近义替换**　%s" % " · ".join(w["syn"]))
            A("- **词族延伸**　%s" % " → ".join(w["fam"]))
            A("- **易混辨析**　%s" % w["dif"])
            A("- **加分句式**　%s %s" % (w["pat"], w["patZh"]))
            A("")
        A("### 本故事词表")
        A("")
        A(" · ".join("%s %s" % (w["w"], w["zh"]) for w in ws))
        A("")
        A("---")
        A("")

    A("# 中文译文")
    A("")
    A("> 建议：读完英文再展开核对。译文按「意义的自然表达」处理，不逐字直译。")
    A("")
    for i, st in enumerate(stories, 1):
        A("<details>")
        A("<summary><b>%02d · %s｜%s</b></summary>" % (i, st["en"], st["zh"]))
        A("")
        A("\n\n".join(p["zh"] for p in st["ps"]))
        A("")
        A("</details>")
        A("")
    A("---")
    A("")
    A("## 附：Unit %s 全词速查" % unit)
    A("")
    A("| # | 词 | 故事义 | 常考义要点 | 必背搭配 |")
    A("|---|---|---|---|---|")
    n = 0
    for st in stories:
        for w in by_story.get(st["id"], []):
            n += 1
            key = bare_phrase(split_bilingual(w["c"][0])[0]) if w["c"] else ""
            A("| %02d | %s | %s | %s | %s |" % (n, w["w"], w["zh"], w["exam"], key))
    A("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, dest="json_path")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    D = json.load(io.open(a.json_path, encoding="utf-8-sig"))
    md = build(D)
    io.open(a.out, "w", encoding="utf-8").write(md)
    print("wrote %s (%d chars)" % (a.out, len(md)))


if __name__ == "__main__":
    main()
