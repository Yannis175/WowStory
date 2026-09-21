---
name: word-storybook-generation
description: 把一个单元的英语词表 CSV 转成「单词故事本」结构化数据（英文故事段落 + 五维考点卡片），产出 JSON 供 html 原型与 Markdown 渲染。This skill should be used when 用户想换任何模型从词表 CSV 批量生成故事、考点卡、搭配句式数据，或需要校验生成结果是否完整（词覆盖、标记闭合、字段齐全、顺序对齐）。典型触发：用故事背考研/四六级单词、词表转故事本、生成 UnitNN.json、检查生成结果漏没漏词。
agent_created: true
---

# 单词故事本 · 单元数据生成规范与执行指南

把词表 CSV 里的**一个单元**，转成可直接喂给前端原型的结构化「故事本」数据 (`UnitNN.json`) 与衍生 Markdown (`UnitNN.md`)。

---

## 核心原则与痛点克服

### 1. 如何克服“频繁 Python 命令确认”弹窗？
* **痛点原因**：在当前 Agent 执行环境中，每次调用 `run_command` 执行单独命令（如：生成 Python 脚本 -> 运行生成 -> 运行校验 -> 导出 MD -> 运行四轮审查）都会在界面上触发一次用户审批弹窗。步骤越散，弹窗越多。
* **克服方案**：
  1. **单指令管线化 (Single Consolidated Command)**：将“提取校验 + 故事生成 + 结构校验 + MD 导出 + 四轮审查”打包进**单个 Master 自动化脚本**（如 `scripts/run_unit_pipeline.py`）中。用户只需在终端**确认 1 次**，整个管线自动跑完并汇报最终校验结果。
  2. **Batch 批量统一调度**：批量生成多个单元（如 Unit 27~30）时，在单一命令里循环处理整个 Batch，无需每个 Unit 分拆执行。

---

## 一、标准执行六步法

### 步骤 1：提取单词与源头质量校验 (Word Extraction & Validation)
* **抽取源数据**：从 `红宝书必考词_全量汇总_清洗版.csv` 抽取当前单元全部单词及常考含义。
* **提取校验（前置硬指标）**：
  1. **拼写与 OCR 截断比对**：将提取的单词与标准词典（如 `_words_alpha.txt`）比对，发现如 `carefu` → 修正为 `careful`，`mora` → `moral`。
  2. **重复与格式检查**：核对提取的单词列表是否存在内部重复、隐藏 Unicode 不可见字符。
  3. **词性与义项初审**：检查常考含义是否存在明显 OCR 噪声乱码（如 `“·“·`），预先清洗。

### 步骤 2：故事分组与叙事构思 (Story Planning & Grouping)
* **合理计算分组**：依据单元总词数 $N$，按 `12–20 词/篇` 计算所需篇数（如 54 词切 3 篇，81 词切 5 篇）。保持词族边界（同一词根/前缀词不割裂）。
* **明确叙事主题与情节**：在动笔前，为每篇故事设定背景场景与起承转合：
  - **S1**：设定主题（如《法律审计》/《科学探究》），规划包含的 12-20 个目标词。
  - **S2**：设定情节冲突与转折，理清叙事脉络。

### 步骤 3：考研英语一/英语二高阶文本创作 (NEEP Standard Drafting)
* **考研语法与句式规范**：
  - 正文与加分句式（`pat`）必须严格符合**考研英语一 / 考研英语二**的语法规范、高级句式结构（如：非谓语动词短语、定语从句、状语从句、虚拟语气、同位语从句等）。
  - 用词地道严谨，避免口语化、幼教化句式。
* **标记语法 `[[surface|base]]` 规范**：
  - **参数顺序绝不可写反**：`[[surface|base]]` 中，**第 1 个参数必须是正文中的变形/表面词 (`surface`)**，**第 2 个参数必须是 `words[]` 中的词典原形 (`base`)**。
  - 例：`[[diminishment|diminish]]`（正文是 diminishment，原形是 diminish）；`[[expectations|expectation]]`。若写反为 `[[diminish|diminishment]]` 会报 E40 错误！

### 步骤 4：构建五维考点卡片 (Word Card Attribute Construction)
每词包含 12 个属性，保持固定五维顺序：
1. `w`: 词形（等于 CSV 单词名）
2. `ipa`: 英式音标（**严禁带前后斜杠 `/`**，如 `"ˈdʒɜːnəlɪst"`）
3. `pos`: 规范词性（`n.` `v.` `vt.` `vi.` `adj.` `adv.`）
4. `s`: 所属故事 ID（`s1` ~ `sN`）
5. `zh`: **故事义**（2–6 字，必须与本篇故事中的语境含义一致）
6. `exam`: **常考义**（来自 CSV 骨架）
7. `c`: **核心搭配**（2–4 条，带中文翻译，优先介词/动宾搭配）
8. `syn`: **近义替换**（2–3 条，覆盖阅读同义改写与写作升级词）
9. `fam`: **词族延伸**（1–3 条，带词性，**严禁为空**）
10. `dif`: **易混辨析**（一句话说明形近/义近区别）
11. `pat`: **加分句式**（符合考研英一/英二语法的作文句式，**必须包含目标词**）
12. `patZh`: 例句中文翻译

### 步骤 5：单指令自动化管线运行 (Consolidated Pipeline Execution)
执行统一 Master 脚本：
```bash
python -X utf8 scripts/run_unit_pipeline.py --unit 27
```
实现一键：`JSON 生成` → `validate_unit.py 校验` → `build_md.py 导出 Markdown` → `4轮自动化深查`。

### 步骤 6：全方位四轮严格审查 (4-Round Multi-Pass Audit)

---

## 二、四轮深度审查逻辑详解 (4-Round Audit Suite)

为了确保生词无错、含义精准、语法地道，生成后必须依次执行以下**四轮针对性审查**：

### 🔍 第 1 轮：全面综合与结构对齐检查 (Pass 1: Comprehensive Baseline Audit)
* **检查重点**：
  - JSON 顶层结构完整性（`unit`, `stories`, `words` 字段齐全）。
  - **CSV 100% 覆盖率**：对比 CSV 与 JSON `words[]`，确保既不漏词也不多词（校验 E30/E31）。
  - 正文标记全覆盖检查：确保每个目标词在故事正文中至少被标记一次（校验 E41）。
  - 自动化脚本 `validate_unit.py` 达到 **ERROR = 0**。

### 🔍 第 2 轮：拼写、音标与卡片五维属性深查 (Pass 2: Spelling, IPA & Card Attributes Audit)
* **检查重点**：
  - **拼写与编码**：检查英文单词是否在标准词典中，杜绝拼写错误；扫描全文本是否存在隐藏 Unicode 不可见字符 (`\u200b`, `\ufeff`)。
  - **音标规范**：检查 `ipa` 字段是否删除了首尾斜杠 `/`。
  - **卡片属性完整性**：
    - `fam`（词族延伸）数组**绝不可为空**。
    - `c`（核心搭配）每条必须包含**英文搭配 + 中文翻译**。
    - `pat`（加分句式）中必须出现该目标词的词干。

### 🔍 第 3 轮：考研英一/英二语法、义项与语境对齐审查 (Pass 3: NEEP Grammar & Context Audit)
* **检查重点**：
  - **考研语法合规性**：审查故事正文及 `pat` 例句是否符合考研英语一/二的复杂句法规范（无语法错误、时态一致、主谓一致、从句引导词使用正确）。
  - **故事义 (`zh`) 语境吻合度**：核对 `zh` 是否精准反映了该词在当前故事段落中的上下文含义，严禁照抄无关的第一义项。
  - **常考义 (`exam`) 忠实度**：核对 `exam` 保持 CSV 骨架含义，无虚假幻觉或随意删改。
  - **辨析精准度 (`dif`)**：审查近义词/形近词辨析是否准确切中考点。

### 🔍 第 4 轮：故事逻辑、标记语法 `[[surface|base]]` 与 Markdown 排版一致性检查 (Pass 4: Story Logic, Tagging & Markdown Audit)
* **检查重点**：
  - **故事叙事起伏**：故事情节是否通顺自然（起承转合），避免为了塞词而机械堆砌名词。
  - **标记语法方向**：严格检查正文中所有 `[[surface|base]]` 标记，确保 `surface` 在前、`base` 在后。
  - **单次标记原则**：故事中同一词汇仅在首次出现时标记 `[[...]]`。
  - **Markdown 一致性**：运行 `build_md.py` 导出 `UnitNN.md`，检查派生 Markdown 是否排版清晰、加粗正确、全词速查表无缝对齐。

---

## 三、输出 Schema 样例

```json
{
  "unit": 27,
  "stories": [
    {
      "id": "s1",
      "en": "The Institutional Reform",
      "zh": "机构改革",
      "theme": "法律 / 社会",
      "ps": [
        {
          "en": "Under severe economic pressure, the legal [[advisor]] issued a formal [[warning]], emphasizing that sustainable [[growth]] required strict compliance.",
          "zh": "在严峻的经济压力下，法律顾问发出了正式警告，强调可持续增长需要严格的合规。"
        }
      ]
    }
  ],
  "words": [
    {
      "w": "advisor",
      "ipa": "ədˈvaɪzə",
      "pos": "n.",
      "s": "s1",
      "zh": "顾问",
      "exam": "顾问；指导老师",
      "c": ["legal advisor 法律顾问", "senior advisor 资深顾问"],
      "syn": ["consultant", "counselor", "guide"],
      "fam": ["advise v. 建议", "advice n. 建议"],
      "dif": "advisor 指在特定领域提供专业咨询建议的顾问；counselor 侧重心理咨询或法庭律师。",
      "pat": "The board appointed a senior advisor to evaluate corporate restructuring risks.",
      "patZh": "董事会任命了一位资深顾问来评估公司重组风险。"
    }
  ]
}
```

---

## 四、底线禁区与避坑清单

1. **标记参数顺序绝对禁止反转**：必须为 `[[surface|base]]`。
2. **故事标题禁止单单词**：英文标题必须为 **2–5 个单词**（如 `The Growth Challenge`），具文学感与考研主题感。
3. **`fam` 字段禁止留空**：必须包含同根词及词性。
4. **`ipa` 禁止带斜杠**：写 `"ˈdʒɜːnəlɪst"`，不写 `"/ˈdʒɜːnəlɪst/"`。
5. **`exam` 禁止臆造**：忠实于 CSV 骨架义项。
6. **分批打包单指令运行**：生成时优先编写单个 Master Python 运行脚本，避免产生大量需要人工依次审批的小 Python 命令。
