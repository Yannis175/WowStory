# -*- coding: utf-8 -*-
import re

with open("单词故事本/Unit01.html", "r", encoding="utf-8") as f:
    text = f.read()

style_blocks = re.findall(r'<style>([\s\S]*?)</style>', text)
print(f"Found {len(style_blocks)} style blocks.")

for idx, css in enumerate(style_blocks):
    open_b = css.count('{')
    close_b = css.count('}')
    print(f"Style block {idx+1}: {open_b} open braces, {close_b} close braces.")
    if open_b != close_b:
        print("WARNING: Unbalanced braces in CSS!")

    # Check for invalid syntax like .foo{.bar{
    bad_matches = re.findall(r'(\.[a-zA-Z0-9_-]+\s*\{\s*\.[a-zA-Z0-9_-]+\s*\{)', css)
    if bad_matches:
        print("BAD MATCHES FOUND IN CSS:", bad_matches)
    else:
        print("No nested malformed selectors found.")
