# -*- coding: utf-8 -*-
import re

# 1. Update index.html .wrap max-width to 900px
INDEX_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\index.html"
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = idx_content.replace(".wrap{max-width:1080px;", ".wrap{max-width:900px;")
idx_content = re.sub(r'\.grid\{display:grid;grid-template-columns:repeat\(auto-fill,minmax\(320px,1fr\)\);gap:20px\}',
                     '.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}', idx_content)

with open(INDEX_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(idx_content)
print("Updated index.html .wrap max-width to 900px.")

# 2. Update Unit01.html .wrap max-width to 900px
TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    tpl_content = f.read()

tpl_content = tpl_content.replace(".wrap{max-width:1040px;", ".wrap{max-width:900px;")
# Update grid minmax for 900px wrap
tpl_content = re.sub(r'\.grid\{display:grid;grid-template-columns:repeat\(auto-fill,minmax\(286px,1fr\)\);gap:14px\}',
                     '.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}', tpl_content)

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(tpl_content)
print("Updated Unit01.html .wrap max-width to 900px.")
