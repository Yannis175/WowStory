# -*- coding: utf-8 -*-
import re

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Update .pick CSS
html = re.sub(r'\.pick\{display:grid;grid-template-columns:repeat\(auto-fill,minmax\(210px,1fr\)\);gap:12px\}',
              '.pick{display:grid;gap:12px}', html)

# Update viewRead pick rendering
old_view_read = """function viewRead(){
  var st = DATA.stories[state.story];
  var h = '<div class="label">选一篇开始读</div><div class="pick">';"""

new_view_read = """function viewRead(){
  var st = DATA.stories[state.story];
  var sCnt = DATA.stories.length;
  var cols = (sCnt === 5) ? 5 : ((sCnt === 6) ? 3 : sCnt);
  var h = '<div class="label">选一篇开始读</div><div class="pick" style="grid-template-columns:repeat(' + cols + ',1fr)">';"""

if old_view_read in html:
    html = html.replace(old_view_read, new_view_read)

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Updated Unit01.html pick grid logic!")
