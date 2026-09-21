# Skill: 通用型 WowStory 音频合成与单页 HTML 编译工作流指南

> **Skill 定位**：本指南为**通用型自动化音频合成与 HTML 页面编译 Skill**，不依赖具体单元号。
> 只要通过前置流程/Skill 提取生成了符合标准 Schema 的 `Unit{N}.json`（无论 `N` 为 1、27、50 还是任意单元），本 Skill 均可通用执行**音源合成、句级时间轴（PT JSON）毫秒级对齐提取、防削音切词、以及独立 `Unit{N}.html` 单页应用自动编译**。

---

## 📌 一、 通用数据 Schema 规范 (Universal Data Schema)

输入的 `Unit{N}.json` 文件必须符合以下通用数据结构（存放于 `单词故事本/Unit{N}.json`，其中 `{N}` 可为任意补零数字如 `01`, `08`, `27`, `100`）：

```json
{
  "unit": 27,
  "stories": [
    {
      "id": "s1",
      "en": "English Story Title",
      "zh": "中文故事标题",
      "theme": "题材分类",
      "ps": [
        {
          "en": "Paragraph English text with [[target_word|base_form]] markups.",
          "zh": "段落中文译文。"
        }
      ]
    }
  ],
  "words": [
    {
      "w": "target_word",
      "ipa": "ˈtɑːɡɪt",
      "pos": "n.",
      "s": "s1",
      "zh": "故事义",
      "exam": "常考义",
      "c": ["collocation 1", "collocation 2"],
      "syn": ["synonym1", "synonym2"],
      "fam": ["word family 1"],
      "dif": "辨析说明",
      "pat": "Example sentence containing the target word.",
      "patZh": "例句中文翻译。"
    }
  ]
}
```

---

## 📌 二、 通用避坑原则与底层技术规范 (Universal Pitfalls & Principles)

### 1. 句首削音防吃词规范 (HTML5 Audio Seeking Lead-in Buffer)
- **底层原理**：现代浏览器及操作系统音频驱动在执行 `audio.currentTime = offset` 时，MP3 解码与硬件输出需要 150ms ~ 250ms 的解压缓冲与音量平滑淡入（Fade-in）。若直接定位到 TTS 事件返回的 0ms 点，句首短词（如 `A`, `The`, `In`, `It`, `When`）会被硬件淡入消音。
- **通用规范**：
  在任意前端单页面 JS 播放器 `speakSentence(k, j)` 中，必须应用**双向通用缓冲策略**：
  - **前置缓冲**：`from = j > 0 ? Math.max(0, (marks[j] || 0) - 0.25) : 0;` （向前移动 250ms 到上一句后的静音区，抵消 Seeking Fade-in 延迟）
  - **后置保护**：`to = (j + 1 < marks.length) ? (marks[j + 1] + 0.10) : undefined;` （向后延长 100ms，保护句尾浊辅音自然衰减）

### 2. 文本断句规则双端强一致 (Regex Split Consistency)
- **通用规范**：
  Python 音频提取脚本与 JavaScript 前端 DOM 渲染脚本的断句正则**必须 100% 保持一致**，且必须包含常用英文缩写保护（防止 `Dr.`, `Mr.`, `St.` 等导致句数错位）：
  - **Python / JS 统一正则**：
    `SENT = r"[^.!?]+[.!?]*\s*"`
    `ABBR = r"(^|[\s(])(Dr|Mr|Mrs|Ms|Prof|St|vs|etc|No|Jr|Sr)\."`

### 3. 音频命名空间通用隔离 (Namespace Isolation)
- **通用规范**：
  - 段落 MP3：统一采用 `u{N:02d}_p{story_id}-{para_idx}.mp3`（英文）与 `u{N:02d}_pz{story_id}-{para_idx}.mp3`（中文），实现任意单元无缝隔离。
  - 单词及短语 MP3：文件名通过 `safe(w)` 清洗非路径字符（`re.sub(r"[^A-Za-z0-9_-]", "_", w)`）。

### 4. 批量网络合成防卡死保护 (Network Concurrency Guard)
- **通用规范**：
  - 合成脚本并发数限制为 `asyncio.Semaphore(2)`。
  - 每一个 WebSocket 流请求加装 `asyncio.wait_for(..., timeout=25.0)` 超时自动重试机制。
  - 断点续传机制：判断音频文件存在且 `size > 800 bytes`，且对应 PT JSON 已有有效时间轴时，自动跳过网络请求。

### 5. 视觉跟读敏捷高亮 (Highlight Lead-in)
- **通用规范**：
  段落跟读 `follow()` 中设置 `t >= marks[j] - 0.15`，视觉高亮提前 150ms 响应发音。

---

## 🚀 三、 通用自动化命令行指令 (Universal CLI Operations)

针对任意单元 `{N}`（如 `N=27`），按顺序执行以下通用命令：

### 1. 任意指定单元音频合成与 PT 时间轴提取
```bash
# 通用命令格式：python scripts/gen_unit_audio.py <任意Unit编号>
python scripts/gen_unit_audio.py 27
```
*自动生成产物*：
- `单词故事本/audio/aria/u27_p1-0.mp3` 等 MP3 文件
- `单词故事本/_pt_u27.json` 时间轴数据

### 2. 多单元批量合成（可选）
```bash
# 通用命令格式：python scripts/gen_all_audio.py <起始Unit> <结束Unit>
python scripts/gen_all_audio.py 1 30
```

### 3. 校验 PT 时间轴匹配度
```bash
# 自动检验 target 目录下所有 PT 时间轴与 JSON 句数的对齐度（确保 Mismatches 为 0）
python scripts/check_pt.py
```

### 4. 通用单页 HTML 应用编译与打包
```bash
# 通用命令格式：python scripts/build_unit_html.py <任意Unit编号 | all>
python scripts/build_unit_html.py 27

# 同步 App 全局逻辑脚本
python 单词故事本/_sync_app.py
```
*自动生成产物*：
- 独立单页应用：`单词故事本/Unit27.html`

---

## 🛠️ 四、 前端通用核心代码组件 (Universal Frontend Snippet)

### 1. 智能缓冲单句朗读
```javascript
function speakSentence(k, j, btn){
  var st = DATA.stories[state.story];
  var marks = (PT[TTS.en] || {})[st.id + "-" + k] || [];
  if(j >= marks.length) return;
  var from = j > 0 ? Math.max(0, (marks[j] || 0) - 0.25) : 0;
  var to = (j + 1 < marks.length) ? (marks[j + 1] + 0.10) : undefined;
  playList([{ src: srcPara(st.id, k), from: from, to: to, sel: selOf(k, j) }], btn);
}
```

### 2. 敏捷高亮跟读
```javascript
function follow(key, my){
  var marks = (PT[TTS.en] || {})[key] || [];
  var k = +String(key).split("-")[1], cur = -1;
  (function tick(){
    if(my !== SAY.token) return;
    var a = SAY.audio;
    SAY.raf = requestAnimationFrame(tick);
    if(!a || a.paused) return;
    var t = a.currentTime, idx = 0;
    for(var j = 0; j < marks.length; j++){ if(t >= marks[j] - 0.15) idx = j; }
    if(idx === cur) return;
    cur = idx;
    var sel = selOf(k, idx);
    if(SAY.hl.indexOf(sel) >= 0) return;
    purgeHL();
    var n = document.querySelector(sel);
    if(!n) return;
    n.classList.add("say"); SAY.hl.push(sel);
  })();
}
```

---

*通用 Skill 维护规范 · Antigravity Agent Team*
