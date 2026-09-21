import csv
import json

csv_path = r'd:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv'
rows = []
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        u = (r.get('单元') or '').strip()
        if u.lower() == 'unit 17':
            rows.append({
                'w': (r.get('单词名') or '').strip(),
                'trans': (r.get('单词中文翻译') or '').strip(),
                'exam': (r.get('常考含义') or '').strip()
            })

with open('u17_raw.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"Unit 17 Extracted {len(rows)} words.")
for i, r in enumerate(rows, 1):
    print(f"{i:02d}. {r['w']} | {r['trans']} | {r['exam']}")
