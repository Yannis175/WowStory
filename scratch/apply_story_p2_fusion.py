# -*- coding: utf-8 -*-
import re

# 1. Update index.html
INDEX_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\index.html"
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    idx = f.read()

idx = idx.replace("<title>单词故事本 · 全 26 单元故事合集</title>", "<title>S T O R Y · 1837 个考研必考词，穿成 121 篇故事</title>")
idx = idx.replace('<meta name="apple-mobile-web-app-title" content="单词故事本">', '<meta name="apple-mobile-web-app-title" content="S T O R Y">')
idx = idx.replace('.brand h1{font-family:var(--serif);font-size:32px;font-weight:700;margin:0;letter-spacing:.02em;color:var(--ink)}',
                  '.brand h1{font-family:var(--serif);font-size:36px;font-weight:700;margin:0;letter-spacing:.15em;color:var(--clay2)}')
idx = idx.replace('<h1>单词故事本 · 全集</h1>', '<h1>S T O R Y</h1>')
idx = idx.replace('<p>考研英语一 / 英语二必考词全量故事串记（Unit 01 ~ Unit 26）</p>', '<p>单词故事本 —— 1837 个考研必考词，穿成 121 篇故事</p>')
idx = idx.replace('placeholder="🔍 搜索任意考研单词 / 中文释义（覆盖全量 1,837 词）..."', 'placeholder="🔍 搜索 S T O R Y 中的任意考研单词 / 中文释义（覆盖全量 1,837 词）..."')
idx = idx.replace('<div class="footer">单词故事本 · 考研英语真题句式与故事记忆系统</div>', '<div class="footer">S T O R Y · 单词故事本 —— 考研英语真题句式与故事记忆系统</div>')

with open(INDEX_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(idx)
print("Updated index.html with STORY name + P2 style.")

# 2. Update Unit01.html template
TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    tpl = f.read()

tpl = tpl.replace("<title>单词故事本 · Unit 1</title>", "<title>S T O R Y · Unit 1</title>")

# Brand area
old_brand = re.search(r'<div class="brand">[\s\S]*?</div>\s*<div class="unit-nav">', tpl)
new_brand = """<div class="brand">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
        <a href="index.html" class="home-link" title="返回全量 26 单元合集首页">🏠 单元总览</a>
        <span style="font-size:11px;color:var(--ink3)">/</span>
        <span style="font-size:12px;color:var(--clay2);font-weight:600" id="headerUnitTag">Unit 1</span>
      </div>
      <h1 style="font-family:var(--serif);font-size:28px;font-weight:700;margin:0;letter-spacing:.15em;color:var(--clay2)"><a href="index.html" style="text-decoration:none !important;color:inherit" title="返回首页">S T O R Y</a></h1>
      <p style="margin:6px 0 0;font-size:12.5px;color:var(--ink2)">单词故事本 —— 1837 个考研必考词，穿成 121 篇故事</p>
    </div>"""

if old_brand:
    tpl = tpl[:old_brand.start()] + new_brand + tpl[old_brand.end()-22:]

# Tabs area
old_tabs = re.search(r'<div class="tabs" id="tabs">[\s\S]*?</div>', tpl)
new_tabs = """<div class="tabs" id="tabs">
        <button class="tab" data-tab="read">📖 读<small>S · Story 猜词</small></button>
        <button class="tab" data-tab="drill">🎴 背<small>T · Test 自测</small></button>
        <button class="tab" data-tab="write">✍️ 写<small>O · Output 素材</small></button>
        <button class="tab" data-tab="index">🔍 查<small>R · Reference 速查</small></button>
        <button class="tab" data-tab="vocab">📓 本<small>Y · Your Vocab 生词</small></button>
      </div>"""

if old_tabs:
    tpl = tpl[:old_tabs.start()] + new_tabs + tpl[old_tabs.end():]

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(tpl)

print("Updated Unit01.html template with STORY name + P2 style.")
