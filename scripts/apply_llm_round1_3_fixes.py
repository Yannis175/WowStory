import json
import os
import subprocess

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
builder = r"d:\xinyi\codespace\WowStory\scripts\build_md.py"

# 1. 修复 Round 1 单词标题 (扩展为 2-5 词具文学色彩的标题)
title_fixes = {
    (13, "s3"): ("The Growth Challenge", "增长的挑战"),
    (18, "s2"): ("The Stamp of Approval", "认可的印记"),
    (18, "s3"): ("The Displaced Community", "流离的群体"),
    (18, "s4"): ("Urban Modernization", "都市的现代化")
}

for (u, sid), (new_en, new_zh) in title_fixes.items():
    jp = os.path.join(story_dir, f"Unit{u:02d}.json")
    if os.path.exists(jp):
        with open(jp, "r", encoding="utf-8-sig") as f:
            D = json.load(f)
        for st in D.get("stories", []):
            if st.get("id") == sid:
                st["en"] = new_en
                st["zh"] = new_zh
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(D, f, ensure_ascii=False, indent=2)
        print(f"Fixed title for Unit {u:02d} [{sid}] -> '{new_en}' | '{new_zh}'")

# 2. 重新编译所有受影响的 MD 文件
for u in range(1, 21):
    jp = os.path.join(story_dir, f"Unit{u:02d}.json")
    mp = os.path.join(story_dir, f"Unit{u:02d}.md")
    if os.path.exists(jp):
        cmd_md = ["python", builder, "--json", jp, "--out", mp]
        subprocess.run(cmd_md, capture_output=True, text=True, encoding="utf-8")

print("\n全量 LLM 3 轮优化与修正部署完成！")
