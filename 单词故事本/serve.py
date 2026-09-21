#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单词故事本 · 本地预览服务器
==============================================================
它做两件事：

1) 给页面一个稳定的「真 URL」
   页面里的音频全是相对路径 audio/...，实体放在与本 HTML 同级的 audio
   文件夹里。只有让页面以真 URL 打开，浏览器才找得到这些文件。被内嵌预览
   （about: / blob:）加载时，相对路径解析不到磁盘，朗读会报「音频没找到」。

2) 本机 API：让页面点一下就能给生词补发音
   POST /api/vocab/audio   起一个生成任务（后台跑，页面轮询进度）
   GET  /api/job/<id>      任务进度
   POST /api/setup         一键准备朗读引擎（建项目内 venv + 装 edge-tts）
   GET  /api/ping          这台机器能不能自动生成、写接口开没开

   生成逻辑不在这里，在 vocab_audio.py（手动跑 _gen_vocab.py 也是同一份代码）。

常用：
    双击 serve.cmd            最简单（等价于 python serve.py）
    python serve.py --lan     允许局域网访问，手机/平板可开（通勤路上听）
    python serve.py --lan --allow-write   连写接口一起开（默认关，见下）
    python serve.py --port 9000          指定起始端口（默认 8899，占用则自动 +1）
    python serve.py --python <路径>      指定用哪个 python 生成音频
    python serve.py --no-browser         不自动打开浏览器

安全：写接口（补音频 / 装引擎）默认只在绑 127.0.0.1 时开放。--lan 之后同 WiFi
下别的设备也能访问，那里默认关掉写接口 —— 否则任何同网设备都能让你机器上的
python 去调外部语音服务并往你硬盘写文件。要用就显式加 --allow-write。

按 Ctrl+C 停止。
"""
import argparse
import glob
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import time
import uuid
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))      # 服务器根 = 本目录
PROJ = os.path.dirname(HERE)                            # 项目根
DEFAULT_PAGE = "Unit01.html"
WORKER = os.path.join(HERE, "vocab_audio.py")
VENV = os.path.join(PROJ, ".ttsenv")                    # 项目内的朗读引擎环境
JOBS_DIR = os.path.join(PROJ, ".vcache", "jobs")        # 任务临时文件（不被 http 暴露）
EN_VOICES = ("aria", "guy", "andrew")
MAX_ITEMS = 300
FNAME_RE = re.compile(r"^[a-z0-9_]{1,64}$")             # f 会当文件名用，必须卡死
KEEP_JOBS = 30

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, HERE)
try:
    import vocab_audio as VA            # 只为复用 vfname / build_plan，缺 edge-tts 也能 import
except Exception as _e:                 # pragma: no cover
    VA = None
    VA_ERR = repr(_e)
else:
    VA_ERR = None

LAN = False
WRITE_OK = True
CLI_PYTHON = None
JOBS = {}
JOBS_LOCK = threading.Lock()
_PY = {"path": None, "ver": None, "probe": "pending", "canVenv": None}   # probe: pending / done
_PY_LOCK = threading.Lock()


# ---------------------------------------------------------------- 环境探测
def in_use(port):
    """端口是否已有人在监听。用 connect 探测而不是 bind —— Windows 上
    SO_REUSEADDR 允许 bind 到已被占用的端口，靠 bind 会误判成空闲。"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        return s.connect_ex(("127.0.0.1", port)) == 0
    except Exception:
        return False
    finally:
        s.close()


def lan_ip():
    """取本机在局域网里的地址，取不到就退回 127.0.0.1"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def _run_quiet(args, timeout=30):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                           encoding="utf-8", errors="replace")
        return r.returncode, (r.stdout or ""), (r.stderr or "")
    except Exception as e:
        return -1, "", repr(e)


def _edge_ok(path):
    """这个解释器能不能 import edge_tts？能就返回版本号"""
    rc, out, _ = _run_quiet([path, "-c", "import edge_tts;print(edge_tts.__version__)"], timeout=25)
    if rc == 0 and out.strip():
        return out.strip().splitlines()[-1].strip()
    return None


def py_candidates():
    """按「最可能有 edge-tts」的顺序列出候选解释器"""
    home = os.path.expanduser("~")
    out = []
    if CLI_PYTHON:
        out.append(CLI_PYTHON)
    out += [
        os.path.join(VENV, "Scripts", "python.exe"),      # 本脚本一键装的那个，首选
        os.path.join(VENV, "bin", "python"),
        sys.executable,
    ]
    pats = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Python", "Python3*", "python.exe"),
        os.path.join(home, ".workbuddy", "binaries", "python", "envs", "*", "Scripts", "python.exe"),
        os.path.join(home, ".workbuddy", "binaries", "python", "envs", "*", "bin", "python"),
        os.path.join(home, ".workbuddy", "binaries", "python", "versions", "*", "python.exe"),
        r"C:\Python3*\python.exe",
        "/usr/bin/python3",
    ]
    for p in pats:
        out += sorted(glob.glob(p))
    for c in ("python", "python3", "py"):
        w = shutil.which(c)
        if w:
            out.append(w)
    seen, uniq = set(), []
    for p in out:
        if not p:
            continue
        try:
            k = os.path.normcase(os.path.abspath(p))
        except Exception:
            continue
        if k not in seen and os.path.exists(p):
            seen.add(k)
            uniq.append(p)
    return uniq


def find_python(force=False):
    """找一个装了 edge-tts 的解释器，结果缓存。force=True 重新探（装完引擎后）"""
    with _PY_LOCK:
        if _PY["probe"] == "done" and not force:
            return _PY["path"], _PY["ver"]
        _PY["probe"] = "pending"
        found = None
        for p in py_candidates():
            v = _edge_ok(p)
            if v:
                found = (p, v)
                break
        _PY["path"], _PY["ver"] = found if found else (None, None)
        _PY["probe"] = "done"
        if found:
            print("[生成] 用这个解释器：%s（edge-tts %s）" % (found[0], found[1]))
            sys.stdout.flush()
        return _PY["path"], _PY["ver"]


def can_make_venv():
    """能不能建 venv（装引擎用）。只要 python 本身在就行。结果缓存，别每次 ping 都探一遍"""
    if _PY["canVenv"] is not None:
        return _PY["canVenv"] or None
    for p in py_candidates():
        rc, _, _ = _run_quiet([p, "-c", "import venv"], timeout=20)
        if rc == 0:
            _PY["canVenv"] = p
            return p
    _PY["canVenv"] = ""
    return None


# ---------------------------------------------------------------- 任务
def _job_new(kind, total=0):
    jid = uuid.uuid4().hex[:12]
    d = os.path.join(JOBS_DIR, jid)
    os.makedirs(d, exist_ok=True)
    j = {"id": jid, "kind": kind, "state": "running", "phase": "preparing",
         "t0": time.time(), "total": total, "done": 0, "new": 0, "reuse": 0,
         "skip": 0, "fail": 0, "failed": [], "error": None, "hint": None,
         "log": "", "dir": d, "voice": None, "proc": None}
    with JOBS_LOCK:
        JOBS[jid] = j
        if len(JOBS) > KEEP_JOBS:
            for k in sorted(JOBS, key=lambda x: JOBS[x]["t0"])[:-KEEP_JOBS]:
                old = JOBS.pop(k, None)
                if old:
                    shutil.rmtree(old["dir"], ignore_errors=True)
    return j


def _job_read_state(j):
    """worker 边跑边写的进度（done 是数磁盘上的文件，不靠 stdout 解析）"""
    p = j.get("statefile")
    if not p or not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _job_finish(j, rc, log):
    """worker 退出后收尾：读结果文件，定 final state"""
    j["proc"] = None
    j["log"] = (log or "")[-1500:]
    res = None
    p = j.get("resfile")
    if p and os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as f:
                res = json.load(f)
        except Exception:
            res = None
    if res:
        for k in ("total", "done", "new", "reuse", "skip", "fail", "failed"):
            if k in res:
                j[k] = res[k]
    if j["state"] == "running":
        if res and res.get("ok"):
            j["state"] = "done"
            j["phase"] = "done"
        elif res and res.get("error"):
            j["state"] = "error"
            j["error"] = res.get("error")
            j["hint"] = res.get("hint") or ("生成脚本报错，看日志：" + (j["log"] or "").strip()[-400:])
        elif rc == 0:
            j["state"] = "done"
            j["phase"] = "done"
        else:
            j["state"] = "error"
            j["error"] = "worker_failed"
            j["hint"] = (j["log"] or "").strip()[-400:] or ("退出码 %s" % rc)


def _run_worker(j, timeout):
    py, ver = find_python()
    if not py:
        j.update(state="error", error="no_edge_tts",
                 hint="这台机器上没找到装了 edge-tts 的 python。点「准备朗读引擎」可以自动装一次。")
        return
    cmd = [py, WORKER, j["jobfile"], j["resfile"], "--state", j["statefile"]]
    log = ""
    try:
        p = subprocess.Popen(cmd, cwd=HERE, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True,
                             encoding="utf-8", errors="replace")
        j["proc"] = p
        try:
            log = p.communicate(timeout=timeout)[0] or ""
            rc = p.returncode
        except subprocess.TimeoutExpired:
            p.kill()
            log = (p.communicate()[0] or "")
            j.update(state="error", error="timeout",
                     hint="等了 %d 秒还没跑完，已中止。多半是网络卡了，重试一次通常就好。" % timeout)
            rc = -1
    except Exception as e:
        j.update(state="error", error="spawn_failed", hint=repr(e)[:300])
        return
    _job_finish(j, rc, log)


def start_gen(voice, items):
    """起一个生成任务。items 已由 clean_items 校验过"""
    j = _job_new("gen", total=len(items) * 2)
    j["voice"] = voice
    j["jobfile"] = os.path.join(j["dir"], "job.json")
    j["resfile"] = os.path.join(j["dir"], "result.json")
    j["statefile"] = os.path.join(j["dir"], "state.json")
    with open(j["jobfile"], "w", encoding="utf-8") as f:
        json.dump({"voice": voice, "items": items}, f, ensure_ascii=False)
    if VA:      # 计划阶段先把分母算准（跳过/复用的也是产出）
        try:
            jobs, pre = VA.build_plan(voice, items)
            j["total"] = len(jobs) + len(pre)
            j["willTts"] = len(jobs)
            # 全都已经躺在磁盘上（补过一次又点了一次）→ 不必起进程，直接结束。
            # 省掉一次 python 启动 + import edge-tts，点击手感是「瞬间」
            if pre and not jobs and all(p["kind"] == "skip" for p in pre):
                j.update(state="done", phase="done", done=len(pre), skip=len(pre))
                return j
        except Exception:
            pass
    timeout = min(1800, max(150, 40 * max(1, j["total"])))
    threading.Thread(target=_run_worker, args=(j, timeout), daemon=True).start()
    return j


def start_setup():
    """建项目内 venv 并装 edge-tts（一次性的）"""
    j = _job_new("setup", total=2)
    threading.Thread(target=_run_setup, args=(j,), daemon=True).start()
    return j


def _run_setup(j):
    base = can_make_venv()
    if not base:
        j.update(state="error", error="no_python",
                 hint="机器上找不到可用的 python，没法自动装。装一个 Python 再来。")
        return
    j["phase"] = "venv"
    rc, out, err = _run_quiet([base, "-m", "venv", VENV], timeout=300)
    if rc != 0 or not os.path.exists(VENV):
        j.update(state="error", error="venv_failed",
                 hint="建虚拟环境失败：%s" % ((err or out).strip()[-300:] or "未知原因"))
        return
    j["done"] = 1
    j["phase"] = "pip"
    pip = os.path.join(VENV, "Scripts" if os.name == "nt" else "bin",
                       "pip.exe" if os.name == "nt" else "pip")
    if not os.path.exists(pip):
        pip = os.path.join(VENV, "Scripts" if os.name == "nt" else "bin", "pip")
    rc, out, err = _run_quiet([pip, "install", "--disable-pip-version-check",
                               "--quiet", "edge-tts"], timeout=600)
    j["log"] = ((out or "") + (err or ""))[-1500:]
    if rc != 0:
        j.update(state="error", error="pip_failed",
                 hint="装 edge-tts 失败（多半是网络）。日志：%s" % (j["log"].strip()[-300:] or "空"))
        return
    j["done"] = 2
    j["phase"] = "probe"
    find_python(force=True)          # 装完立刻重探，页面接着就能用
    if _PY["path"]:
        j.update(state="done", phase="done")
    else:
        j.update(state="error", error="still_missing",
                 hint="装完了但还是找不到，可能装到了别的环境。重启一次服务器再试。")


def clean_items(raw):
    """校验并规整页面传来的词条。返回 (items, 丢弃数)"""
    if not isinstance(raw, list):
        return None, 0
    out, bad = [], 0
    for x in raw[:MAX_ITEMS]:
        if not isinstance(x, dict):
            bad += 1
            continue
        w = str(x.get("w", "")).strip()
        if not w or len(w) > 64:
            bad += 1
            continue
        f = str(x.get("f", "")).strip()
        if not FNAME_RE.match(f):          # f 会当文件名，不合法就重算，绝不放行
            f = VA.vfname(w) if VA else (re.sub(r"[^a-z0-9]+", "_", w.lower()).strip("_") or "x")
        zh = str(x.get("zh", "")).strip()[:200]
        out.append({"w": w, "f": f, "zh": zh})
    return out, bad


def job_view(j):
    """给页面的任务快照。运行中优先用 worker 写的进度（数文件更准）"""
    v = {"id": j["id"], "kind": j["kind"], "state": j["state"], "phase": j["phase"],
         "total": j["total"], "done": j["done"], "new": j["new"], "reuse": j["reuse"],
         "skip": j["skip"], "fail": j["fail"], "failed": j["failed"],
         "error": j["error"], "hint": j["hint"], "voice": j["voice"],
         "ms": int((time.time() - j["t0"]) * 1000)}
    st = _job_read_state(j)
    if st and j["state"] == "running":
        for k in ("total", "done", "new", "fail"):
            if k in st:
                v[k] = st[k]
        v["phase"] = st.get("phase") or v["phase"]
    if j["state"] == "error" and not v["hint"]:
        v["hint"] = (j["log"] or "").strip()[-400:] or None
    return v


# ---------------------------------------------------------------- HTTP
class Handler(SimpleHTTPRequestHandler):
    """目录浏览保留；日志静音；顺手关掉缓存，改完文件刷新即见
    另外提供 /api/* 的本地接口（只服务本机页面）"""

    def log_message(self, fmt, *args):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    # ---- 小工具
    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except Exception:
            pass

    def _body(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except Exception:
            return None
        if n <= 0 or n > 4 * 1024 * 1024:
            return None
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception:
            return None

    def _guard_write(self):
        """写接口的三道门。返回拒绝理由，None 表示放行。

        中间那道 X-WowStory 是关键：跨站请求带自定义头会触发 CORS 预检，
        而本服务器不回 CORS 头，浏览器就把请求拦了 —— 免得你随便打开的
        某个网页偷偷往你硬盘写文件、或让本机去调外部语音服务。
        """
        if not WRITE_OK:
            return ("服务器是 --lan 模式启动的，写接口默认关闭（怕同 WiFi 下别的设备"
                    "往你硬盘写东西）。要用就重启：serve.cmd --lan --allow-write")
        if self.headers.get("X-WowStory") != "1":
            return "缺少本地页面标识，已拒绝。"
        org = (self.headers.get("Origin") or "").strip()
        if org and not (org.startswith("http://127.0.0.1") or org.startswith("http://localhost")
                        or org.startswith("http://[::1]")):
            return "来源不是本机页面，已拒绝。"
        return None

    # ---- 路由
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/api/ping":
            return self._api_ping()
        if path.startswith("/api/job/"):
            jid = path[len("/api/job/"):].strip("/")
            with JOBS_LOCK:
                j = JOBS.get(jid)
            if not j:
                return self._json({"ok": False, "error": "no_such_job"}, 404)
            return self._json({"ok": True, "job": job_view(j)})
        if path.startswith("/api/"):
            return self._json({"ok": False, "error": "not_found"}, 404)
        if path in ("/", "/index.html"):
            page = "index.html" if os.path.exists(os.path.join(HERE, "index.html")) else DEFAULT_PAGE
            self.send_response(302)
            self.send_header("Location", "/" + page)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ("/api/vocab/audio", "/api/setup"):
            return self._json({"ok": False, "error": "not_found"}, 404)
        why = self._guard_write()
        if why:
            return self._json({"ok": False, "error": "write_disabled", "hint": why}, 403)
        if VA is None:
            return self._json({"ok": False, "error": "worker_missing",
                               "hint": "vocab_audio.py 没能加载：%s" % VA_ERR}, 500)

        if path == "/api/setup":
            return self._json({"ok": True, "job": job_view(start_setup())})

        d = self._body()
        if not isinstance(d, dict):
            return self._json({"ok": False, "error": "bad_body",
                               "hint": "请求体不是合法 JSON"}, 400)
        voice = str(d.get("voice") or "aria")
        if voice not in EN_VOICES:
            return self._json({"ok": False, "error": "bad_voice",
                               "hint": "音色只能是 %s" % "、".join(EN_VOICES)}, 400)
        items, dropped = clean_items(d.get("items"))
        if not items:
            return self._json({"ok": False, "error": "no_items",
                               "hint": "没有要生成的词（收到 %s 条，可用 0 条）" % (
                                   len(d.get("items") or []))}, 400)
        j = start_gen(voice, items)
        return self._json({"ok": True, "job": job_view(j), "accepted": len(items),
                           "dropped": dropped})

    def do_OPTIONS(self):
        # 不回 CORS 头 —— 跨站预检到这里就失败，正是我们要的
        self.send_response(204)
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ---- /api/ping
    def _api_ping(self):
        path, ver = find_python()
        gen = {"available": bool(path), "python": path, "edgeTts": ver,
               "probe": _PY["probe"],
               "venv": os.path.relpath(VENV, PROJ),
               "canSetup": bool(can_make_venv()) if not path else True}
        if not path:
            gen["hint"] = ("这台机器上没找到装了 edge-tts 的 python。"
                           "可以在这里点「准备朗读引擎」自动装一次（约 30 秒）。")
        return self._json({
            "ok": True, "server": "wowstory", "page": DEFAULT_PAGE,
            "lan": LAN, "write": WRITE_OK, "voices": list(EN_VOICES),
            "audio": os.path.isdir(os.path.join(HERE, "audio")),
            "worker": VA is not None,
            "gen": gen,
        })


class Server(ThreadingHTTPServer):
    daemon_threads = True
    # Windows 上必须关掉：开着的话第二个进程能绑到同一端口，请求会乱窜
    allow_reuse_address = False


def serve_on(host, start):
    """从 start 起找第一个能真正绑上的端口，绑定成功才返回"""
    last = None
    for p in range(start, start + 40):
        if in_use(p):
            continue
        try:
            return p, Server((host, p), partial(Handler, directory=HERE))
        except OSError as e:
            last = e
            continue
    raise SystemExit("端口 %d-%d 都绑不上（%s），换个 --port 再来。" % (start, start + 39, last))


def main():
    global LAN, WRITE_OK, CLI_PYTHON
    ap = argparse.ArgumentParser(description="单词故事本 本地预览服务器")
    ap.add_argument("--port", type=int, default=8899, help="起始端口（默认 8899，占用则自动 +1）")
    ap.add_argument("--lan", action="store_true", help="绑 0.0.0.0，同一 WiFi 下的手机/平板可访问")
    ap.add_argument("--allow-write", action="store_true",
                    help="--lan 时也开放写接口（补音频 / 装引擎）。默认关")
    ap.add_argument("--python", help="指定用哪个 python 生成音频（默认自动找带 edge-tts 的）")
    ap.add_argument("--no-browser", action="store_true", help="不自动打开浏览器")
    ap.add_argument("--page", default=DEFAULT_PAGE, help="启动后打开的页面（默认 %s）" % DEFAULT_PAGE)
    a = ap.parse_args()

    os.chdir(HERE)
    CLI_PYTHON = a.python
    LAN = a.lan
    WRITE_OK = (not a.lan) or a.allow_write

    shutil.rmtree(JOBS_DIR, ignore_errors=True)       # 上次的任务残留清掉
    os.makedirs(JOBS_DIR, exist_ok=True)

    host = "0.0.0.0" if a.lan else "127.0.0.1"
    port, srv = serve_on(host, a.port)
    url = "http://127.0.0.1:%d/%s" % (port, a.page)

    threading.Thread(target=find_python, daemon=True).start()   # 先探着，别卡启动

    bar = "─" * 54
    print(bar)
    print("  单词故事本 · 本地预览已启动")
    print(bar)
    print("  电脑打开    %s" % url)
    if a.lan:
        print("  手机打开    http://%s:%d/%s" % (lan_ip(), port, a.page))
        print("             （手机要连同一个 WiFi；首次可能弹防火墙，允许即可）")
        print("  写接口      %s" % ("已开放" if WRITE_OK else "关闭（要开就加 --allow-write）"))
    else:
        print("  手机访问    重启时加 --lan 参数即可（如 serve.cmd --lan）")
    print()
    print("  根目录      %s" % HERE)
    print("  音频        audio/ 已就位，朗读可直接用")
    print("  补发音      页面「本 → 补音频」点一下就能生成；引擎环境 %s" % os.path.relpath(VENV, PROJ))
    print()
    print("  按 Ctrl+C 停止")
    print(bar)
    sys.stdout.flush()

    if not a.no_browser:
        threading.Timer(0.7, lambda: webbrowser.open(url)).start()

    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止。")
    finally:
        srv.server_close()


if __name__ == "__main__":
    main()
