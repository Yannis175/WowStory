# -*- coding: utf-8 -*-
"""
生成多单元清单与全量索引 bundle 数据 _units_manifest.js 以及全量索引数据。
用于在 index.html 及各单元 HTML 中实现全量 26 单元卡片弹窗切换与跨单元搜索。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
APP_DIR = os.path.join(PROJ, "单词故事本")

def build_units_bundle():
    manifest = []
    all_words_index = []

    for u in range(1, 27):
        json_path = os.path.join(APP_DIR, f"Unit{u:02d}.json")
        if not os.path.exists(json_path):
            continue
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        stories = data.get("stories", [])
        words = data.get("words", [])

        themes = list(dict.fromkeys([s.get("theme", "") for s in stories if s.get("theme")]))

        manifest.append({
            "unit": u,
            "title": f"Unit {u:02d}",
            "storiesCount": len(stories),
            "wordsCount": len(words),
            "themes": themes,
            "url": f"Unit{u:02d}.html"
        })

        for w in words:
            all_words_index.append({
                "w": w.get("w"),
                "ipa": w.get("ipa", ""),
                "pos": w.get("pos", ""),
                "zh": w.get("zh", ""),
                "exam": w.get("exam", ""),
                "unit": u,
                "url": f"Unit{u:02d}.html#index"
            })

    manifest_js = "window.UNITS_MANIFEST = " + json.dumps(manifest, ensure_ascii=False, indent=2) + ";\n"
    manifest_js += "window.ALL_WORDS_INDEX = " + json.dumps(all_words_index, ensure_ascii=False) + ";\n"

    out_path = os.path.join(APP_DIR, "_units_manifest.js")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(manifest_js)

    print(f"[成功] 已生成 _units_manifest.js (收录 26 单元, {len(all_words_index)} 考点词词条, {os.path.getsize(out_path)} 字节)")

if __name__ == "__main__":
    build_units_bundle()
