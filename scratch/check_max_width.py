# -*- coding: utf-8 -*-
import re

for fname in ["index.html", "Unit01.html", "Unit03.html"]:
    with open(f"单词故事本/{fname}", "r", encoding="utf-8") as f:
        text = f.read()
    mw = re.findall(r'([.#a-zA-Z0-9_-]+\s*\{[^}]*max-width:[^}]+|\.wrap\s*\{[^}]*\})', text)
    print(f"=== {fname} ===")
    for m in mw:
        print("  ", m.replace("\n", " "))
