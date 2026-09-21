# -*- coding: utf-8 -*-
import re

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS
css_search = re.search(r'\.stickyhead\{[\s\S]*?\.label\{font-size:11px', html)

new_css = """.stickyhead{position:sticky;top:0;z-index:30;background:var(--paper);padding:12px 18px 10px;margin:0 -18px 10px;
  border-bottom:1px solid transparent;transition:padding .22s,border-color .22s,background .22s,box-shadow .22s;
  display:flex;align-items:center;justify-content:space-between;gap:10px}
.sticky-left{display:flex;align-items:center;gap:10px;flex:1 1 auto;min-width:0}
.tabs{display:flex;gap:5px;flex:1 1 auto;max-width:650px}
.tab{flex:1;border:1px solid var(--line);background:rgba(255,251,246,.85);border-radius:999px;
  padding:8px 4px;font-size:13px;color:var(--ink2);transition:.16s ease;text-align:center;
  display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;white-space:nowrap}
.tab:hover{border-color:var(--clay);color:var(--clay2);background:#fff}
.tab.on{background:var(--clay);color:#fff;border-color:var(--clay);box-shadow:0 2px 8px rgba(200,100,59,.22)}
.tab small{display:block;font-size:10px;opacity:.75;margin-top:1px;font-weight:400}
.tab.on small{opacity:.9}

.sticky-right{display:flex;align-items:center;gap:8px;flex:0 0 auto}

/* 吸顶 MINI 模式：背景玻璃拟态，精致双侧布局 */
.stickyhead.mini{padding:8px 14px;background:rgba(244,235,224,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);
  border-bottom-color:var(--line);box-shadow:0 4px 16px rgba(43,38,34,.06)}
.stickyhead.mini .tab{padding:5px 8px;font-size:12.5px;border-radius:999px;flex-direction:row;gap:3px}
.stickyhead.mini .tab small{display:none}

.subtn-badge{border:1px solid rgba(200,100,59,.45);background:rgba(255,251,246,.95);border-radius:999px;padding:5px 12px;font-size:12px;color:var(--clay2);cursor:pointer;transition:.15s;font-weight:600;font-family:var(--sans)}
.subtn-badge:hover{background:#fff;border-color:var(--clay);transform:translateY(-1px)}

.opt-settings-btn{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:5px 9px;font-size:13px;color:var(--ink2);transition:.15s;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
.opt-settings-btn:hover{border-color:var(--clay);color:var(--clay2);background:#fff}

.wrap{transition:max-width .3s ease,padding .3s ease}
.grid,.pick,.storycard,.wcard,.flip,.tab{transition:all .25s ease}

/* 📱 手机仿真排版模式 (layout-mobile) */
body.layout-mobile .wrap{max-width:480px;padding-left:12px;padding-right:12px}
body.layout-mobile .stickyhead{padding:10px 12px 6px;margin:0 -12px 8px}
body.layout-mobile .stickyhead.mini{padding:6px 10px}
body.layout-mobile .tabs{gap:3px}
body.layout-mobile .tab{padding:6px 2px;font-size:11.8px}
body.layout-mobile .tab small{display:none}
body.layout-mobile .stickyhead.mini .tab{padding:4px 6px;font-size:11.5px}
body.layout-mobile .subtn-badge{padding:4px 8px;font-size:11px}

@media(max-width:640px){
  .home-text{display:none}
}
@media(max-width:430px){
  .tab{padding:6px 1px;font-size:11px}
  .subtn-badge{padding:4px 7px;font-size:11px}
}

.label{font-size:11px;letter-spacing:.16em;color:var(--clay2);margin:26px 0 10px;font-weight:600}"""

if css_search:
    html = html[:css_search.start()] + new_css + html[css_search.end()-9:]

# 2. Update Sticky Head HTML block
sticky_html_search = re.search(r'<div class="stickyhead">[\s\S]*?<div id="app"></div>', html)

new_sticky_html = """<div class="stickyhead">
    <div class="sticky-left">
      <div class="tabs" id="tabs">
        <button class="tab" data-tab="read">📖 读<small>故事猜词</small></button>
        <button class="tab" data-tab="drill">🎴 背<small>遮词自测</small></button>
        <button class="tab" data-tab="write">✍️ 写<small>表达素材</small></button>
        <button class="tab" data-tab="index">🔍 查<small>全词速查</small></button>
        <button class="tab" data-tab="vocab">📓 本<small>我的生词</small></button>
      </div>
    </div>

    <div class="sticky-right">
      <button class="subtn-badge" id="stickyUnitModalBtn" title="点击展开 26 单元选关矩阵"><span id="stickyBadgeText">Unit 1</span> ▾</button>
      <button class="opt-settings-btn" id="optSettingsBtn" title="页面设置：视角排版与语音朗读">⚙️</button>
    </div>
  </div>

  <div id="app"></div>"""

if sticky_html_search:
    html = html[:sticky_html_search.start()] + new_sticky_html + html[sticky_html_search.end():]

# 3. Update Unit Modal Header to include Home Link
unit_modal_search = re.search(r'<div class="umodal-head">\s*<h3>切换单元 \(Unit 01 ~ Unit 26\)</h3>\s*<button class="btn quiet" id="closeUnitModal">✕ 关闭</button>\s*</div>', html)
if unit_modal_search:
    new_modal_head = """<div class="umodal-head">
      <div style="display:flex;align-items:center;gap:12px">
        <h3 style="margin:0">切换单元 (Unit 01 ~ Unit 26)</h3>
        <a href="index.html" class="home-link">🏠 返回 26 单元总览</a>
      </div>
      <button class="btn quiet" id="closeUnitModal">✕ 关闭</button>
    </div>"""
    html = html[:unit_modal_search.start()] + new_modal_head + html[unit_modal_search.end():]

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Applied Option 1 to Unit01.html!")
