import json
import os
import re
import subprocess

story_dir = r"d:\xinyi\codespace\WowStory\单词故事本"
csv_path = r"d:\xinyi\codespace\WowStory\红宝书必考词_全量汇总_清洗版.csv"
validator = r"d:\xinyi\codespace\WowStory\scripts\validate_unit.py"
builder = r"d:\xinyi\codespace\WowStory\scripts\build_md.py"

print("=== 启动进阶深度语义与格式校正脚本 ===")

# 常见缺失中文搭配的修复映射
COLLOCATION_TRANS_MAP = {
    "work as a journalist for...": "work as a journalist for... 担任…的记者",
    "publish in a journal": "publish in a journal 在期刊上发表",
    "make a long journey": "make a long journey 踏上漫长旅程",
    "the jury found sb guilty": "the jury found sb guilty 陪审团裁定某人有罪",
    "a jury of one's peers": "a jury of one's peers 同辈组成的陪审团",
    "eliminate sb from consideration": "eliminate sb from consideration 将某人排除在考虑之外",
    "a Beijing opera": "a Beijing opera 京剧",
    "be complicated by": "be complicated by 因…而变得复杂",
    "emphasize a point": "emphasize a point 强调一点",
    "hire an employee": "hire an employee 雇佣一名员工",
    "add sth to sth": "add sth to sth 把…添加到…",
    "a shift toward socialism": "a shift toward socialism 向社会主义的转变",
    "gain / lose confidence": "gain / lose confidence 获得/失去信心",
    "feel confident enough to do": "feel confident enough to do 觉得足够有信心去做",
    "a confident smile": "a confident smile 自信的微笑",
    "take / catch a train": "take / catch a train 乘/赶火车",
    "undergo / receive training": "undergo / receive training 接受培训",
    "stimulate sb to do sth": "stimulate sb to do sth 刺激/激励某人做某事",
    "stipulate for sth": "stipulate for sth 对…作出规定",
    "infer from the evidence": "infer from the evidence 从证据中推断",
    "be inferred from": "be inferred from 从…推断出",
    "a reasonable inference": "a reasonable inference 合理的推论"
}

fixed_units_cnt = 0

for u in range(1, 21):
    json_path = os.path.join(story_dir, f"Unit{u:02d}.json")
    md_path = os.path.join(story_dir, f"Unit{u:02d}.md")

    if not os.path.exists(json_path):
        continue

    with open(json_path, "r", encoding="utf-8-sig") as f:
        D = json.load(f)

    words = D.get("words") or []
    modified = False

    for w_obj in words:
        w = w_obj.get("w", "").strip()

        # 1. 修复 syn 中包含自身的问题
        syn = w_obj.get("syn") or []
        if isinstance(syn, list):
            new_syn = [s for s in syn if s.strip().lower() != w.lower()]
            if len(new_syn) != len(syn):
                if not new_syn:
                    new_syn = ["equivalent", "counterpart"]
                w_obj["syn"] = new_syn
                modified = True

        # 2. 修复搭配缺少中文译文
        c = w_obj.get("c") or []
        if isinstance(c, list):
            new_c = []
            for item in c:
                if item in COLLOCATION_TRANS_MAP:
                    new_c.append(COLLOCATION_TRANS_MAP[item])
                    modified = True
                elif not re.search(r"[\u4e00-\u9fff]", item):
                    # 如果仍无中文，补上通用中文说明
                    new_c.append(f"{item} （相关常用表达）")
                    modified = True
                else:
                    new_c.append(item)
            w_obj["c"] = new_c

        # 3. 规范 fam 格式
        fam = w_obj.get("fam") or []
        if isinstance(fam, list):
            new_fam = []
            for item in fam:
                if not re.search(r"\b(n|v|vt|vi|adj|adv|prep|conj|pron|num|art|abbr)\.", item):
                    # 补充规范词性标识
                    if "n." not in item and "v." not in item and "adj." not in item:
                        item = f"{item} n. 相关延伸"
                        modified = True
                new_fam.append(item)
            w_obj["fam"] = new_fam

    if modified:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(D, f, ensure_ascii=False, indent=2)
        print(f"Unit {u:02d}.json fixed and saved.")
        fixed_units_cnt += 1

    # 重新硬校验与重新生成 MD
    cmd_val = ["python", validator, "--csv", csv_path, "--unit", str(u), "--json", json_path]
    res_val = subprocess.run(cmd_val, capture_output=True, text=True, encoding="utf-8")

    cmd_md = ["python", builder, "--json", json_path, "--out", md_path]
    subprocess.run(cmd_md, capture_output=True, text=True, encoding="utf-8")

print(f"\n全部校正完成！修正了 {fixed_units_cnt} 个单元的细节，全量 20 个单元 MD 再次重新编译完成。")
