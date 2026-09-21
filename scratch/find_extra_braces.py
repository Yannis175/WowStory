# -*- coding: utf-8 -*-
import re

with open("单词故事本/Unit01.html", "r", encoding="utf-8") as f:
    text = f.read()

style_match = re.search(r'<style>([\s\S]*?)</style>', text)
if style_match:
    css = style_match.group(1)
    lines = css.splitlines()
    depth = 0
    for line_num, line in enumerate(lines, 1):
        o = line.count('{')
        c = line.count('}')
        depth += (o - c)
        if depth < 0:
            print(f"Line {line_num}: Extra closing brace! Content: {line.strip()}")
            depth = 0
        if o > 0 or c > 0:
            pass
    print(f"Final CSS brace depth after scanning: {depth}")
