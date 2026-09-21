# -*- coding: utf-8 -*-
import re

with open("单词故事本/Unit01.html", "r", encoding="utf-8") as f:
    u1 = f.read()

with open("单词故事本/Unit03.html", "r", encoding="utf-8") as f:
    u3 = f.read()

# Strip DATA js from both
u1_clean = re.sub(r'var DATA = \{[\s\S]*?\};', 'var DATA = {};', u1)
u3_clean = re.sub(r'var DATA = \{[\s\S]*?\};', 'var DATA = {};', u3)

# Strip PT js from both
u1_clean = re.sub(r'var PT = \{[\s\S]*?\};', 'var PT = {};', u1_clean)
u3_clean = re.sub(r'var PT = \{[\s\S]*?\};', 'var PT = {};', u3_clean)

# Replace Unit 1 -> Unit 3
u1_clean = u1_clean.replace("Unit 1", "Unit 3").replace("Unit 01", "Unit 3").replace("53", "84")

diff_same = (u1_clean == u3_clean)
print("Are Unit01 and Unit03 structurally identical except DATA?", diff_same)

if not diff_same:
    for i, (line1, line3) in enumerate(zip(u1_clean.splitlines(), u3_clean.splitlines())):
        if line1 != line3:
            print(f"Diff at line {i+1}:\n  U1: {line1[:80]}\n  U3: {line3[:80]}")
