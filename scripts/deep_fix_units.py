import json
import os
import re
import subprocess

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
csv_path = r"d:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv"
validator = r"d:\xinyi\codespace\WowStory\scripts\validate_unit.py"
builder = r"d:\xinyi\codespace\WowStory\scripts\build_md.py"

print("=== 开始对 Unit 01 到 Unit 20 全量数据真源进行深度校正 ===")

def clean_exam_noise(text):
    if not text:
        return text
    # 替换 OCR 乱码符号
    t = text
    t = re.sub(r'“““|“·“·|“·“|“·', '…', t)
    t = re.sub(r'theæ\)', '', t)
    t = re.sub(r'n\.Ä', '', t)
    t = re.sub(r'vt\.ü', '', t)
    t = re.sub(r'adj\.\*ß', '', t)
    t = re.sub(r'adj\.æ', '', t)
    t = re.sub(r'vt\.ié', '', t)
    t = re.sub(r'vt\.g', '', t)
    t = re.sub(r'adj\.É', '', t)
    return t

fixed_units = 0
for u in range(1, 21):
    json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
    md_path = os.path.join(story_dir, f"Unit{u:02d}.md")

    if not os.path.exists(json_path):
        print(f"Skipping Unit {u:02d}: File not found")
        continue

    with open(json_path, "r", encoding="utf-8-sig") as f:
        D = json.load(f)

    modified = False
    words = D.get("words") or []

    for w_obj in words:
        # 1. 修复 IPA 音标前后多余的斜杠和空格
        orig_ipa = w_obj.get("ipa", "")
        cleaned_ipa = orig_ipa.strip("/ ")
        if cleaned_ipa != orig_ipa:
            w_obj["ipa"] = cleaned_ipa
            modified = True

        # 2. 清洗 exam 里面的 OCR 乱码残留
        orig_exam = w_obj.get("exam", "")
        cleaned_exam = clean_exam_noise(orig_exam)
        if cleaned_exam != orig_exam:
            w_obj["exam"] = cleaned_exam
            modified = True

    if modified:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(D, f, ensure_ascii=False, indent=2)
        print(f"✅ Unit {u:02d}.json 已自动纠错并保存")
        fixed_units += 1

    # 跑硬校验
    cmd_val = ["python", validator, "--csv", csv_path, "--unit", str(u), "--json", json_path]
    res_val = subprocess.run(cmd_val, capture_output=True, text=True, encoding="utf-8")
    val_status = "PASS (ERROR 0)" if res_val.returncode == 0 else "FAIL"

    # 重新编译 MD
    cmd_md = ["python", builder, "--json", json_path, "--out", md_path]
    subprocess.run(cmd_md, capture_output=True, text=True, encoding="utf-8")

    print(f"Unit {u:02d}: Validation={val_status} -> Unit{u:02d}.md 重新编译完成")

print(f"\n全量纠错与修复完成！共修复了 {fixed_units} 个单元的数据瑕疵。")
