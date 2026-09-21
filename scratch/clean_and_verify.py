# -*- coding: utf-8 -*-
import re
import os

FILE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Clean lines 422-430 (duplicate sticky-right block)
# Clean lines 3796-3802 (dead JS syntax error)

new_lines = []
skip_dup_html = False
skip_dead_js = False

for i, line in enumerate(lines):
    line_num = i + 1
    # Check duplicate HTML block: lines around 422
    if '<div class="sticky-right">' in line and lines[i-1].strip() == '</div>' and lines[i-2].strip() == '</div>':
        skip_dup_html = True
        print(f"Skipping duplicate HTML starting at line {line_num}")
        continue
    if skip_dup_html:
        if line.strip() == '</div>' and lines[i+1].strip() == '<div id="app"></div>':
            skip_dup_html = False
            print(f"Ended duplicate HTML skip at line {line_num}")
            continue
        continue

    # Check dead JS syntax error: lines around 3796
    if 'if(menu && menu.classList.contains("on")){' in line:
        skip_dead_js = True
        print(f"Skipping dead JS starting at line {line_num}")
        continue
    if skip_dead_js:
        if line.strip() == '}' and lines[i+1].strip() == '':
            skip_dead_js = False
            print(f"Ended dead JS skip at line {line_num}")
            continue
        continue

    new_lines.append(line)

content = "".join(new_lines)

# Write back
with open(FILE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(content)

print("Cleaned Unit01.html!")
