# -*- coding: utf-8 -*-
"""生词的离线发音生成核心（被两种入口共用）。

两种入口：
  ① 手动：项目根目录 `python _gen_vocab.py`（读 vocab.json）
  ② 自动：页面点「一键补音频」→ serve.py 起本文件的 __main__（读 job.json）

本文件是「怎么生成」的唯一真源，两个入口都不许再抄一遍逻辑。

命令行（serve.py 用的就是这条）：
    python vocab_audio.py <job.json> <result.json>

job.json:  {"voice": "aria", "items": [{"w": "...", "f": "...", "zh": "..."}]}
   * f 是页面算好的文件名，优先用它 —— 以后页面改了 vfname 规则也不会错位
   * zh 为空则不生成中文音频
result.json: 见 build_result()，进度由 run() 边跑边写（现写现覆盖，供轮询）

两个设计要点：
  * 音频落在 audio/<音色>/vw/ 与 audio/zh/vwz/，与书里的 audio/<音色>/w/ 是两个
    目录 —— 生词和书里的词哪怕同名也是两个文件，不会互相覆盖。
  * 书里已经有同一个词就先复制过来，不重复调语音服务（省时且音色完全一致）。
"""
import argparse
import asyncio
import json
import os
import re
import shutil
import sys
import time

try:
    import edge_tts
    EDGE_TTS_ERR = None
except ImportError as e:      # 不在这里抛 —— serve.py 要复用它算文件名，得能 import 成功
    edge_tts = None
    EDGE_TTS_ERR = str(e)

# 本文件在 单词故事本/ 下，音频就在旁边
HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(HERE, "audio")

EN_VOICE = {"aria": "en-US-AriaNeural", "guy": "en-US-GuyNeural", "andrew": "en-US-AndrewNeural"}
ZH_VOICE = "zh-CN-XiaoxiaoNeural"
MIN = 800                      # 小于这个字节数当作没生成成功（与 _gen.py 同口径）
CONCURRENCY = 4
RETRY = 3


# ---------------------------------------------------------------- 命名 / 查找
def vfname(w):
    """必须与页面里的 vfname() 完全一致：小写 + 连续非字母数字压成一个下划线。"""
    s = re.sub(r"[^a-z0-9]+", "_", str(w).strip().lower()).strip("_")
    return s or "x"


def booksafe(w):
    """书里 _gen.py 的 safe()：保留大小写与 - _"""
    return re.sub(r"[^A-Za-z0-9_-]", "_", w)


class BookIndex:
    """书里现有音频的索引，惰性建（每个目录只列一次）

    英文在 audio/<音色>/w/，中文在 audio/zh/wz/（中文只有一套，不按音色分）。
    从背模式「没记住」收进来的词，这两处通常都已经有了 —— 那就直接复制，
    一次网络请求都不用发（这是最常见的情况，所以值得单独建索引）。
    """

    def __init__(self, audio=AUDIO):
        self.audio = audio
        self._cache = {}

    def _ls(self, d):
        if d not in self._cache:
            self._cache[d] = os.listdir(d) if os.path.isdir(d) else []
        return self._cache[d]

    def _pick(self, d, names):
        for n in self._ls(d):
            if n.lower() in names:
                p = os.path.join(d, n)
                if ok(p):
                    return p
        return None

    def find_en(self, voice, w, fname=None):
        names = {(booksafe(w) + ".mp3").lower(), (vfname(w) + ".mp3").lower()}
        if fname:
            names.add((fname + ".mp3").lower())
        return self._pick(os.path.join(self.audio, voice, "w"), names)

    def find_zh(self, w, fname=None):
        names = {(booksafe(w) + ".mp3").lower(), (vfname(w) + ".mp3").lower()}
        if fname:
            names.add((fname + ".mp3").lower())
        return self._pick(os.path.join(self.audio, "zh", "wz"), names)


def ok(path):
    return os.path.exists(path) and os.path.getsize(path) >= MIN


# ---------------------------------------------------------------- 计划
def build_plan(voice, items, audio=AUDIO, index=None):
    """把词表摊成「要产出哪些文件」。

    返回 (jobs, pre)：jobs 是要调语音服务的 [(文本, 音色, 目标路径)]，
    pre 是已经就位/可直接复用的清单 —— 计划阶段就能算出来的都先算掉，
    这样进度条的分母一开始就是准的。
    """
    index = index or BookIndex(audio)
    jobs, pre = [], []
    for x in items:
        w = str(x.get("w", "")).strip()
        if not w:
            continue
        f = str(x.get("f", "")).strip() or vfname(w)
        dst = os.path.join(audio, voice, "vw", f + ".mp3")
        if ok(dst):
            pre.append({"w": w, "kind": "skip", "path": dst})
            continue
        src = index.find_en(voice, w, f)
        if src:
            pre.append({"w": w, "kind": "reuse", "path": dst, "src": src})
            continue
        jobs.append({"w": w, "kind": "tts", "path": dst, "text": w, "voice": EN_VOICE[voice]})
    for x in items:
        w = str(x.get("w", "")).strip()
        zh = str(x.get("zh", "")).strip()
        if not w or not zh:
            continue
        f = str(x.get("f", "")).strip() or vfname(w)
        dst = os.path.join(audio, "zh", "vwz", f + ".mp3")
        if ok(dst):
            pre.append({"w": w, "kind": "skip", "path": dst})
            continue
        src = index.find_zh(w, f)
        if src:
            pre.append({"w": w, "kind": "reuse", "path": dst, "src": src})
            continue
        jobs.append({"w": w, "kind": "tts", "path": dst, "text": zh, "voice": ZH_VOICE})
    return jobs, pre


def all_paths(jobs, pre):
    return [j["path"] for j in jobs] + [p["path"] for p in pre]


# ---------------------------------------------------------------- 生成
class Runner:
    def __init__(self, jobs, pre, state_path=None, audio=AUDIO):
        self.jobs = jobs
        self.pre = pre
        self.state_path = state_path
        self.audio = audio
        self.total = len(jobs) + len(pre)
        self.new = 0
        self.fail = 0
        self.failed = []
        self.t0 = time.time()
        self._lock = asyncio.Lock()

    async def _write_state(self, phase):
        if not self.state_path:
            return
        d = {"phase": phase, "total": self.total, "done": self._done(),
             "new": self.new, "fail": self.fail,
             "elapsed": round(time.time() - self.t0, 1)}
        tmp = self.state_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        os.replace(tmp, self.state_path)

    def _done(self):
        return sum(1 for p in all_paths(self.jobs, self.pre) if ok(p))

    async def _one(self, job, sem):
        path = job["path"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if edge_tts is None:
            self.fail += 1
            self.failed.append({"w": job["w"], "err": "没装 edge-tts"})
            return
        async with sem:
            for attempt in range(RETRY):
                try:
                    c = edge_tts.Communicate(job["text"], job["voice"])
                    with open(path, "wb") as f:
                        async for ch in c.stream():
                            if ch["type"] == "audio":
                                f.write(ch["data"])
                    if os.path.getsize(path) < MIN:
                        raise RuntimeError("文件太小")
                    self.new += 1
                    break
                except Exception as e:
                    if attempt == RETRY - 1:
                        if os.path.exists(path):
                            try:
                                os.remove(path)
                            except OSError:
                                pass
                        self.fail += 1
                        self.failed.append({"w": job["w"], "err": repr(e)[:160]})
                    else:
                        await asyncio.sleep(1.5 * (attempt + 1))
            await self._write_state("running")

    async def run(self):
        await self._write_state("running")
        # 复用/跳过的先就地落位（复制很快），这样进度条不会一开始卡着不动
        for p in self.pre:
            if p["kind"] == "reuse" and not ok(p["path"]):
                os.makedirs(os.path.dirname(p["path"]), exist_ok=True)
                try:
                    shutil.copyfile(p["src"], p["path"])
                except OSError as e:
                    self.fail += 1
                    self.failed.append({"w": p["w"], "err": repr(e)[:160]})
        await self._write_state("running")
        if self.jobs:
            sem = asyncio.Semaphore(CONCURRENCY)
            await asyncio.gather(*[self._one(j, sem) for j in self.jobs])
        await self._write_state("done")
        return self.result()

    def result(self):
        return {
            "ok": self.fail == 0,
            "total": self.total,
            "done": self._done(),
            "new": self.new,
            "reuse": sum(1 for p in self.pre if p["kind"] == "reuse"),
            "skip": sum(1 for p in self.pre if p["kind"] == "skip"),
            "fail": self.fail,
            "failed": self.failed[:20],
            "elapsed": round(time.time() - self.t0, 1),
        }


def generate(voice, items, state_path=None, audio=AUDIO):
    """同步入口（两种调用方式都走它）"""
    jobs, pre = build_plan(voice, items, audio)
    r = Runner(jobs, pre, state_path=state_path, audio=audio)
    return asyncio.run(r.run())


# ---------------------------------------------------------------- 词表读取
def load_words(path):
    """读页面导出的词表；顺手容忍「只有 words 数组」的裸 JSON"""
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, list):
        return data
    return data.get("words") or []


def pick_voices(arg_voices, data_voices=None):
    cand = [v for v in (arg_voices or data_voices or list(EN_VOICE))]
    return [v for v in cand if v in EN_VOICE]


# ---------------------------------------------------------------- 命令行
def main(argv=None):
    ap = argparse.ArgumentParser(description="给生词本补发音")
    ap.add_argument("job", nargs="?", help="job.json（自动模式：serve.py 传进来）")
    ap.add_argument("result", nargs="?", help="result.json（自动模式）")
    ap.add_argument("--json", default=os.path.join(os.path.dirname(HERE), "vocab.json"),
                    help="页面导出的词表（手动模式，默认 <项目根>/vocab.json）")
    ap.add_argument("--voice", action="append", metavar="ID",
                    help="只补指定音色，可重复：aria / guy / andrew")
    ap.add_argument("--force", action="store_true", help="已存在的也重新生成")
    ap.add_argument("--state", help="把实时进度写到这里（自动模式用）")
    a = ap.parse_args(argv)

    if edge_tts is None:
        msg = ("跑本脚本的这个 python 没装 edge-tts。装一下：\n"
               "    pip install edge-tts\n"
               "（注意要装到同一个解释器里，机器上有多个 python 时最容易踩这个坑）\n"
               "原始错误：%s" % EDGE_TTS_ERR)
        print(msg)
        if a.result:
            with open(a.result, "w", encoding="utf-8") as f:
                json.dump({"ok": False, "error": "no_edge_tts", "hint": msg}, f, ensure_ascii=False)
        return 2

    # ---- 自动模式：serve.py 起的，一次一个音色，结果写 result.json
    if a.job:
        job = json.load(open(a.job, encoding="utf-8"))
        voice = job.get("voice") or "aria"
        if voice not in EN_VOICE:
            res = {"ok": False, "error": "未知音色：" + str(voice)}
        else:
            try:
                res = generate(voice, job.get("items") or [], state_path=a.state)
            except Exception as e:       # 网络/依赖问题都收拢成可读结果
                res = {"ok": False, "error": repr(e)[:300]}
        if a.result:
            with open(a.result, "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False)
        print(json.dumps(res, ensure_ascii=False))
        return 0 if res.get("ok") else 1

    # ---- 手动模式：读 vocab.json，可一次补多个音色
    if not os.path.exists(a.json):
        print("找不到词表：" + a.json)
        print("可以改成在页面里点「本 → 补音频 / 导出 → 一键补音频」，就不用管文件了。")
        return 1
    raw = json.load(open(a.json, encoding="utf-8"))
    words = [x for x in load_words(a.json) if str(x.get("w", "")).strip()]
    if not words:
        print("词表里没有词，没什么要补的。")
        return 1
    voices = pick_voices(a.voice, (raw or {}).get("voices") if isinstance(raw, dict) else None)
    if not voices:
        print("没有可用音色，可选：" + "、".join(EN_VOICE))
        return 1
    if not os.path.isdir(AUDIO):
        print("警告：没找到音频目录 %s —— 生成的音频会和页面失联。" % AUDIO)

    if a.force:
        for v in voices:
            for x in words:
                p = os.path.join(AUDIO, v, "vw", (x.get("f") or vfname(x["w"])) + ".mp3")
                if os.path.exists(p):
                    os.remove(p)

    print("生词 %d 个 · 音色 %s" % (len(words), "、".join(voices)))
    total = {"new": 0, "reuse": 0, "skip": 0, "fail": 0}
    bad = []
    for v in voices:
        res = generate(v, words)
        for k in total:
            total[k] += res.get(k, 0)
        bad += res.get("failed") or []
        print("  %-7s 新生成 %d · 复用 %d · 已存在 %d · 失败 %d"
              % (v, res.get("new", 0), res.get("reuse", 0), res.get("skip", 0), res.get("fail", 0)))

    print("\n合计：新生成 %d · 复用 %d · 已存在跳过 %d · 失败 %d"
          % (total["new"], total["reuse"], total["skip"], total["fail"]))
    if bad:
        print("\n失败的（多为网络问题，重跑即可，已成功的不会重做）：")
        for x in bad[:10]:
            print("  %s :: %s" % (x.get("w"), x.get("err")))
        return 1
    print("\n搞定。回页面刷新一下，生词就能读了。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
