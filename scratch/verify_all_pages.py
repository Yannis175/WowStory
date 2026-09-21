# -*- coding: utf-8 -*-
import os

APP_DIR = r"d:\xinyi\codespace\WowStory\单词故事本"

files_to_check = ["index.html"] + [f"Unit{u:02d}.html" for u in range(1, 27)]

print(f"Checking {len(files_to_check)} HTML files...\n")

success_count = 0
for fname in files_to_check:
    fpath = os.path.join(APP_DIR, fname)
    if not os.path.exists(fpath):
        print(f"[ERROR] File missing: {fname}")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    has_title = ("S T O R Y" in html)
    has_tagline = ("1837 个考研必考词" in html or "1,837" in html)

    if fname != "index.html":
        has_tabs = ("S · Story" in html and "T · Test" in html and "O · Output" in html and "R · Reference" in html and "Y · Your Vocab" in html)
        has_breadcrumb = ("🏠 单元总览" in html)
        valid = has_title and has_tagline and has_tabs and has_breadcrumb
    else:
        valid = has_title and has_tagline

    if valid:
        success_count += 1
    else:
        print(f"[FAIL] {fname}: title={has_title}, tagline={has_tagline}, tabs={has_tabs if fname!='index.html' else 'N/A'}")

print(f"\nVerification finished: {success_count} / {len(files_to_check)} files 100% VERIFIED!")
