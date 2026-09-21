# -*- coding: utf-8 -*-
"""
用微软 Edge 神经网络语音为指定单元 (如 Unit 2) 离线生成全量 mp3 音频与 PT 句级时间轴。
使用包含 edge-tts 的 Python 解释器。
"""
import asyncio
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
APP_DIR = os.path.join(PROJ, "单词故事本")
OUT = os.path.join(APP_DIR, "audio")

EN_VOICE = {
    "aria": "en-US-AriaNeural",
    "guy": "en-US-GuyNeural",
    "andrew": "en-US-AndrewNeural"
}
ZH_VOICE = "zh-CN-XiaoxiaoNeural"

MK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
SENT = re.compile(r"[^.!?]+[.!?]*\s*")
ABBR = re.compile(r"(^|[\s(])(Dr|Mr|Mrs|Ms|Prof|St|vs|etc|No|Jr|Sr)\.", re.I)

clean = lambda s: MK.sub(lambda m: m.group(1), s)
safe = lambda w: re.sub(r"[^A-Za-z0-9_-]", "_", w)

def _split(full):
    prot = ABBR.sub(lambda m: m.group(1) + m.group(2) + "\u0001", full)
    return [t.replace("\u0001", ".").strip() for t in SENT.findall(prot) if t.strip()]

def sentences(raw):
    full = clean(raw)
    return full, _split(full)

def sayable(t):
    t = re.sub(r"\bsb\b", "somebody", t)
    t = re.sub(r"\bsth\b", "something", t)
    t = re.sub(r"…|\.\.\.", ", ", t)
    t = re.sub(r"[·／]", " ", t)
    return re.sub(r"\s{2,}", " ", t).strip()

try:
    import edge_tts
except ImportError:
    print("[错误] 未安装 edge-tts")
    sys.exit(1)

SEM = asyncio.Semaphore(6)
FAIL = []

async def gen(text, voice, path, want_marks=False, force=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and os.path.getsize(path) > 800 and not force:
        return [] if want_marks else None
    async with SEM:
        for attempt in range(3):
            try:
                c = edge_tts.Communicate(text, voice)
                marks = []
                
                async def stream_audio():
                    with open(path, "wb") as f:
                        async for ch in c.stream():
                            if ch["type"] == "audio":
                                f.write(ch["data"])
                            elif ch["type"] == "SentenceBoundary":
                                marks.append((ch["offset"] / 1e7, ch.get("text", "")))

                await asyncio.wait_for(stream_audio(), timeout=25.0)
                if os.path.getsize(path) < 800:
                    raise RuntimeError("too small")
                return marks if want_marks else None
            except Exception as e:
                if attempt == 2:
                    FAIL.append(path + " :: " + repr(e)[:120])
                    if os.path.exists(path):
                        try:
                            os.remove(path)
                        except Exception:
                            pass
                    return [] if want_marks else None
                await asyncio.sleep(1.2 * (attempt + 1))
    return [] if want_marks else None

async def build_zh(data, u_num):
    print("== 中文 Xiaoxiao ==")
    jobs = []
    prefix = f"u{u_num:02d}_"
    for st in data["stories"]:
        for k, p in enumerate(st["ps"]):
            jobs.append((p["zh"], os.path.join(OUT, "zh", f"{prefix}pz{st['id']}-{k}.mp3")))
    for w in data["words"]:
        jobs.append((w["zh"] + "。" + w["exam"], os.path.join(OUT, "zh", "wz", safe(w["w"]) + ".mp3")))
        jobs.append((w["patZh"], os.path.join(OUT, "zh", "patz", safe(w["w"]) + ".mp3")))
    await asyncio.gather(*[gen(t, ZH_VOICE, p) for t, p in jobs])
    print("中文任务完成: %d 个" % len(jobs))

async def build_en(data, vk, u_num):
    voice = EN_VOICE[vk]
    print("== 英文 " + voice + " ==")
    para, other = [], []
    prefix = f"u{u_num:02d}_"
    pt_path = os.path.join(APP_DIR, "pt_data", f"_pt_u{u_num:02d}.json")
    existing_pt = {}
    if os.path.exists(pt_path):
        try:
            with open(pt_path, "r", encoding="utf-8") as f:
                existing_pt = json.load(f).get(vk, {})
        except Exception:
            existing_pt = {}

    for st in data["stories"]:
        for k, p in enumerate(st["ps"]):
            full, parts = sentences(p["en"])
            para.append({
                "key": "%s-%d" % (st["id"], k),
                "full": full,
                "parts": parts,
                "path": os.path.join(OUT, vk, f"{prefix}p{st['id']}-{k}.mp3"),
            })
    for w in data["words"]:
        other.append((w["w"], os.path.join(OUT, vk, "w", safe(w["w"]) + ".mp3")))
        other.append((sayable(clean(w["pat"])), os.path.join(OUT, vk, "pat", safe(w["w"]) + ".mp3")))
        for i, c in enumerate(w.get("c", [])):
            other.append((sayable(clean(c)), os.path.join(OUT, vk, "chip", "%s_%d.mp3" % (safe(w["w"]), i))))

    # 如果所有段落 MP3 已存在且已有有效 PT 时间轴，直接复用，避免重新请求网络
    all_paras_exist = all(os.path.exists(p["path"]) and os.path.getsize(p["path"]) > 800 for p in para)
    all_pts_exist = all(p["key"] in existing_pt and len(existing_pt[p["key"]]) == len(p["parts"]) for p in para)

    if all_paras_exist and all_pts_exist:
        print(f"  [复用] {vk} 段落音频与 PT 时间轴已完整就绪，自动跳过网络请求")
        pres = [None] * len(para)
        PT = existing_pt
    else:
        pres = await asyncio.gather(*[gen(p["full"], voice, p["path"], want_marks=True, force=True) for p in para])
        PT = {}
        for i, p in enumerate(para):
            marks, parts = pres[i] or [], p["parts"]
            if len(marks) == len(parts):
                PT[p["key"]] = [round(m[0], 2) for m in marks]
                continue
            if marks:
                total = marks[-1][0] + max(1.2, len(parts[-1]) / 14.0)
            else:
                total = sum(len(x) for x in parts) / 14.0
            weights = [len(x) for x in parts]
            acc, s = [], 0
            for w in weights:
                acc.append(s)
                s += w
            tot = float(sum(weights)) or 1.0
            PT[p["key"]] = [round(total * a / tot, 2) for a in acc]

    await asyncio.gather(*[gen(t, voice, p) for t, p in other])
    return PT

async def process_unit(u_num):
    json_path = os.path.join(APP_DIR, f"Unit{u_num:02d}.json")
    if not os.path.exists(json_path):
        print(f"[错误] 找不到数据文件: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"\n--- 开始生成 Unit {u_num:02d} 音频与 PT 时间轴 ---")
    await build_zh(data, u_num)

    pt_all = {}
    for vk in ["aria", "guy", "andrew"]:
        pt = await build_en(data, vk, u_num)
        pt_all[vk] = pt

    # 将生成的 PT 时间轴保存或写回数据中
    pt_path = os.path.join(APP_DIR, "pt_data", f"_pt_u{u_num:02d}.json")
    with open(pt_path, "w", encoding="utf-8") as f:
        json.dump(pt_all, f, ensure_ascii=False, indent=2)

    print(f"[成功] Unit {u_num:02d} 音频与 PT 时间轴已就绪！PT: {pt_path}")

def main():
    u_num = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    asyncio.run(process_unit(u_num))

if __name__ == "__main__":
    main()
