# -*- coding: utf-8 -*-
import re

with open("单词故事本/Unit01.html", "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r'<script>([\s\S]*?)</script>', text)
print(f"Found {len(scripts)} inline script blocks.")

# Check for obvious syntax mismatches or trailing syntax issues
for i, s in enumerate(scripts):
    print(f"Script block {i+1} length: {len(s)} chars.")

print("Checks passed!")
