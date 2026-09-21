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

当你（或通过 AI Skill）修改/新增某个单元（以 `Unit 01` 或新增的 `Unit 27` 为例）时，流水线操作步骤如下：

### 步骤一：编辑/生成唯一真源 JSON
在 `单词故事本/` 目录下修改或新建对应的 `UnitNN.json`。

### 步骤二：运行确定性校验器 (validate_unit.py)
```bash
python scripts/validate_unit.py 1
# 必须确认输出：validate ERROR 0
```

### 步骤三：生成音频与时间轴 (gen_unit_audio.py)
```bash
python scripts/gen_unit_audio.py 1
# 产出：单词故事本/audio/... 及 单词故事本/pt_data/_pt_u01.json
```

### 步骤四：重新编译 HTML、Markdown 与跨单元索引
```bash
# 1. 编译单元 HTML
python scripts/build_unit_html.py 1   # 或 python scripts/build_unit_html.py all

# 2. 派生 Markdown
python scripts/build_md.py 1

# 3. 重新打包全集搜索索引
python scripts/build_units_bundle.py

# 4. 校验运行时镜像同步
python 单词故事本/_sync_app.py
```

> 💡 **小技巧**：也可以直接运行一键流水线：
> `python scripts/run_unit_pipeline.py 1`

---

## 📝 3. 提交 PR 时的文件变更清单 (Git PR Checklist)

在提交 PR 前，使用 `git status` 检查，一个标准的 PR 应该包含以下文件变更：

- [ ] **真源文件**：`单词故事本/UnitNN.json` (或修改过的 JSON)
- [ ] **时间轴数据**：`单词故事本/pt_data/_pt_uNN.json`
- [ ] **朗读音频**：`单词故事本/audio/aria/...` (新增/更新的 mp3)
- [ ] **页面与文档**：`单词故事本/UnitNN.html` 及 `单词故事本/UnitNN.md`
- [ ] **全局索引**：`单词故事本/_units_manifest.js`
- [ ] **PWA 清单**：如新增了单元，确认 `单词故事本/sw.js` 已包含新增的 HTML 缓存路径。

---

## 🚀 4. Git 提交 PR 命令行模板

```bash
# 1. 创建并切换到新功能/修复分支
git checkout -b feature/update-unit-01

# 2. 暂存所有更新文件
git add 单词故事本/

# 3. 提交 Commit
git commit -m "feat(unit01): update story cards and sentence timing audio"

# 4. 推送到远程分支并提交 PR
git push origin feature/update-unit-01
```
