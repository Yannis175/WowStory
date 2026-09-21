# -*- coding: utf-8 -*-
import re

TEMPLATE_PATH = r"d:\xinyi\codespace\WowStory\单词故事本\Unit01.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

old_block = """document.getElementById("audiobar").addEventListener("click", function(e){
  var b = e.target.closest("button"); if(!b) return;
  var pop = document.getElementById("apop");
  if(b.id === "audiobtn"){
    pop.classList.toggle("on");
    return;
  }
  if(b.id === "stopbtn"){ stopSay(); toast("已停止"); return; }
  if(b.id === "preven"){ previewVoice(TTS.en); return; }
  if(b.dataset.voice){
    TTS.en = b.dataset.voice; saveTTS(); syncAudio();
    toast("音色已换成 " + (VOICES.filter(function(v){ return v.id === TTS.en; })[0] || {}).name);
    previewVoice(TTS.en);
    return;
  }
  if(b.dataset.mode){
    TTS.mode = b.dataset.mode; saveTTS(); syncAudio();
    stopSay(); SAY.last = "";
    var ch = document.getElementById("cardhint");
    if(ch) ch.textContent = cardHintText();
    autoDrill();
    toast(TTS.mode === "off" ? "朗读已关闭" : TTS.mode === "auto" ? "背词与释义全自动" : "背词自动读，其余点 🔊 才发声");
  } else if(b.dataset.rate){
    TTS.rate = parseFloat(b.dataset.rate); saveTTS(); syncAudio();
    toast("语速 " + (TTS.rate < 0.8 ? "慢速跟读" : TTS.rate > 1 ? "快速过词" : "正常"));
  }
});
document.addEventListener("click", function(e){
  var pop = document.getElementById("apop");
  if(!pop.classList.contains("on")) return;
  if(pop.contains(e.target) || document.getElementById("audiobtn").contains(e.target)) return;
  pop.classList.remove("on");
});"""

new_block = """var abar = document.getElementById("audiobar");
if(abar){
  abar.addEventListener("click", function(e){
    var b = e.target.closest("button"); if(!b) return;
    var pop = document.getElementById("apop");
    if(b.id === "audiobtn"){
      if(pop) pop.classList.toggle("on");
      return;
    }
    if(b.id === "stopbtn"){ stopSay(); toast("已停止"); return; }
    if(b.id === "preven"){ previewVoice(TTS.en); return; }
    if(b.dataset.voice){
      TTS.en = b.dataset.voice; saveTTS(); syncAudio();
      toast("音色已换成 " + (VOICES.filter(function(v){ return v.id === TTS.en; })[0] || {}).name);
      previewVoice(TTS.en);
      return;
    }
    if(b.dataset.mode){
      TTS.mode = b.dataset.mode; saveTTS(); syncAudio();
      stopSay(); SAY.last = "";
      var ch = document.getElementById("cardhint");
      if(ch) ch.textContent = cardHintText();
      autoDrill();
      toast(TTS.mode === "off" ? "朗读已关闭" : TTS.mode === "auto" ? "背词与释义全自动" : "背词自动读，其余点 🔊 才发声");
    } else if(b.dataset.rate){
      TTS.rate = parseFloat(b.dataset.rate); saveTTS(); syncAudio();
      toast("语速 " + (TTS.rate < 0.8 ? "慢速跟读" : TTS.rate > 1 ? "快速过词" : "正常"));
    }
  });
}
document.addEventListener("click", function(e){
  var pop = document.getElementById("apop");
  if(!pop || !pop.classList.contains("on")) return;
  var abtn = document.getElementById("audiobtn");
  if(pop.contains(e.target) || (abtn && abtn.contains(e.target))) return;
  pop.classList.remove("on");
});"""

if old_block in html:
    html = html.replace(old_block, new_block)
    with open(TEMPLATE_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    print("Successfully patched document click listener!")
else:
    print("Block not found!")
