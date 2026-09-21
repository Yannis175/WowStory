# -*- coding: utf-8 -*-
import os
import re

ROOT = r"d:\xinyi\codespace\WowStory"

keywords = [
    "单词故事本", "单元总览", "读故事猜词", "背遮词自测", "写表达素材",
    "全词速查", "我的生词", "返回 26 单元总览", "返回全量 26 单元"
]

matched_files = {}

for dirpath, dirnames, filenames in os.walk(ROOT):
    if any(x in dirpath for x in [".vcache", ".workbuddy", "__pycache__", ".git", "_archive"]):
        continue
    for fname in filenames:
        if fname.endswith((".html", ".js", ".py", ".md", ".txt", ".json")):
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                found_kws = [kw for kw in keywords if kw in content]
                if found_kws:
                    rel_path = os.path.relpath(fpath, ROOT)
                    matched_files[rel_path] = found_kws
            except Exception as e:
                pass

print(f"Audit complete. Found {len(matched_files)} files with target keywords:\n")
for path, kws in matched_files.items():
    print(f"  - {path}: {', '.join(kws)}")
