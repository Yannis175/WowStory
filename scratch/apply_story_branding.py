# -*- coding: utf-8 -*-
import re

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Title Tag
html = html.replace("<title>单词故事本 · Unit 1</title>", "<title>S T O R Y · Unit 1</title>")

# 2. Add home-text-link CSS
css_addition = """.home-text-link{font-size:12px;color:var(--ink2);font-weight:600;text-decoration:none;transition:.15s}
.home-text-link:hover{color:var(--clay)}
.logo-title{font-family:var(--serif);font-size:34px;font-weight:700;margin:0;letter-spacing:.18em;color:var(--clay2);line-height:1.15}
.logo-title a{color:inherit;text-decoration:none;transition:.15s}
.logo-title a:hover{color:var(--clay)}
.brand-tagline{margin:6px 0 0;font-size:13px;color:var(--ink2)}

.tab{flex:1;border:1px solid var(--line);background:rgba(255,251,246,.85);border-radius:999px;
  padding:7px 4px;font-size:16px;font-family:var(--serif);font-weight:700;color:var(--ink2);transition:.16s ease;text-align:center;
  display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;white-space:nowrap}
.tab:hover{border-color:var(--clay);color:var(--clay2);background:#fff}
.tab.on{background:var(--clay);color:#fff;border-color:var(--clay);box-shadow:0 2px 8px rgba(200,100,59,.22)}
.tab small{display:block;font-size:9.5px;font-family:var(--sans);font-weight:400;opacity:.8;margin-top:1px}
.tab.on small{opacity:.95}"""

# Replace old .home-link and .brand h1 styling
html = re.sub(r'\.home-link\{[\s\S]*?\.brand p\{margin:6px 0 0;font-size:12\.5px;color:var\(--ink2\)\}', css_addition, html)

# 3. Replace Brand Area HTML
old_brand_html = re.search(r'<div class="brand">[\s\S]*?</div>\s*<div class="unit-nav">', html)
new_brand_html = """<div class="brand">
      <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px">
        <a href="index.html" class="home-text-link" title="返回目录首页">目录</a>
        <span style="font-size:11px;color:var(--ink3)">/</span>
        <span style="font-size:12px;color:var(--clay2);font-weight:600" id="headerUnitTag">Unit 1</span>
      </div>
      <h1 class="logo-title"><a href="index.html" title="点按返回目录首页">S T O R Y</a></h1>
      <p class="brand-tagline">单词故事本 —— 1837 个考研必考词，穿成 121 篇故事</p>
    </div>"""

if old_brand_html:
    html = html[:old_brand_html.start()] + new_brand_html + html[old_brand_html.end()-22:]

# 4. Replace 5 Tabs HTML
old_tabs_html = re.search(r'<div class="tabs" id="tabs">[\s\S]*?</div>', html)
new_tabs_html = """<div class="tabs" id="tabs">
        <button class="tab" data-tab="read">S<small>Story 读故事</small></button>
        <button class="tab" data-tab="drill">T<small>Test 背自测</small></button>
        <button class="tab" data-tab="write">O<small>Output 写素材</small></button>
        <button class="tab" data-tab="index">R<small>Reference 查速查</small></button>
        <button class="tab" data-tab="vocab">Y<small>Your Vocab 生词本</small></button>
      </div>"""

if old_tabs_html:
    html = html[:old_tabs_html.start()] + new_tabs_html + html[old_tabs_html.end():]

# 5. Replace modal links
html = html.replace('<a href="index.html" class="home-link">🏠 返回 26 单元总览</a>', '<a href="index.html" class="home-text-link" style="font-size:13px">目录</a>')

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Applied S T O R Y branding to Unit01.html template!")
