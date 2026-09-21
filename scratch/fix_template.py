# -*- coding: utf-8 -*-
import re
import os

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS
css_pattern = r'/\* -------------------------------------------------- \*/[\s\S]*?/\* ---------- 生词本 ---------- \*/'
# Let's find CSS block around .stickyhead
old_css_part = re.search(r'\.stickyhead\{[\s\S]*?\.label\{font-size:11px', html)

new_css = """.stickyhead{position:sticky;top:0;z-index:30;background:var(--paper);padding:12px 18px 10px;margin:0 -18px 10px;
  border-bottom:1px solid transparent;transition:padding .22s,border-color .22s,background .22s,box-shadow .22s;
  display:flex;align-items:center;justify-content:space-between;gap:12px}
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

/* 吸顶 MINI 模式：背景玻璃拟态，淡入呈现吸顶单元导航与 index 返回 */
.sticky-unit-nav{display:flex;align-items:center;gap:6px;opacity:0;visibility:hidden;max-width:0;overflow:hidden;
  transition:opacity .25s ease,max-width .25s ease,visibility .25s ease}
.stickyhead.mini{padding:8px 14px;background:rgba(244,235,224,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);
  border-bottom-color:var(--line);box-shadow:0 4px 16px rgba(43,38,34,.06)}
.stickyhead.mini .tab{padding:5px 8px;font-size:12.5px;border-radius:999px;flex-direction:row;gap:3px}
.stickyhead.mini .tab small{display:none}
.stickyhead.mini .sticky-unit-nav{opacity:1;visibility:visible;max-width:240px}

.sticky-home-btn{display:inline-flex;align-items:center;gap:4px;font-size:12px;color:var(--clay2);
  background:rgba(200,100,59,.1);border-radius:999px;padding:4px 9px;font-weight:600;text-decoration:none;transition:.15s}
.sticky-home-btn:hover{background:var(--clay);color:#fff}
.sticky-unit-selector{display:flex;align-items:center;gap:3px}
.subtn-icon{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:3px 8px;font-size:11px;color:var(--ink2);text-decoration:none;transition:.15s;font-weight:600;line-height:1.3}
.subtn-icon:hover{border-color:var(--clay);color:var(--clay2)}
.subtn-badge{border:1px solid rgba(200,100,59,.45);background:rgba(255,251,246,.95);border-radius:999px;padding:3px 10px;font-size:11.5px;color:var(--clay2);cursor:pointer;transition:.15s;font-weight:600}
.subtn-badge:hover{background:#fff;border-color:var(--clay);transform:translateY(-1px)}

/* 纯 Icon 视角排版切换与设置按钮 */
.layout-toggle{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:var(--card);flex:0 0 auto}
.lbtn{border:none;background:transparent;padding:5px 9px;font-size:13px;color:var(--ink2);cursor:pointer;transition:.15s;font-weight:600;font-family:var(--sans);display:inline-flex;align-items:center;justify-content:center}
.lbtn.on{background:var(--clay);color:#fff}
.lbtn+.lbtn{border-left:1px solid var(--line)}

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
body.layout-mobile .grid{grid-template-columns:1fr}
body.layout-mobile .pick{grid-template-columns:1fr}
body.layout-mobile .storycard{padding:24px 18px 18px;border-radius:16px}
body.layout-mobile .stitle{font-size:18.5px}
body.layout-mobile .en{font-size:16px;line-height:1.85}
body.layout-mobile .zh{font-size:13.5px;line-height:1.8}
body.layout-mobile .wcard{padding:13px 14px}

@media(max-width:640px){
  .home-text{display:none}
  .sticky-home-btn{padding:4px 7px}
  .subtn-icon{display:none}
}
@media(max-width:430px){
  .tab{padding:6px 1px;font-size:11px}
}

.label{font-size:11px;letter-spacing:.16em;color:var(--clay2);margin:26px 0 10px;font-weight:600}"""

if old_css_part:
    html = html[:old_css_part.start()] + new_css + html[old_css_part.end()-9:]

# 2. Update Sticky Head HTML
old_sticky_html = re.search(r'<div class="stickyhead">[\s\S]*?</div>\s*</div>\s*</div>', html)
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
      <div class="sticky-unit-nav" id="stickyUnitNav">
        <a class="sticky-home-btn" href="index.html" title="返回 26 单元总览">🏠 <span class="home-text">总览</span></a>
        <div class="sticky-unit-selector">
          <a class="subtn-icon" id="stickyPrevUnitNav" href="#" title="上一单元">◀</a>
          <button class="subtn-badge" id="stickyUnitModalBtn" title="点击展开全量 26 单元选关矩阵"><span id="stickyBadgeText">Unit 1</span> ▾</button>
          <a class="subtn-icon" id="stickyNextUnitNav" href="#" title="下一单元">▶</a>
        </div>
      </div>

      <div class="layout-toggle" id="layoutToggle" title="切换视角排版">
        <button class="lbtn on" data-layout="desktop" title="💻 电脑视角">💻</button>
        <button class="lbtn" data-layout="mobile" title="📱 手机视角">📱</button>
      </div>

      <button class="opt-settings-btn" id="optSettingsBtn" title="页面设置：视角排版与语音朗读">⚙️</button>
    </div>
  </div>"""

if old_sticky_html:
    html = html[:old_sticky_html.start()] + new_sticky_html + html[old_sticky_html.end():]

# 3. Update syncAudio & JS null-checks
sync_audio_old = re.search(r'function syncAudio\(\)\{[\s\S]*?\}\n/\* 背模式朗读', html)
sync_audio_new = """function syncAudio(){
  var m = document.getElementById("modeseg"), r = document.getElementById("rateseg");
  if(m){
    Array.prototype.forEach.call(m.children, function(b){ b.classList.toggle("on", b.dataset.mode === TTS.mode); });
  }
  if(r){
    var rl = Array.prototype.slice.call(r.children), near = null, best = 9;
    rl.forEach(function(b){
      var d = Math.abs(parseFloat(b.dataset.rate) - TTS.rate);
      if(d < best){ best = d; near = b; }
    });
    if(near && best > 0.02){ TTS.rate = parseFloat(near.dataset.rate); saveTTS(); }
    rl.forEach(function(b){ b.classList.toggle("on", b === near); });
  }
  var vs = document.getElementById("voiceseg");
  if(vs){
    vs.innerHTML = VOICES.map(function(v){
      return '<button data-voice="' + v.id + '"' + (v.id === TTS.en ? ' class="on"' : "") + '>'
        + v.name + '<small>' + v.desc + '</small></button>';
    }).join("");
  }
  var amode = document.getElementById("amode");
  if(amode) amode.textContent = TTS.mode === "off" ? "关" : (TTS.mode === "auto" ? "自动" : "手动");
  var abtn = document.getElementById("audiobtn");
  if(abtn) abtn.classList.toggle("on", TTS.mode !== "off");
  var hint = document.getElementById("ttshint");
  if(hint){
    hint.classList.remove("err");
    hint.textContent = TTS.mode === "off" ? "静音中" : (TTS.mode === "auto" ? "背词 + 释义全自动" : "背词自动读，其余点按");
  }
}
/* 背模式朗读"""

if sync_audio_old:
    html = html[:sync_audio_old.start()] + sync_audio_new + html[sync_audio_old.end()-11:]

# 4. Remove initMoreTabs and update bottom script initialization
html = re.sub(r'function initMoreTabs\(\)\{[\s\S]*?\}\n', '', html)
html = html.replace('initMoreTabs();\n', '')

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Template Unit01.html successfully updated.")
