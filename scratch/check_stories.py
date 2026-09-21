# -*- coding: utf-8 -*-
import json

for u in range(1, 27):
    with open(f"单词故事本/Unit{u:02d}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        sc = len(data.get("stories", []))
        wc = len(data.get("words", []))
        print(f"Unit {u:02d}: {sc} stories, {wc} words")
