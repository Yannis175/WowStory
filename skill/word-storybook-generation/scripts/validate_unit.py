#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
word-storybook-generation / validate_unit.py

校验「单词故事本」单元数据（JSON）与词表 CSV 的一致性。
生成端可以换任何模型，但产物必须过这一关。

用法：
  python validate_unit.py --csv 红宝书必考词_全量汇总_清洗版.csv --unit 2 --json Unit02.json
  python validate_unit.py --csv ... --unit 2 --json Unit02.json --out report.txt

退出码：有 ERROR 返回 1，否则 0。
"""
import argparse
import csv
import json
import re
import sys

MARKER = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
SENSE_SEP = re.compile(r"[；;，,、/]")
REQUIRED_TEXT = ["w", "ipa", "pos", "s", "zh", "exam", "dif", "pat", "patZh"]
REQUIRED_LIST = ["c", "syn", "fam"]

ERRORS = []
WARNS = []
NOTES = []


def err(code, msg):
    ERRORS.append((code, msg))


def warn(code, msg):
    WARNS.append((code, msg))


def note(msg):
    NOTES.append(msg)


def senses(s):
    return [x.strip() for x in SENSE_SEP.split(s or "") if x.strip()]


def markers(text):
    out = []
    for m in MARKER.finditer(text or ""):
        surface = m.group(1).strip()
        base = (m.group(2) or m.group(1)).strip()
        out.append((surface, base))
    return out


def load_csv_unit(path, unit):
    rows = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            u = (r.get("单元") or "").strip()
            if u.lower() == ("unit %s" % unit).lower():
                rows.append({
                    "w": (r.get("单词名") or "").strip(),
                    "trans": (r.get("单词中文翻译") or "").strip(),
                    "exam": (r.get("常考含义") or "").strip(),
                })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--unit", required=True)
    ap.add_argument("--json", required=True, dest="json_path")
    ap.add_argument("--min-group", type=int, default=12)
    ap.add_argument("--max-group", type=int, default=20)
    ap.add_argument("--max-stories", type=int, default=0,
                    help="人工硬上限（默认 0 = 不限）。篇数通常不必指定，"
                         "它由词数反推，见 W02")
    ap.add_argument("--exam-strict", action="store_true",
                    help="逐词列出常考义与 CSV 原文不一致的地方（默认只给聚合提示）")
    ap.add_argument("--max-warn-items", type=int, default=6,
                    help="每类 WARN 最多列几条明细，默认 6")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    # ---------- 读输入 ----------
    csv_rows = load_csv_unit(a.csv, a.unit)
    if not csv_rows:
        err("E00", "CSV 里找不到 Unit %s 的任何行，检查 --unit 或文件路径" % a.unit)

    csv_words = [r["w"] for r in csv_rows]
    csv_exam = dict((r["w"], r["exam"]) for r in csv_rows)
    dup_csv = sorted(set(w for w in csv_words if csv_words.count(w) > 1))
    if dup_csv:
        warn("W00", "CSV 内单元有重复词条（按词族排版残留）：%s" % "、".join(dup_csv))

    try:
        with open(a.json_path, "r", encoding="utf-8-sig") as f:
            D = json.load(f)
    except Exception as e:
        err("E01", "JSON 读取失败：%s" % e)
        D = None

    # ---------- 结构 ----------
    stories = []
    words = []
    if D is not None:
        if not isinstance(D, dict):
            err("E02", "顶层不是对象，应为 {unit, stories, words}")
        else:
            if str(D.get("unit")) != str(a.unit):
                warn("W01", "DATA.unit=%r 与 --unit=%s 不一致" % (D.get("unit"), a.unit))
            stories = D.get("stories") or []
            words = D.get("words") or []
            if not isinstance(stories, list) or not stories:
                err("E03", "stories 缺失或为空")
                stories = []
            if not isinstance(words, list) or not words:
                err("E04", "words 缺失或为空")
                words = []

    # 故事字段
    sid_list = []
    for i, st in enumerate(stories):
        sid = st.get("id")
        if not sid:
            err("E10", "stories[%d] 缺 id" % i)
            continue
        if sid in sid_list:
            err("E11", "story id 重复：%s" % sid)
        sid_list.append(sid)
        for k in ("en", "zh", "theme"):
            if not (st.get(k) or "").strip():
                err("E12", "story %s 缺 %s" % (sid, k))
        ps = st.get("ps") or []
        if not ps:
            err("E13", "story %s 的 ps 为空" % sid)
        for j, p in enumerate(ps):
            if not (p.get("en") or "").strip():
                err("E14", "story %s 第 %d 段缺英文" % (sid, j + 1))
            if not (p.get("zh") or "").strip():
                err("E15", "story %s 第 %d 段缺中文译文" % (sid, j + 1))

    # 篇数：由词数反推的可行区间 —— 每组必须落在 min_group..max_group 内，
    # 所以「篇数」是每组规模的**结果**，不是独立指标。
    #   lo = 篇数下限（再少就会逼出超过 max_group 的长篇）
    #   hi = 篇数上限（再多就会切出低于 min_group 的碎片）
    n_uniq = len(set(csv_words))
    if n_uniq and stories:
        lo = (n_uniq + a.max_group - 1) // a.max_group
        hi = max(lo, n_uniq // a.min_group)
        k = len(stories)
        if k < lo:
            warn("W02", "共 %d 词却只切 %d 篇 → 平均每篇 %.1f 词，超过 %d 上限；"
                        "守住每组 %d–%d 词至少需要 %d 篇"
                 % (n_uniq, k, n_uniq / float(k), a.max_group,
                    a.min_group, a.max_group, lo))
        elif k > hi:
            warn("W02", "共 %d 词却切了 %d 篇 → 平均每篇仅 %.1f 词，低于 %d 下限；"
                        "可考虑合并到 %d 篇以内"
                 % (n_uniq, k, n_uniq / float(k), a.min_group, hi))
        if a.max_stories and k > a.max_stories:
            warn("W13", "篇数 %d 超过显式设定的 --max-stories %d" % (k, a.max_stories))

    # 词条字段
    w_list = []
    for i, x in enumerate(words):
        w = x.get("w")
        if not w:
            err("E20", "words[%d] 缺 w" % i)
            continue
        if w in w_list:
            warn("W03", "words 里重复词条：%s" % w)
        w_list.append(w)
        for k in REQUIRED_TEXT:
            if not str(x.get(k) or "").strip():
                err("E21", "%s 缺字段 %s" % (w, k))
        for k in REQUIRED_LIST:
            v = x.get(k)
            if not isinstance(v, list) or not v:
                err("E22", "%s 的 %s 必须是非空数组" % (w, k))
        c, syn, fam = x.get("c") or [], x.get("syn") or [], x.get("fam") or []
        if not (2 <= len(c) <= 4):
            warn("W04", "%s 的核心搭配 %d 条，建议 2–4 条" % (w, len(c)))
        if not (2 <= len(syn) <= 3):
            warn("W05", "%s 的近义替换 %d 条，建议 2–3 条" % (w, len(syn)))
        if len(fam) < 1:
            warn("W06", "%s 缺词族延伸" % w)
        if x.get("s") and sid_list and x["s"] not in sid_list:
            err("E23", "%s 的 s=%r 指向不存在的故事" % (w, x.get("s")))
        pat = x.get("pat") or ""
        stem = w[:max(3, len(w) - 2)].lower()
        if pat and stem not in pat.lower():
            warn("W07", "%s 的加分句式里找不到该词或其变形：%s" % (w, pat[:60]))

    # ---------- CSV 对齐 ----------
    set_csv = set(csv_words)
    set_json = set(w_list)
    missing = sorted(set_csv - set_json)
    extra = sorted(set_json - set_csv)
    if missing:
        err("E30", "CSV 有但 JSON 漏掉 %d 个词：%s" % (len(missing), "、".join(missing)))
    if extra:
        err("E31", "JSON 有但 CSV 里没有 %d 个词：%s" % (len(extra), "、".join(extra)))

    # exam 冻结校验：exam 应以 CSV 常考义为骨架。允许合并近义、去掉 OCR 括号噪声，
    # 但不该凭空新增无关义项。默认只给聚合提示，避免噪声淹没真问题。
    drift = []
    for x in words:
        w = x.get("w")
        if w not in csv_exam:
            continue
        src = set(senses(csv_exam[w]))
        got = set(senses(x.get("exam")))
        if not src:
            continue
        bad = sorted(got - src)
        if bad:
            drift.append((w, bad, csv_exam[w]))
    if drift:
        if a.exam_strict:
            for w, bad, s in drift:
                warn("W10", "%s 的常考义混入了 CSV 之外的义项：%s（原文：%s）"
                     % (w, "、".join(bad), s))
        else:
            sample = "、".join(w for w, _, _ in drift[:6])
            warn("W10", "%d/%d 个词的常考义与 CSV 原文不完全一致（多为合并近义、"
                        "去掉 OCR 括号噪声，属正常加工）：%s%s；要逐词核对加 --exam-strict"
                 % (len(drift), len(words), sample,
                    "…" if len(drift) > 6 else ""))

    # ---------- 标记完整性 ----------
    covered = set()
    per_story = {}
    for st in stories:
        sid = st.get("id")
        seen = {}
        for p in (st.get("ps") or []):
            for surface, base in markers(p.get("en") or ""):
                if base not in set_json:
                    err("E40", "标记 [[%s]] 的还原形 %r 不在 words 里（story %s）"
                        % (surface, base, sid))
                    continue
                covered.add(base)
                seen[base] = seen.get(base, 0) + 1
        per_story[sid] = len([1 for x in words if x.get("s") == sid])
        rep = sorted([k for k, v in seen.items() if v > 1])
        if rep:
            warn("W11", "story %s 里这些词被标记了多次（建议只标首次出现）：%s"
                 % (sid, "、".join(rep)))

    if set_json:
        not_in_story = sorted(set_json - covered)
        if not_in_story:
            err("E41", "以下 %d 个词在正文里完全没有标记，无法在故事中习得：%s"
                % (len(not_in_story), "、".join(not_in_story)))

    # 分组规模
    for sid, n in per_story.items():
        if n and not (a.min_group <= n <= a.max_group):
            warn("W12", "story %s 收录 %d 词，超出 %d–%d 的建议区间"
                 % (sid, n, a.min_group, a.max_group))

    # 顺序（提示，不报错）：JSON 词序应与 CSV 词序一致
    csv_order = [w for w in csv_words if w in set_json]
    if w_list and csv_order and w_list != csv_order:
        note("词序与 CSV 顺序不同（属于正常情况，w 顺序按故事分组重排）")

    # ---------- 报告 ----------
    L = []
    L.append("== 单词故事本 · Unit %s 数据校验 ==" % a.unit)
    L.append("CSV 词数 %d ｜ JSON 词数 %d ｜ 故事 %d 篇 ｜ 正文标记覆盖 %d/%d"
             % (len(csv_words), len(w_list), len(stories), len(covered), len(set_json)))
    for sid, n in per_story.items():
        L.append("  %s 收录 %d 词" % (sid, n))
    for n in NOTES:
        L.append("  · " + n)
    L.append("")
    if ERRORS:
        L.append("ERROR %d 条：" % len(ERRORS))
        for c, m in ERRORS:
            L.append("  [%s] %s" % (c, m))
    else:
        L.append("ERROR 0 条 —— 结构、覆盖、标记全部通过")
    L.append("")
    if WARNS:
        groups = []
        for c, m in WARNS:
            for g in groups:
                if g[0] == c:
                    g[1].append(m)
                    break
            else:
                groups.append((c, [m]))
        L.append("WARN %d 条（%d 类，需人工判断，不阻塞）：" % (len(WARNS), len(groups)))
        for c, ms in groups:
            for m in ms[:a.max_warn_items]:
                L.append("  [%s] %s" % (c, m))
            if len(ms) > a.max_warn_items:
                L.append("  [%s] … 另有 %d 条同类" % (c, len(ms) - a.max_warn_items))
    else:
        L.append("WARN 0 条")
    L.append("")
    L.append("结论：" + ("不通过，先修 ERROR" if ERRORS else "通过（WARN 请人工过一眼）"))
    text = "\n".join(L)

    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
