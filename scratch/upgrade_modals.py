# -*- coding: utf-8 -*-
import re

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace modal & audio CSS
old_modal_css_search = re.search(r'\.umodal\{[\s\S]*?\.stickyhead\{', html)

new_modal_css = """.umodal{position:fixed;inset:0;z-index:90;background:rgba(43,38,34,.48);
  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);
  display:flex;align-items:center;justify-content:center;padding:20px;
  opacity:0;pointer-events:none;transition:opacity .22s ease}
.umodal.on{opacity:1;pointer-events:auto}
.umodal-card{background:#FFFDF9;border-radius:24px;padding:26px 28px;max-width:800px;width:100%;max-height:85vh;overflow:auto;
  border:1px solid rgba(200,100,59,.2);box-shadow:0 24px 60px -12px rgba(43,38,34,.28),0 0 0 1px rgba(255,255,255,.8) inset;
  transform:scale(.94) translateY(12px);transition:transform .24s cubic-bezier(.16,1,.3,1)}
.umodal.on .umodal-card{transform:scale(1) translateY(0)}

.umodal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding-bottom:14px;border-bottom:1px dashed rgba(43,38,34,.12)}
.umodal-head h3{margin:0;font-family:var(--serif);font-size:20px;font-weight:700;color:var(--clay2);display:flex;align-items:center;gap:8px}

.modal-close-btn{width:32px;height:32px;border-radius:50%;background:rgba(43,38,34,.06);border:1px solid rgba(43,38,34,.1);
  display:inline-flex;align-items:center;justify-content:center;color:var(--ink2);font-size:14px;cursor:pointer;transition:all .2s ease}
.modal-close-btn:hover{background:rgba(200,100,59,.12);color:var(--clay2);border-color:rgba(200,100,59,.3);transform:rotate(90deg)}

.ugrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:12px}
.uitem{background:#FFFDF9;border:1px solid rgba(43,38,34,.1);border-radius:14px;padding:14px 16px;display:block;text-align:left;
  transition:all .2s cubic-bezier(.16,1,.3,1);text-decoration:none}
.uitem:hover{border-color:var(--clay);background:#fff;transform:translateY(-2px);box-shadow:0 8px 20px rgba(200,100,59,.12)}
.uitem.on{border:2px solid var(--clay);background:rgba(200,100,59,.06);box-shadow:0 4px 12px rgba(200,100,59,.15)}
.uitem b{display:block;font-family:var(--serif);font-size:16.5px;color:var(--clay2)}
.uitem span{display:block;font-size:11px;color:var(--ink3);margin-top:4px}

.opt-group{background:rgba(255,251,246,.7);border:1px solid rgba(43,38,34,.08);border-radius:16px;padding:16px}
.opt-label{display:block;font-size:12px;font-weight:700;color:var(--clay2);letter-spacing:.05em;margin-bottom:12px}

.layout-toggle{display:flex;background:rgba(43,38,34,.06);border-radius:12px;padding:4px;gap:4px;border:1px solid rgba(43,38,34,.08);width:100%}
.lbtn{flex:1;border:none;background:transparent;padding:9px 14px;font-size:13px;color:var(--ink2);cursor:pointer;
  transition:all .2s cubic-bezier(.16,1,.3,1);font-weight:500;font-family:var(--sans);display:inline-flex;align-items:center;justify-content:center;gap:6px;border-radius:8px}
.lbtn.on{background:#ffffff;color:var(--clay2);font-weight:700;box-shadow:0 3px 10px rgba(43,38,34,.1)}

.audiobar{display:flex;flex-direction:column;gap:12px;width:100%}
.arow{display:flex;align-items:center;gap:12px}
.alabel{flex:0 0 42px;font-size:12.5px;font-weight:600;color:var(--ink2)}
.aseg{display:flex;background:rgba(43,38,34,.06);border-radius:10px;padding:3px;gap:3px;border:none}
.aseg button{border:none;background:transparent;padding:7px 10px;font-size:12.5px;color:var(--ink2);font-weight:500;
  border-radius:7px;transition:all .18s ease;cursor:pointer;text-align:center}
.aseg button:hover{color:var(--clay2)}
.aseg button.on{background:#ffffff;color:var(--clay2);font-weight:700;box-shadow:0 2px 6px rgba(43,38,34,.12)}
.aseg.wide{flex:1;min-width:0}
.aseg.wide button{flex:1;padding:6px 4px;line-height:1.25}
.aseg.wide button small{display:block;font-size:9.8px;opacity:.65;font-weight:400;margin-top:1px}
.aseg.wide button.on small{opacity:.9}

#preven{border:1px solid rgba(200,100,59,.35);background:rgba(200,100,59,.08);color:var(--clay2);border-radius:999px;
  padding:6px 14px;font-size:12px;font-weight:600;cursor:pointer;transition:all .15s;flex:0 0 auto}
#preven:hover{background:var(--clay);color:#fff;border-color:var(--clay)}

.stickyhead{"""

if old_modal_css_search:
    html = html[:old_modal_css_search.start()] + new_modal_css + html[old_modal_css_search.end()-12:]

# 2. Update Modals HTML Markup
modals_html_search = re.search(r'<div class="umodal" id="unitModal">[\s\S]*?</div>\s*</div>\s*</div>', html)

new_modals_html = """<div class="umodal" id="unitModal">
  <div class="umodal-card">
    <div class="umodal-head">
      <div style="display:flex;align-items:center;gap:12px">
        <h3 style="margin:0">切换单元 (Unit 01 ~ Unit 26)</h3>
        <a href="index.html" class="home-link">🏠 返回 26 单元总览</a>
      </div>
      <button class="modal-close-btn" id="closeUnitModal" title="关闭">✕</button>
    </div>
    <div class="ugrid" id="unitModalGrid"></div>
  </div>
</div>

<div class="umodal" id="settingsModal">
  <div class="umodal-card" style="max-width:460px">
    <div class="umodal-head">
      <h3>⚙️ 页面与语音控制设置</h3>
      <button class="modal-close-btn" id="closeSettingsModal" title="关闭">✕</button>
    </div>
    
    <div style="display:grid;gap:16px">
      <div class="opt-group">
        <label class="opt-label">展示视角排版</label>
        <div class="layout-toggle" id="layoutToggle">
          <button class="lbtn on" data-layout="desktop">💻 电脑宽屏视角</button>
          <button class="lbtn" data-layout="mobile">📱 手机单列视角</button>
        </div>
      </div>

      <div class="opt-group">
        <label class="opt-label">语音朗读控制</label>
        <div class="audiobar" id="audiobar">
          <div class="arow"><span class="alabel">模式</span>
            <div class="aseg wide" id="modeseg">
              <button data-mode="off">关<small>不朗读</small></button>
              <button data-mode="manual">手动<small>背词自动</small></button>
              <button data-mode="auto">自动<small>连释义读</small></button>
            </div>
          </div>
          <div class="arow"><span class="alabel">语速</span>
            <div class="aseg" id="rateseg">
              <button data-rate="0.75">慢速</button>
              <button data-rate="1">正常</button>
              <button data-rate="1.15">快速</button>
            </div>
          </div>
          <div class="arow"><span class="alabel">英音</span>
            <div class="aseg wide" id="voiceseg"></div>
            <button id="preven">试听</button>
          </div>
        </div>
      </div>

      <div style="border-top:1px dashed rgba(43,38,34,.14);padding-top:14px;display:flex;justify-content:space-between;align-items:center">
        <span style="font-size:12px;color:var(--ink3);font-weight:500">快捷跳转</span>
        <a href="index.html" class="home-link">🏠 返回 26 单元总览</a>
      </div>
    </div>
  </div>
</div>"""

if modals_html_search:
    html = html[:modals_html_search.start()] + new_modals_html + html[modals_html_search.end():]

with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("Modal styling and markup successfully updated!")
