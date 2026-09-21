# -*- coding: utf-8 -*-
"""把 Unit01.html 里的内联脚本原样同步到 _app.js。

约定：**页面是唯一真源**，`_app.js` 只是它的镜像（给未来的多单元页面当共享运行时用）。
所以改完页面记得跑一次：

    python _sync_app.py            # 同步并报告差异
    python _sync_app.py --check    # 只检查是否一致（不一致则退出码 1）

`--check` 可以挂在提交前的自检里，防止镜像悄悄落后。
"""
import argparse
import difflib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "Unit01.html")
APP = os.path.join(HERE, "_app.js")

OPEN_TAG = "<script>"
CLOSE_TAG = "</script>"


def script_block(html):
    i = html.find(OPEN_TAG)
    j = html.rfind(CLOSE_TAG)
    if i < 0 or j < i:
        raise SystemExit("页面里找不到 <script>…</script> 块")
    return html[i + len(OPEN_TAG):j]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查，不写")
    a = ap.parse_args()

    if not os.path.exists(PAGE):
        raise SystemExit("找不到 %s" % PAGE)
    html = open(PAGE, encoding="utf-8").read()
    new = script_block(html)
    old = open(APP, encoding="utf-8").read() if os.path.exists(APP) else ""

    if old == new:
        print("已一致 · _app.js %d 字节" % len(new.encode("utf-8")))
        return 0

    ops = [o for o in difflib.SequenceMatcher(None, old, new,
                                              autojunk=False).get_opcodes()
           if o[0] != "equal"]
    print("不一致：%d 处差异（页面 %d 字节 / 镜像 %d 字节）"
          % (len(ops), len(new.encode("utf-8")), len(old.encode("utf-8"))))
    if a.check:
        for t, a1, a2, b1, b2 in ops[:6]:
            print("  %-6s 页面 %r" % (t, new[b1:min(b2, b1 + 70)]))
        print("跑一次不带 --check 的即可同步")
        return 1

    with open(APP, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    print("已同步 -> %s（%d 字节）" % (os.path.basename(APP), len(new.encode("utf-8"))))
    for t, a1, a2, b1, b2 in ops[:6]:
        print("  %-6s 页面 %r" % (t, new[b1:min(b2, b1 + 70)]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
