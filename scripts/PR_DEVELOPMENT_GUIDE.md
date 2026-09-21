# 《单词故事本》目录更新与 Skill 提交 PR 指南

为了确保后续新增单元、修改错别字或通过 Skill / LLM 自动生成内容后能够顺利提交标准的 Git Pull Request (PR)，本文档梳理了**真源数据、派生编译产物与音频目录**的更新关系。

---

## 📁 1. 项目核心目录更新图谱

```
.
├─ 单词故事本/
│  ├─ UnitNN.json              # ⭐ [唯一真源] 修改内容/增加新单元时唯一必须修改的数据
│  ├─ pt_data/_pt_uNN.json     # 🤖 [自动生成] 句级时间轴（由 gen_unit_audio.py 产出）
│  ├─ audio/                   # 🎙️ [自动生成/更新] 离线 mp3 音频（由 gen_unit_audio.py 产出）
│  ├─ UnitNN.html              # 🛠️ [编译产物] 由 build_unit_html.py 生成的 HTML
│  ├─ UnitNN.md                # 📄 [编译产物] 由 build_md.py 派生的 Markdown 文档
│  ├─ _units_manifest.js       # 🔍 [编译产物] 由 build_units_bundle.py 产出的全集目录与全词搜索索引
│  ├─ _app.js                  # 🔄 [同步产物] 共享运行时镜像（通过 _sync_app.py 校验）
│  └─ sw.js                    # 📱 [离线配置] 新增单元时在预缓存清单 (PRECACHE_ASSETS) 中补上路径
│
└─ scripts/                    # ⚙️ 自动化流水线脚本
   ├─ validate_unit.py         # 🔍 [校验器] 确定性检查器，必须 ERROR 0 才能提交
   ├─ gen_unit_audio.py        # 🎙️ [音频脚本] 生成 mp3 + pt_data/_pt_uNN.json
   ├─ build_unit_html.py       # 🛠️ [HTML编译] JSON + 时间轴 ➔ HTML
   ├─ build_units_bundle.py    # 🔍 [索引编译] 生成 _units_manifest.js
   └─ run_unit_pipeline.py     # 🚀 [全流程流水线] 一键完成校验、音频、编译与同步
```

---

## 🔄 2. 更新或新增内容时的标准工作流

当你（或通过 AI Skill）修改/新增内容或调整 UI 交互时，流水线操作步骤如下：

### 场景 A：修改/新增单元内容（数据真源流程）
1. **编辑唯一真源**：修改或新建 `单词故事本/UnitNN.json`。
2. **确定性校验**：`python scripts/validate_unit.py <Unit编号>` (必须 ERROR 0)。
3. **生成音频与时间轴**：`python scripts/gen_unit_audio.py <Unit编号>`。
4. **全量编译产物**：
   ```bash
   python scripts/build_unit_html.py <Unit编号>   # 或 python scripts/build_unit_html.py all
   python scripts/build_md.py <Unit编号>
   python scripts/build_units_bundle.py
   python 单词故事本/_sync_app.py
   ```

### 场景 B：调整前端 UI / 交互与样式（模板编译流程）
1. **编辑主模板**：修改 `单词故事本/Unit01.html` 或 `单词故事本/index.html`。
2. **UI 规范核对**：
   - **排版视角切换**：单按钮点按切换（`💻 电脑视角` / `📱 手机视角`），`index.html` 顶部 Header 中与 `S T O R Y` 标题在同一行**顶部对齐**分布。
   - **语音控制挂件**：右下角常驻悬浮挂件 (`#audioWidgetWrap`)，面板内保留朗读模式（关/手动/自动）、语速调节及**人声切换（Aria/Guy/Andrew + 试听）**。
3. **编译全量单元 HTML**：
   ```bash
   python scripts/build_unit_html.py all
   ```

---

## 📝 3. 提交 PR 时的文件变更清单 (Git PR Checklist)

在提交 PR 前，使用 `git status` 检查，一个标准的 PR 应该包含以下文件变更：

- [ ] **分支规范**：**绝对禁止直接提交到 `main` 分支！必须提交到 `xy` 分支**（如不存在需 `git checkout -b xy` 新建）。
- [ ] **真源文件**：`单词故事本/UnitNN.json` (或修改过的 JSON)
- [ ] **时间轴数据**：`单词故事本/pt_data/_pt_uNN.json`
- [ ] **朗读音频**：`单词故事本/audio/aria/...` (新增/更新的 mp3，仅在公开资产库或私有库中包含)
- [ ] **页面与文档**：全量 `单词故事本/UnitNN.html` 及 `单词故事本/UnitNN.md`
- [ ] **全局索引与首页**：`单词故事本/_units_manifest.js` 及 `单词故事本/index.html`
- [ ] **PWA 清单**：如新增了单元，确认 `单词故事本/sw.js` 已包含新增的 HTML 缓存路径。
- [ ] **安全隔离**：确认 `git status` 中没有泄漏版权 PDF、个人工作过程 `.workbuddy` 缓存或包含本机绝对路径的临时文件。

---

## 🚀 4. Git 提交 Commit 与 PR 命令行模板 (必须提交至 `xy` 分支)

> ⚠️ **强制要求**：
> 1. **禁止直接提交至 `main` 主分支**！必须推送到 **`xy` 分支**（不存在则新建 `git checkout -b xy`）。
> 2. 每次更新与提交**必须新建独立 Commit**，禁止未 Commit 直接覆盖推送代码！

```bash
# 1. 检查并切换到 xy 分支（若本地不存在则从当前起点新建 xy 分支）
git checkout xy 2>/null || git checkout -b xy

# 2. 暂存所有更新与编译文件
git add 单词故事本/ scripts/PR_DEVELOPMENT_GUIDE.md

# 3. 创建独立规范 Commit
git commit -m "docs(pr-guide): update PR workflow skill and UI compilation rules (target branch: xy)"

# 4. 推送到远程 xy 分支并提交 PR
git push -u origin xy
```
