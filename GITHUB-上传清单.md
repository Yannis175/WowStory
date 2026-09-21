# GitHub 上传清单 · WowStory 单词故事本

> 结论先行：**当前工作区不能直接 `git add .`**。里面混了三类东西 —— 可公开的原创代码与内容、必须处理掉的本机痕迹、以及**明确不能公开的版权材料**。
> 本文件只给决策。你的工作区里**没有建立过 git 仓库**，也没有提交或推送任何东西。

---

## 一、总览：工作区现状

| 项 | 数值 |
|---|---|
| 总体积 / 文件数 | **684.8 MB / 32,276 个文件** |
| 其中音频 | **618.0 MB / 31,869 个 mp3** |
| 其中扫描件 PDF | **50.3 MB / 5 个** |
| **剥离音频与素材后的「可发布核心」** | **8.58 MB / 150 个文件**（已实测，见第七节） |

一句话：**8.58 MB 是精华，剩下 676 MB 都是不该进仓库的东西。**

---

## 二、三档分类

### ✅ 第一档：可以直接公开（原创代码 + 原创内容）

| 路径 | 体积 | 说明 |
|---|---|---|
| `单词故事本/Unit01.html` ~ `Unit26.html` | 约 4.5 MB | 26 个单页应用，五 tab + 单元切换器。**唯一需要处理的是内嵌 `exam` 字段，见下** |
| `单词故事本/Unit01.json` ~ `Unit26.json` | 约 1.6 MB | 单元数据真源。同上，内含 `exam` 字段 |
| `单词故事本/index.html` | 7 KB | 总目录 + 跨单元搜索 |
| `单词故事本/Unit01.md` ~ `Unit26.md` | 约 1.6 MB | 派生文档 |
| `单词故事本/pt_data/_pt_uNN.json`（26 个） | 约 2.2 MB | 句级时间轴源文件（每单元一份，编译页面时内联进 HTML） |
| `单词故事本/_app.js` | 135 KB | 共享运行时（Unit01 内联脚本的镜像） |
| `单词故事本/serve.py` | 24 KB | 本地预览服务器 |
| `单词故事本/serve.cmd` | 1.7 KB | 双击入口。**本机绝对路径已清除，见第二档** |
| `单词故事本/vocab_audio.py` | 14 KB | 生词本音频合成 |
| `单词故事本/_sync_app.py` | 2 KB | 镜像同步检查 |
| `scripts/`（发布 25 个文件） | 0.39 MB | 整条生成 / 校验 / 音频 / 编译管线，**这是项目最有复用价值的部分** |
| `scripts/SKILL_AUDIO_AND_BUILD.md` | 6 KB | 管线说明（顺手修一下文末提到的段落命名漂移） |
| `skill/word-storybook-generation/`（5 个文件） | 0.07 MB | 生成 skill：`SKILL.md` + 校验器 + 增量自检 + md 派生 + 样例。已从 `.workbuddy/skills/` **复制**到明面路径（原件仍在原处，未删除） |

> `.workbuddy/` 整体必须被忽略，所以 skill 不能从那里发布。已经把它复制了一份到 `skill/word-storybook-generation/` —— 两份内容一致，后续要改请改明面这份，或改完再同步。

### ⚠️ 第二档：处理过才能公开

| 路径 | 问题 | 处理建议 |
|---|---|---|
| `单词故事本/serve.cmd` | 原本内含**写死的本机绝对路径**（`C:\Users\<用户名>\...`），会泄漏本机用户名与目录结构 | ✅ **已处理**：两处本机路径已换成通用兜底（`%LOCALAPPDATA%\Programs\Python\Python3*`、`%ProgramFiles%\Python3*`、Windows Store 版 `python.exe`），文件仍保持纯 ASCII。已确认本机 `where py` / `where python` 都能命中，改动不影响你双击使用 |
| `单词故事本/UnitNN.json`、`UnitNN.html`、`_units_manifest.js`、`pt_data/_pt_uNN.json` | 内嵌 `exam`（「常考含义」）字段是**从《红宝书》原文照抄**的义项；`exam` 是版权材料，其余字段（`w`/`ipa`/`zh`/`c`/`syn`/`fam`/`dif`/`pat`）都是原创或公共信息 | 二选一：① 公开仓库里**清空 `exam`** 只留原创字段 ② 仓库设为**私有**，`exam` 保留 |
| `_words_alpha.txt` | 4 MB 英文词表，不是自己产的 | 已默认排除。若确认来自 `dwyl/english-words`（Unlicense，公共领域），可从 `.gitignore` 移除该行，但**必须在 README 致谢里标注** |
| 根目录 5 个脚本（`extract_words.py` / `auto_extract_all.py` / `analyze_quality.py` / `apply_confirmed_fixes.py` / `quality_check.py`） | 本身是纯代码，不含书的内容，可以公开 | 只是散在根目录不太整洁，建议挪进 `scripts/`（纯整理，不影响发布） |

### ⛔ 第三档：不能公开（版权 / 隐私 / 无价值）

| 路径 | 体积 | 为什么不能发 |
|---|---|---|
| `原始单词本/*.pdf`（5 个） | **50.3 MB** | 《红宝书》扫描件，**商业出版物原件**。公开发布 = 直接侵权，DMCA 高发区，**必须排除** |
| `红宝书必考词_全量汇总.csv`、`..._清洗版.csv` | 0.4 MB | 从上述扫描件 OCR 出来的**成书词表 + 中文释义 + 常考含义**，逐行都是书的内容（原文里连 OCR 乱码都在，如「刀乁旨；荚讠吾」）。属衍生作品，**必须排除** |
| `清洗记录.txt` | 8 KB | 逐条记录了书里的词与释义，等于一份缩小版词表 |
| `quality_audit_u01_u20.txt` | 61 KB | 同上，含大量书内释义原文 |
| `_archive/`（164 文件，含 `crop_images/` 10 张 PNG） | 3.1 MB | 里面是**书页截图**（`doc3_p3.png` 等）+ 中间备份 + 日志，全是版权材料与本机残留 |
| `.workbuddy/` 全部 | 0.2 MB | 本机 AI 助手的记忆、日志、自动化记录、质量报告。含**个人工作过程与本机路径**，且无对外价值 |
| `.vcache/`（23 文件） | <0.1 MB | 工具任务缓存（`job.json` / `result.json`），本机运行时产物 |
| `_probe/` | 0.1 MB | 本次盘点用的临时探针与报告，内含本机绝对路径 |
| `__pycache__/`、所有 `*.pyc` | <0.1 MB | 编译缓存 |
| `单词故事本/audio/` | **618 MB** | 体积问题，且另有授权问题，见下节 |

---

## 三、两个需要你拍板的点

### 1. 音频（618 MB）——建议不进仓库

- **体积**：GitHub 单文件上限 100 MB（这里最大才 0.3 MB，没触线），但仓库**推荐控制在 1 GB 以内**，且 3 万个二进制文件会让 `clone` 极慢。一次性 `push` 600 MB 很可能中途超时。
- **授权**：音频由 `edge-tts`（微软 Edge「大声朗读」同款神经网络语音）离线合成。把 TTS 输出**公开再分发**在多数司法辖区属灰色地带 —— 自用没问题，公开分发请自行判断。
- **三条路**：
  - **A（推荐）** 仓库只放生成脚本，音频由使用者自己跑 `scripts/gen_all_audio.py 1 26` 生成；README 写明耗时与前置条件。
  - **B** 用 **Git LFS** 管理 `audio/`（配额与流量要花钱）。
  - **C** 音频打包放 **GitHub Releases** 或网盘，README 给下载链接。

### 2. 仓库可见性——决定 `exam` 去留

- **公开仓库**：必须清掉 `exam`（及 CSV/PDF），只发原创部分。项目作为「用故事串记考研词汇的方法 + 可复用的生成管线」是站得住的。
- **私有仓库**：`exam` 可保留，只需排除 PDF / CSV / `_archive` / `.workbuddy` 等。**如果你是给自己存档，这条最省事。**

---

## 四、建议的上传形态

```
wowstory/                          # 8.58 MB / 150 个文件
├─ README.md                       # 对外门面
├─ LICENSE                         # 代码 MIT（内容另注）
├─ .gitignore                      # 排除规则（见下）
├─ 单词故事本/
│  ├─ Unit01.html ~ Unit26.html
│  ├─ Unit01.json ~ Unit26.json    # 公开版：exam 置空
│  ├─ Unit01.md  ~ Unit26.md
│  ├─ pt_data/_pt_u01.json ~ _pt_u26.json
│  ├─ index.html
│  ├─ _units_manifest.js
│  ├─ _app.js
│  ├─ serve.py / serve.cmd
│  ├─ vocab_audio.py
│  └─ _sync_app.py
├─ scripts/                        # 生成 / 校验 / 音频 / 编译管线
└─ skill/
   └─ word-storybook-generation/   # 从 .workbuddy/skills 复制出来的副本
```

**不要提交**：`audio/`、`原始单词本/`、`*.csv`、`清洗记录.txt`、`quality_*.txt`、`_archive/`、`.workbuddy/`、`.vcache/`、`_probe/`、`__pycache__/`、`_words_alpha.txt`（除非确认来源）。

---

## 五、执行参考（按需自取，我没有执行）

```bash
cd D:/xinyi/codespace/WowStory
git init
# 先落 .gitignore，再 add —— 顺序反了就会把不该提的东西写进历史
git add .
git status          # ← 关键一步：确认列表里没有 pdf / csv / audio / .workbuddy
git commit -m "feat: 单词故事本 · 26 单元全量故事串记"
git branch -M main
git remote add origin git@github.com:<你的账号>/<仓库名>.git
git push -u origin main
```

**提交前必查三件事**

1. `git status` 的输出里**没有** `.pdf` / `.csv` / `.mp3` / `.workbuddy` / `_archive`
2. 第一次 `push` 前跑 `du -sh .git`，超过 100 MB 说明有东西漏进去了（大概率是音频）
3. 用 `git log --stat` 复查首个提交的文件清单

> 万一手滑提交了不该提的（尤其是 PDF），**改历史也未必干净** —— 公开仓库一旦被 fork 或缓存就无法回收。这种情况直接删仓库重建，比 `filter-repo` 省心。

---

## 六、`.gitignore` 草案

已写入工作区 `.gitignore`，可直接用。核心是「先全排除，再白名单」还是「黑名单列举」—— 这里用**黑名单 + 明确排除**，因为你要发的是 `单词故事本/` 下的大部分内容，白名单反而更绕。

---

## 七、已实测：`.gitignore` 到底拦住了什么

在系统临时目录建了一个空仓库、只放这份 `.gitignore`，把工作区 **32,276 个真实相对路径**喂给 `git check-ignore` 做离线推演（**没有在工作区建 `.git`，没有提交任何东西**）。

**结果：拦截 32,126 个，放行 150 个。**

| 生效的规则 | 命中文件数 |
|---|---|
| `单词故事本/audio/` | 31,869 |
| `_archive/` | 164 |
| `_probe/` | 36 |
| `.vcache/` | 23 |
| `.workbuddy/` | 15 |
| `__pycache__/` | 9 |
| `原始单词本/` | 5 |
| `红宝书必考词_全量汇总.csv` / `_清洗版.csv` | 2 |
| `清洗记录.txt` / `quality_audit_*.txt` / `_words_alpha.txt` | 3 |

**放行的 150 个文件**（这就是将来 `git add .` 会进去的全部内容）

- `单词故事本/`：26 组 `UnitNN.html` + `UnitNN.json` + `UnitNN.md`（78）、`pt_data/` 26 个、`index.html`、`_units_manifest.js`、`_app.js`、`serve.py`、`serve.cmd`、`vocab_audio.py`、`_sync_app.py` → 共 111
- `scripts/`：25 个
- `skill/word-storybook-generation/`：5 个
- 根目录：`README.md`、`LICENSE`、`.gitignore`、`GITHUB-上传清单.md`、5 个 py 脚本 → 9

**逐个抽查确认（全部符合预期）**

| 路径 | 结果 |
|---|---|
| `原始单词本/必考词1-5.pdf` | 已挡住 ✓ |
| `红宝书必考词_全量汇总_清洗版.csv` | 已挡住 ✓ |
| `清洗记录.txt` / `quality_audit_u01_u20.txt` | 已挡住 ✓ |
| `单词故事本/audio/aria/u01_ps1-0.mp3`（及 zh 中文音） | 已挡住 ✓ |
| `.workbuddy/memory/MEMORY.md` | 已挡住 ✓ |
| `_archive/crop_images/doc3_p3.png`（书页截图） | 已挡住 ✓ |
| `_words_alpha.txt` / `__pycache__/*.pyc` / `.vcache/jobs/*` | 已挡住 ✓ |
| `README.md` / `LICENSE` / `单词故事本/Unit01.html` / `Unit01.json` / `index.html` / `_units_manifest.js` / `serve.py` / `scripts/gen_unit_audio.py` / `skill/**` | 保留 ✓ |

> 推演用的是**路径**而不是文件内容，所以结论对「将来新增的音频文件」同样成立，不需要每加一个文件就重测一遍。
> 放行的这 150 个文件合计 **8.58 MB**，正常网速下几秒内就能推完 —— 唯一没法替你验证的是实际 `push` 时的网络状况。
