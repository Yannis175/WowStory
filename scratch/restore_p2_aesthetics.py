# -*- coding: utf-8 -*-
import re

# 1. Restore index.html aesthetics
INDEX_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\index.html"
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_new = """<title>单词故事本 · 全 26 单元故事合集</title>
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#C8643B">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="单词故事本">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23F4EBE0'/%3E%3Ccircle cx='16' cy='16' r='9' fill='%23C8643B'/%3E%3Ccircle cx='20.5' cy='12.5' r='7.5' fill='%23F4EBE0'/%3E%3C/svg%3E">
<style>
*{box-sizing:border-box}
:root{
  --paper:#F4EBE0;--card:#FFFBF6;--ink:#2B2622;--ink2:#6B6156;--ink3:#9A8E80;
  --clay:#C8643B;--clay2:#A9542F;--moon:#E8B84B;--line:rgba(43,38,34,.13);
  --serif:"Source Han Serif SC","Noto Serif SC","Songti SC",Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
}
html,body{margin:0;padding:0;background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(rgba(43,38,34,.04) 1px,transparent 1px);background-size:22px 22px}
a{text-decoration:none !important;color:inherit}
.wrap{max-width:900px;margin:0 auto;padding:32px 20px 100px}
.header{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:28px}
.brand h1{font-family:var(--serif);font-size:32px;font-weight:700;margin:0;letter-spacing:.02em;color:var(--ink)}
.brand p{margin:8px 0 0;font-size:14px;color:var(--ink2);line-height:1.6}
.badge-total{font-size:13px;color:var(--clay2);border:1px dashed rgba(200,100,59,.45);border-radius:999px;padding:8px 18px;background:rgba(255,251,246,.85);font-weight:600}

.search-box{position:relative;margin-bottom:32px}
.search-input{width:100%;border:1.5px solid var(--line);background:var(--card);border-radius:999px;padding:14px 24px;font-size:15px;color:var(--ink);outline:none;transition:.2s;box-shadow:0 4px 16px rgba(43,38,34,.04)}
.search-input:focus{border-color:var(--clay);box-shadow:0 6px 20px rgba(200,100,59,.15)}
.search-results{margin-top:12px;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;max-height:360px;overflow:auto;padding-right:4px}
.s-item{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;transition:.15s;display:block}
.s-item:hover{border-color:var(--clay);transform:translateY(-1px)}
.s-word{font-family:var(--serif);font-weight:700;color:var(--clay2);font-size:15px;display:flex;justify-content:space-between;align-items:center}
.s-unit{font-size:10.5px;background:rgba(232,184,75,.4);color:#6B4A20;border-radius:4px;padding:1px 6px;font-family:var(--sans);font-weight:normal}
.s-zh{font-size:12px;color:var(--ink2);margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.unit-card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 22px;transition:.2s;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.unit-card:hover{border-color:rgba(200,100,59,.5);transform:translateY(-2px);box-shadow:0 8px 24px rgba(43,38,34,.08)}
.u-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px}
.u-num{font-family:var(--serif);font-size:24px;font-weight:700;color:var(--clay2)}
.u-stats{font-size:12px;color:var(--ink3)}
.u-themes{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.u-theme{font-size:11.5px;background:rgba(43,38,34,.05);color:var(--ink2);border-radius:6px;padding:3px 9px}
.u-btn{display:block;text-align:center;background:var(--clay);color:#fff;border-radius:999px;padding:10px 0;font-size:13.5px;font-weight:600;transition:.15s}
.unit-card:hover .u-btn{background:var(--clay2)}

.footer{text-align:center;margin-top:60px;font-size:12.5px;color:var(--ink3);font-family:var(--serif)}
</style>
</head>
<body>
<div class="wrap">
  <div class="header">
    <div class="brand">
      <h1>单词故事本</h1>
      <p>把红宝书必考词，穿成一篇篇能读下去的小故事</p>
    </div>
    <div class="badge-total" id="totalBadge">26 个单元 · 121 篇故事 · 1,837 考点词</div>
  </div>

  <div class="search-box">
    <input type="text" class="search-input" id="searchInput" placeholder="🔍 搜索任意考研单词 / 中文释义（覆盖全量 1,837 词）...">
    <div class="search-results" id="searchResults" style="display:none"></div>
  </div>

  <div class="grid" id="unitGrid"></div>

  <div class="footer">单词故事本 · 考研英语真题句式与故事记忆系统</div>"""

idx_search = re.search(r'<title>[\s\S]*?<div class="footer">[\s\S]*?</div>', idx_content)
if idx_search:
    idx_content = idx_content[:idx_search.start()] + idx_new + idx_content[idx_search.end():]

with open(INDEX_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(idx_content)
print("Restored index.html P2 aesthetics!")

# 2. Restore Unit01.html template aesthetics
TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace title
html = html.replace("<title>S T O R Y · Unit 1</title>", "<title>单词故事本 · Unit 1</title>")

# Update CSS for home-link and brand
css_p2 = """a{text-decoration:none !important;color:inherit}
.home-link{display:inline-flex;align-items:center;gap:4px;font-size:12px;color:var(--clay2);background:rgba(200,100,59,.1);border-radius:999px;padding:4px 10px;font-weight:600;transition:.15s;text-decoration:none !important}
.home-link:hover{background:var(--clay);color:#fff}
.brand h1{font-family:var(--serif);font-size:25px;font-weight:700;margin:0;letter-spacing:.02em;color:var(--ink)}
.brand p{margin:6px 0 0;font-size:12.5px;color:var(--ink2)}

.tab{flex:1;border:1px solid var(--line);background:rgba(255,251,246,.85);border-radius:999px;
  padding:8px 4px;font-size:13.5px;font-family:var(--sans);font-weight:500;color:var(--ink2);transition:.16s ease;text-align:center;
  display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;white-space:nowrap}
.tab:hover{border-color:var(--clay);color:var(--clay2);background:#fff}
.tab.on{background:var(--clay);color:#fff;border-color:var(--clay);box-shadow:0 2px 8px rgba(200,100,59,.22)}
.tab small{display:block;font-size:10px;font-family:var(--sans);opacity:.75;margin-top:1px;font-weight:400}
.tab.on small{opacity:.9}"""

html = re.sub(r'\.home-text-link[\s\S]*?\.tab\.on small\{opacity:\.95\}', css_p2, html)

# Replace Brand Area HTML
old_brand = re.search(r'<div class="brand">[\s\S]*?</div>\s*<div class="unit-nav">', html)
new_brand = """<div class="brand">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
        <a href="index.html" class="home-link" title="返回全量 26 单元合集首页">🏠 单元总览</a>
        <span style="font-size:11px;color:var(--ink3)">/</span>
        <span style="font-size:12px;color:var(--clay2);font-weight:600" id="headerUnitTag">Unit 1</span>
      </div>
      <h1>单词故事本</h1>
      <p>把红宝书必考词，穿成一篇篇能读下去的小故事</p>
    </div>"""

if old_brand:
    html = html[:old_brand.start()] + new_brand + html[old_brand.end()-22:]

# Replace 5 Tabs HTML to P2 emoji tabs
old_tabs = re.search(r'<div class="tabs" id="tabs">[\s\S]*?</div>', html)
new_tabs = """<div class="tabs" id="tabs">
        <button class="tab" data-tab="read">📖 读<small>故事猜词</small></button>
        <button class="tab" data-tab="drill">🎴 背<small>遮词自测</small></button>
        <button class="tab" data-tab="write">✍️ 写<small>表达素材</small></button>
        <button class="tab" data-tab="index">🔍 查<small>全词速查</small></button>
        <button class="tab" data-tab="vocab">📓 本<small>我的生词</small></button>
      </div>"""

if old_tabs:
    html = html[:old_tabs.start()] + new_tabs + html[old_tabs.end():]

# Replace modal home links back to P2 capsule link
html = html.replace('<a href="index.html" class="home-text-link" style="font-size:13px">目录</a>', '<a href="index.html" class="home-link">🏠 返回 26 单元总览</a>')

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Restored Unit01.html template P2 aesthetics!")
