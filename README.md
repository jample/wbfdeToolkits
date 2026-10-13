# wbfdetoolkits：FDE Toolkits Simple v0.6/v0.7 的 WorkBuddy Skills 实现

本项目按 [`fde_toolkits_designSimplev0.6.md`](../fde_toolkits_designSimplev0.6.md)（Simple v0.6.2）和 [`fde_toolkits_designSimplev0.7.md`](../fde_toolkits_designSimplev0.7.md)（Simple v0.7.1）实现七个对话式 WorkBuddy Skills，帮助 FDE 通过"给文件位置 → 生成初稿 → 补问 → 完善文档"的方式，完成项目脚手架初始化（v0.8 新增，本项目新增 Skill）、访前准备、需求探究、智能体蓝图设计（v0.6），以及交付内容与培训、客户移交、WorkBuddy 资产归档（v0.7）。

- 当前版本：**v0.8.0**（v0.6 首期三个 Skill + v0.7 新增三个 Skill + v0.8 新增项目初始化 Skill，及多轮会话内功能性验收测试后的修正），变更历史见 [版本与变更记录](#版本与变更记录)。
- 七个 Skill 均为文档型 Skill：由 WorkBuddy 按各 `SKILL.md` 对话式执行，不含可运行代码，不依赖外部运行环境。

## 七个 Skills

### 初始化：项目脚手架（v0.8 新增，本项目新增 Skill，无上游设计章节）

| Skill | 自然语言入口 | 主要方法 | 主要输出 |
|---|---|---|---|
| [`fde-init`](skills/fde-init/SKILL.md) | "帮我新建一个 FDE 项目" | 项目信息收集、骨架生成、幂等与覆盖保护 | `<项目>/00_项目总览/`（项目总览 + 交付计划）+ 01–07 阶段目录骨架与各阶段 README 占位 |

`fde-init` 只建骨架：项目总览填入用户提供的名称与概要，其余章节标"待补"；其余六个内容 Skill 在已初始化的脚手架根目录下对特定阶段目录做内容修改。目录中存在 `00_项目总览/项目总览.md` 即视为已初始化的项目根。

### v0.6：需求获取、捕获与蓝图设计

| Skill | 自然语言入口 | 主要方法 | 主要输出 |
|---|---|---|---|
| [`fde-discovery-prepare`](skills/fde-discovery-prepare/SKILL.md) | "帮我准备这家客户的需求访谈" | 背景整理、岗位角色卡、典型工作日、场景假设、验证问题 | `<项目>/01_预检/访前准备.md` |
| [`fde-discovery-capture`](skills/fde-discovery-capture/SKILL.md) | "把这些访谈和样例整理成需求" | 原始内容归类、假设核验、5W1H、主流程/异常、规则提取 | `<项目>/02_需求探究/角色与场景总览.md` + 每场景 `scenes/<scene-id>/scene-requirement.md` |
| [`fde-design-blueprint`](skills/fde-design-blueprint/SKILL.md) | "把这个需求设计为 WorkBuddy 智能体蓝图" | 场景走查、人机分工、输入输出设计、知识/系统映射、验收推导 | `<项目>/03_场景设计/scenes/<scene-id>/scene-blueprint.md` |

### v0.7：交付、移交与资产归档

| Skill | 自然语言入口 | 解决的问题 | 主要输出 |
|---|---|---|---|
| [`fde-deliver`](skills/fde-deliver/SKILL.md) | "根据蓝图和已有 WorkBuddy 内容准备客户交付材料和培训" | 一个或多个场景应向客户交付哪些内容，怎样解释、使用、培训和确认 | `<项目>/06_交付与培训/`：交付内容总览 + 每场景交付说明 + 培训与使用指南 |
| [`fde-transfer`](skills/fde-transfer/SKILL.md) | "把这个项目的交付内容整理成客户移交包" | 客户最终接收什么，谁维护什么，发生内容变化或使用问题时怎样处理 | `<项目>/07_支持移交归档/`：客户移交总览 + 每场景移交说明 + 内容维护与支持说明 |
| [`fde-assets-archive`](skills/fde-assets-archive/SKILL.md) | "从这个项目提取可复用的 WorkBuddy 场景资产包" | 从完整项目中提取可复用资产，保留来源、边界和后续适配说明 | 独立资产暂存目录（不写入客户项目）：场景资产包 + 资产清单 + 来源追溯 + 脱敏与复用说明 |

边界要点：

- `fde-init` 只建立目录骨架和 00 占位文件，不写业务内容，不覆盖既有非空文件；`fde-deliver` 不构建或部署能力、不验证真实系统、不替客户确认；`fde-transfer` 不产生通用资产、不把内部源文件默认交给客户；`fde-assets-archive` 不直接发布到资产库、不复制客户专属/无权复用内容。
- 七个 Skill 可独立调用，不要求先运行前一个。项目脚手架初始化由 `fde-init` 负责；各内容 Skill 在脚手架根下修改对应阶段目录，未初始化时可降级自建所需目录；增加场景、质量检查和修订是各 Skill 的内部动作。
- 客户交付流与资产复用流是两条不同的信息流，不使用同一个目录，也不能通过"删掉客户名称"简单互相转换（v0.7 设计 §0.4）。

## 在 WorkBuddy 中安装（项目级）

Skill 的 `SKILL.md` 通过相对路径引用 [`shared/`](shared/) 下的共用规则（`../../shared/*.md`），因此安装时必须保持 `skills/` 与 `shared/` 的并列结构，不能只复制单个 Skill 目录。

在目标项目根目录执行：

```bash
# 方式一：复制（推荐，项目自包含）
mkdir -p .workbuddy
cp -R /path/to/wbfdetoolkits/skills .workbuddy/skills
cp -R /path/to/wbfdetoolkits/shared .workbuddy/shared

# 方式二：软链接（便于跟随本仓库更新）
mkdir -p .workbuddy
ln -s /path/to/wbfdetoolkits/skills .workbuddy/skills
ln -s /path/to/wbfdetoolkits/shared .workbuddy/shared
```

安装后目标项目的结构：

```text
<你的项目>/.workbuddy/
├── skills/
│   ├── fde-init/                 # v0.8：SKILL.md + references/ + templates/ + examples/
│   ├── fde-discovery-prepare/    # v0.6：SKILL.md + references/ + templates/ + examples/
│   ├── fde-discovery-capture/
│   ├── fde-design-blueprint/
│   ├── fde-deliver/              # v0.7：SKILL.md + references/ + assets/templates/
│   ├── fde-transfer/
│   └── fde-assets-archive/
└── shared/                       # 七个 Skill 共用的执行契约与规则（必需）
```

说明：

- `tests/` 是开发验收资产，不需要安装到目标项目。
- WorkBuddy 启动后按各 `SKILL.md` 的 frontmatter `description` 自动路由自然语言请求；也可以用 Skill 名显式指定（如"使用 fde-deliver …"）。
- 若 WorkBuddy 使用其他技能目录约定（如 `.agents/skills/`），用同等方式放置并保持 `skills/` 与 `shared/` 并列即可。
- `fde-init` 与 v0.6 三个 Skill 使用 `templates/` + `examples/` 布局；v0.7 三个 Skill 按 Skill Creator 规范使用 `assets/templates/`（待复制到项目的空白模板），详细方法和案例放在 `references/`，Skill 内不含 README 和 examples/。

## 如何使用

### 基本用法

在 WorkBuddy 对话中直接用自然语言说明任务，例如：

> 请使用需求探究 Skill。客户访谈纪要和任务演示记录在"资料目录"，项目在"项目目录"。请整理销售和运营的角色、询盘处理场景、主流程和异常，并告诉我还需要补充什么。

不需要先填标准表、不需要记命令或字段编号。Skill 自动归纳内部 `RunRequest`（见 [shared/execution-contract.md](shared/execution-contract.md)），读取材料生成初稿，每轮最多补问 1–3 个高影响问题，并把结果写入固定章节的目标文件。

复杂任务时可以按五行表达帮助 Skill 定位（可选，不是必填模板）：

```text
目标：初始化项目 / 准备访谈 / 整理需求 / 完善蓝图 / 准备交付材料 / 整理移交 / 形成资产包。
项目位置：希望读取或保存到的项目目录。
输入材料：一个或多个文件/目录地址；如有需要，注明重点章节。
直接补充：没有文件的背景、规则、例子、确认或设计选择，用自然语言描述。
本次结果：先出草稿、补齐某一部分、供客户确认，或生成待评审资产包。
```

### 一轮对话中会发生什么

1. **识别任务**：Skill 判断本轮目标并一句话说明。
2. **读取资料**：读取给出的文件/目录，告知实际读取范围；不可读文件单独指出。
3. **生成初稿**：按方法整理为有业务内容、来源和待补点的初稿。
4. **定向补问**：最多 1–3 个会改变范围、责任、交付内容或复用边界的高影响问题。
5. **合并修订**：接受文字补充、新文件位置或直接编辑过的文档。
6. **保存成果**：输出文件链接、状态、待补材料和下一步。

### 每个 Skill 的一句话用法

| 阶段 | 示例说法 | 详细流程 |
|---|---|---|
| 00 初始化 | "新建项目'蓝湾跨境销售智能体项目'，概要是为其销售团队构建 WorkBuddy 智能体，目录用 projects/bluebay/。" | [SKILL.md](skills/fde-init/SKILL.md)（I1–I3）、[对话缩影](skills/fde-init/examples/dialogue-walkthrough.md) |
| 01 预检 | "资料在售前资料目录，帮我准备销售团队访谈。" | [SKILL.md](skills/fde-discovery-prepare/SKILL.md)（A1–A4）、[对话缩影](skills/fde-discovery-prepare/examples/dialogue-walkthrough.md) |
| 02 需求探究 | "补充运营访谈，地址是……，重点看 OPS-03。请据此修正角色分工。" | [SKILL.md](skills/fde-discovery-capture/SKILL.md)（B1–B6）、[对话缩影](skills/fde-discovery-capture/examples/dialogue-walkthrough.md) |
| 03 场景设计 | "根据两个确认需求设计智能体，系统按 Hyp-sys.md 设计。" | [SKILL.md](skills/fde-design-blueprint/SKILL.md)（C1–C8）、[对话缩影](skills/fde-design-blueprint/examples/dialogue-walkthrough.md) |
| 06 交付与培训 | "蓝图在 03_场景设计/，实际 Skill 和 Prompt 在交付目录，帮我生成本轮的交付材料和角色培训指南。" | [SKILL.md](skills/fde-deliver/SKILL.md)（D1–D5）、[方法详解](skills/fde-deliver/references/delivery-methods.md) |
| 07 客户移交 | "按 06 的交付内容和实际文件目录，整理客户移交包，说明谁维护什么。" | [SKILL.md](skills/fde-transfer/SKILL.md)（E1–E5）、[方法详解](skills/fde-transfer/references/transfer-methods.md) |
| 跨阶段资产化 | "从这个项目提取询盘场景的可复用资产，输出到独立的资产暂存目录，先只做候选分析。" | [SKILL.md](skills/fde-assets-archive/SKILL.md)（F1–F7）、[方法详解](skills/fde-assets-archive/references/archive-methods.md) |

### 设计原则（摘要）

- 先有内容初稿，再问影响结果的少量问题；输入接受自然材料，输出采用稳定章节。
- 未知信息允许保留并集中列出，非关键缺项不阻止草稿生成。
- 假设、FDE 设计选择/建议和客户确认分别标注；关键结论必须能回指来源。
- 三类内容状态不能互相推断：文档状态（草稿/有条件可用/已确认范围）、交付状态（盘点中/可供交付/已提供/已接收）、复用状态（禁止复用/待脱敏与评审/可在确认范围内复用）（见 [shared/quality-gates.md](shared/quality-gates.md)）。
- 已确认范围受保护：只有 FDE 明确说明新的确认来源和覆盖范围，才允许修改（见 [shared/merge-rules.md](shared/merge-rules.md)）。
- 场景是交付说明、移交确认和资产复用的最小颗粒度；项目级文档只做聚合，不复制场景完整内容。

## 如何测试

这些是文档型 Skill，测试方式是：在 WorkBuddy 中加载 Skill，用测试夹具或金样例输入实际对话执行，然后按断言检查行为与产物。完整说明见 [tests/acceptance-matrix.md](tests/acceptance-matrix.md)。

本地可重复的契约检查命令：

```bash
python3 tests/run_functional_tests.py
```

脚本检查七个 Skill 的实现包完整性、关键规则（含 `references/`）、输出模板章节、已提交的对话模拟产物，以及客户项目/移交包/资产暂存之间的安全与状态不变量。2026-09-24 本轮结果为 **217/217 通过**。由于 Skill 本身是文档和对话契约而非可执行服务，该脚本不能替代 WorkBuddy 真实运行；真实对话仍应按验收矩阵逐条复验。

对话模拟参考：`tests/sandbox/` 保留本会话按 `SKILL.md` 执行的代表性产物，覆盖 `i1/`（fde-init 初始化示例脚手架）、`p1/`、`p2/`、`c2/`、`c3/`、`b2/`、`x1/`、`x3/`、`x4/`、`x5/`、`x6/`、`chain/`、`d2-d6/`、`t3-t6/`、`a2-a8/` 和 `golden/`（金样例 8 步完整链路；旧阶段 1–2 快照保留在 `golden-20260914-step12-snapshot/`），以及复测目录（`retest-x4/`、`retest-b3/`）；`assets-staging/` 为空目录，用于验证 A1/A9 的仅分析和输出隔离边界。该目录是测试产物，不属于 Skill 安装包。

### 测试分层

| 层 | 内容 | 位置 |
|---|---|---|
| v0.6 单测矩阵 | 16 个测试（P1–P2 / C1–C4 / B1–B3 / X1–X6），每个测试含输入、必须观察到的结果和四条共性断言 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 1–2 节 |
| v0.6 端到端金样例 | 8 个试用任务，用跨境电商实例从"只有一句背景"跑到"重新打开项目补新纪要" | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 3 节 |
| v0.7 单测矩阵 | 24 个用例（D1–D7 / T1–T7 / A1–A10），覆盖交付、移交和资产归档 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 6 节 |
| fde-init 单测矩阵 | 5 个用例（I1–I5），覆盖最小输入初始化、缺信息补问、覆盖保护、幂等和下游定位 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 8 节 |
| 资产完整性检查 | 模板/实例路径存在、关键结构齐全、实例能回指输入、章节编号与设计一致 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 4 节 |
| 完成标准 | v0.6 三 Skill（15.9 节）与 v0.7 三 Skill（9.2–9.4 节）各自的完成判定 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 5、7 节 |

### v0.6 共性断言（每个测试都必须满足）

1. 主要输出文件路径正确（`01_预检/`、`02_需求探究/`、`03_场景设计/` 约定）。
2. 关键结论有来源或状态。
3. 未知项未伪装成事实。
4. 最终回复包含输出状态、已完成范围和下一步。

### v0.7 共性断言（每个用例都必须满足）

1. 场景是最小交付和复用颗粒度；2. 项目总览和场景内容没有重复堆叠；3. 管理文档为 Markdown，原始资产保留原格式；4. 未知内容未写成事实；5. 客户确认、交付状态和复用状态没有混淆；6. 客户项目、客户移交包和通用资产包相互隔离；7. 最终回复包含文件、范围、状态、待补和下一步。

### v0.6 测试用例与输入数据

| 测试 | 目的 | 输入数据 |
|---|---|---|
| P1 最小准备输入 | 一句背景生成有内容的访前准备 | [fixtures/p1-minimal-background.md](tests/fixtures/p1-minimal-background.md) |
| P2 目录输入 | 混杂目录中正确筛选本轮相关文件 | [fixtures/p2-mixed-directory-listing.md](tests/fixtures/p2-mixed-directory-listing.md) |
| C1 无 01 直接捕获 | 一份销售访谈直接生成角色和场景草稿 | [fixtures/c1-sales-interview.md](tests/fixtures/c1-sales-interview.md) |
| C2 多角色冲突 | 冲突原话并列保留并补问，不静默覆盖 | [fixtures/c2-conflicting-interviews.md](tests/fixtures/c2-conflicting-interviews.md) |
| C3 增量修订 | 已有需求 + 新经理纪要，只更新受影响章节 | 对话直接输入（矩阵第 2.2 节给出输入方法） |
| C4 重复执行 | 同一输入运行两次不产生重复内容 | 复用 [fixtures/c1-sales-interview.md](tests/fixtures/c1-sales-interview.md) 跑两次 |
| B1 无系统资料 | 完成业务蓝图，系统域列待补不虚构 | [fixtures/b1-confirmed-requirement-no-system.md](tests/fixtures/b1-confirmed-requirement-no-system.md) |
| B2 系统补充 | 业务蓝图 + Hyp-sys 更新系统映射 | [../fde跨境电商/03_场景设计/Hyp-sys.md](../fde跨境电商/03_场景设计/Hyp-sys.md) |
| B3 越权保护 | 自动合并/自动外发要求被明确指出冲突 | [fixtures/b3-overreach-request.md](tests/fixtures/b3-overreach-request.md) |
| X1 文件不可读 | 指明不可读文件并继续其他材料 | 对话直接输入 |
| X2 FDE 回答未知 | 保存待补与影响，本轮不重复追问 | 对话直接输入 |
| X3 两场景衔接 | 询盘首次行动成为跟进输入 | [跟进需求](../fde跨境电商/02_需求探究/confirmed/scenes/SCN-SALES-FOLLOWUP/scene-requirement.md) |
| X4 已确认内容保护 | 冲突新访谈不覆盖已确认范围 | [fixtures/x4-confirmed-requirement-and-conflict.md](tests/fixtures/x4-confirmed-requirement-and-conflict.md) |
| X5 自由表达输入 | 自动归纳内部 RunRequest，不要求填模板 | [fixtures/x5-freeform-input.md](tests/fixtures/x5-freeform-input.md) |
| X6 大文件/超范围 | 缩小到相关章节或分块，明确已读范围 | 对话直接输入 |

### v0.7 测试用例与输入数据

v0.7 用例以对话直接输入为主（描述要提供的材料和说法），不强制专用夹具；逐条说明见 [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 6 节。

| 用例组 | 覆盖重点 | 输入数据 |
|---|---|---|
| D1–D7（fde-deliver） | 无实际文件不虚构路径、目录盘点分类、共享内容登记一次、客户适配不改通用核心、角色化培训、部分确认、重复执行 | 对话直接输入；案例素材可参考 v0.7 设计第 6 节"销售拜访准备助手" |
| T1–T7（fde-transfer） | 路径未齐保持盘点中、权利未知标待确认、部分场景移交、触发式维护责任、条件接收、内部内容不进客户包、重复执行 | 对话直接输入 |
| A1–A10（fde-assets-archive） | 只分析不复制、场景颗粒度、共享资产引用、客户 Prompt 参数化、源代码权利未知排除、MCP 配置脱敏、项目证据隔离、已有正式资产更新候选、输出目录隔离、重复运行 | 对话直接输入 |

### fde-init 测试用例与输入数据

fde-init 用例以对话直接输入为主，逐条说明见 [tests/acceptance-matrix.md](tests/acceptance-matrix.md) 第 8 节。

| 用例组 | 覆盖重点 | 输入数据 |
|---|---|---|
| I1–I5（fde-init） | 最小输入初始化、缺关键信息补问、无关内容覆盖保护、重复执行幂等、下游 Skill 脚手架根定位 | 对话直接输入；I1 示例产物见 [tests/sandbox/i1/](tests/sandbox/i1/) |

端到端金样例使用的跨境电商实例数据（只读引用，不复制到本项目）：

| 金样例步骤 | 实例数据 |
|---|---|
| 1 只提供预检背景 | [../fde跨境电商/01_预检/industry-profile-source.md](../fde跨境电商/01_预检/industry-profile-source.md)（兼用 P1 夹具） |
| 2 加入 OPS-03 | [../fde跨境电商/02_需求探究/interview-records/20260831-ROLE-ECOM-OPS-001-interview.md](../fde跨境电商/02_需求探究/interview-records/20260831-ROLE-ECOM-OPS-001-interview.md) |
| 3 加入销售访谈和任务回放 | [销售访谈](../fde跨境电商/02_需求探究/interview-records/20260831-ROLE-SALES-REP-001-interview.md)、[任务观察](../fde跨境电商/02_需求探究/task-observations/20260831-ROLE-SALES-REP-001-SALES-DAY-observation.md) |
| 4 补充经理确认 | [经理访谈](../fde跨境电商/02_需求探究/interview-records/20260831-ROLE-REGIONAL-SALES-MGR-001-interview.md) |
| 5 确认纪要 + 依赖说明 | [confirmation-record.md](../fde跨境电商/02_需求探究/confirmed/confirmation-record.md) |
| 6 选定需求 + 设计会议 | [询盘需求](../fde跨境电商/02_需求探究/confirmed/scenes/SCN-INQUIRY-TRIAGE/scene-requirement.md)、[联合设计访谈](../fde跨境电商/03_场景设计/scene-interviews/scenes-interviews.md) |
| 7 提供 Hyp-sys | [../fde跨境电商/03_场景设计/Hyp-sys.md](../fde跨境电商/03_场景设计/Hyp-sys.md)（兼用 B1 夹具做无系统对照） |
| 8 设计选择 + 跟进场景 + 补新纪要 | [跟进需求](../fde跨境电商/02_需求探究/confirmed/scenes/SCN-SALES-FOLLOWUP/scene-requirement.md)、[Workshop 确认记录](../fde跨境电商/03_场景设计/workshop-confirmation-record.md) |

注意：`tests/fixtures/` 下的夹具是虚构测试输入，跨境电商实例是教学案例，两者都不得作为新客户项目的事实来源。

## 版本与变更记录

### 本项目（实现）

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v0.6.2 | 2026-09-05 | 首期实现：三个 Skills（`fde-discovery-prepare` A1–A4、`fde-discovery-capture` B1–B6、`fde-design-blueprint` C1–C8）的 `SKILL.md` 与 `references/methods.md`；`shared/` 四个共用规则文件；模板与实例资产沿用 fde-toolkit 仓库 `simple-v0.6` 基线（置于 `templates/`、`examples/`，无版本子目录）；`tests/` 验收矩阵与 8 个输入夹具。 |
| v0.7.1 | 2026-09-14 | 扩展实现：新增 `fde-deliver`（D1–D5）、`fde-transfer`（E1–E5）、`fde-assets-archive`（F1–F7）三个 Skills，按 Skill Creator 规范采用 `assets/templates/` 结构，详细方法放 `references/`（资产归档另含 `workbuddy-asset-types.md`、`de-identification-rules.md`）；`shared/` 四个文件按 v0.7 设计 §7.1 扩展（内部推断字段 scene_scope/operation_intent/output_scope、交付/移交/资产证据边界、三类内容状态、三个新质量门、不允许的 AI 行为）；验收矩阵新增 24 个用例（D1–D7/T1–T7/A1–A10）和 v0.7 共性断言。 |
| v0.7.2 | 2026-09-14 | 会话内对话式验收测试后的修正（9 个独立用例全量执行：P1/C2/X4/B3/D1/T1/T2/A1/A9；另执行 1 条 C1→B1 链路，断言全部通过；产物保留在 `tests/sandbox/`）：`shared/merge-rules.md` 规则 5/7/10 明确冲突并列落点、涉已确认范围冲突的"原范围/变化/当前状态"三要素、FDE 转述确认（含"有纪要但未读原文"情形）的标注；`shared/quality-gates.md` 新增门通过与高影响问题的关系、"未决冲突"界定（仅登记未并入设计的被拒变更请求可标"有条件可用（含未决变更请求）"）；`fde-discovery-capture` 明确 scene-id 大写连字符规则、补问须含影响章节与继续方式；`fde-design-blueprint` §11 越权保护扩展到已写明的人工边界（含推演边界），被拒要求写入 §8.3 不并入设计；`fde-deliver` 统一 `06_交付与培训/` 目录称谓与既有目录探测指引、质量门与 shared 规则冲突时从严；`fde-transfer` 统一四档接收结论命名及其与交付状态的映射、消除枚举外状态词"可供移交"；`fde-assets-archive` 澄清仅分析模式（F1–F3 无需输出目录）、内容尚不存在时的登记规则，补齐 `assets/templates/培训材料模板.md`，统一复用状态三值术语，明确抽象产物默认归场景专属资产；两个模板（scene-requirement/scene-blueprint）的"尚未解决的冲突"条目补记录要素提示。复测：X4/B3 全断言通过，无新增问题。 |
| v0.7.3 | 2026-09-16 | 功能性用例全量执行后的修正（按用户要求执行全部功能性用例，"重复执行/幂等"类非功能用例 C4/D7/T7/A10 本期不执行；共执行 20 个用例 + 金样例 8 步端到端链路：P2/C3/X1/X2/B2/X3/X5/X6/D2–D6/T3–T6/A2–A8/golden，断言全部通过；本地契约检查 `tests/run_functional_tests.py` 197/197）：`fde-discovery-prepare` methods.md 置信度指引对齐模板实际列、`访前准备` 模板 §6.2 取值提示改为表下注释；`shared/merge-rules.md` 规则 5 补"目录纯文字描述、文件本体未提供"情形的处理口径；`fde-discovery-capture` SKILL.md §7 高影响问题示例补全为"影响章节+不知道时怎样继续"两段式，总览/需求/蓝图模板"本轮更新"补多轮分条记录说明；`fde-deliver` 读取范围声明明确多轮追加口径；`fde-assets-archive` 脱敏规则补"资产包 ID/目录命名不得含客户标识"和"治理文档自身也须过内容级检查、不抄录被排除的值"；`tests/run_functional_tests.py` 修正一处过严的字面匹配；验收矩阵第 8 节补沙盒复用/重置约定与两轮执行记录。 |
| v0.8.0 | 2026-09-24 | 新增 `fde-init`（I1–I3，本项目新增 Skill，无上游设计章节）：项目脚手架初始化 Skill，采用 v0.6 风格布局（`SKILL.md` + `references/methods.md` + `templates/` + `examples/`），根据项目名称和概要建立 00–07 目录骨架，`00_项目总览/` 填入基本信息（项目总览 + 空白交付计划）、其余章节标"待补"，01–07 只放阶段 README 占位；幂等且不覆盖既有非空文件，目标目录含无关内容时提示风险请 FDE 确认。六个内容 Skill 的 `SKILL.md` 增加统一的项目根定位规则（优先 FDE 指定目录；否则向上查找含 `00_项目总览/项目总览.md` 的脚手架根；未找到时提示可用 fde-init 但不阻塞、降级自建阶段目录）和"初始化脚手架 → fde-init"不适用项。`shared/` 四文件改为七个 Skill 口径：execution-contract.md 补项目根定位规则，merge-rules.md 补初始化保护规则，quality-gates.md 新增 fde-init 初始化质量门。验收矩阵新增第 8 节 fde-init 用例 I1–I5 与共性断言；`tests/run_functional_tests.py` 同步扩展（新增 `sandbox/i1/` 示例脚手架），契约检查 217/217 通过。 |

### 对应设计文档（上游）

| 版本 | 日期 | 变更内容 |
|---|---|---|
| Simple v0.6 | 2026-09-05 | 建立三个对话式 Skills 的总体设计，统一输入输出约定，拆成 A1–A4、B1–B6、C1–C8，增加跨境电商连续补充实例。 |
| Simple v0.6.1 | 2026-09-05 | 完成开发可实施性审查：新增共用调用输入、输入输出合同、证据与增量合并、确认内容保护、补问规则、三阶段质量门、异常恢复、验收测试矩阵和完成标准。 |
| Simple v0.7 | 2026-09-14 | 初步设计阶段 4 `fde-deliver` 与阶段 5 `fde-transfer`，将完整交付方法延伸到后续阶段。 |
| Simple v0.7.1 | 2026-09-14 | 修正 `fde-deliver` frontmatter；移除对外部运行环境的依赖，将后续 Skill 收敛为文本交付内容与客户移交；新增 `fde-assets-archive`，定义场景级资产颗粒度、WorkBuddy 资产类型、独立资产包目录、来源追溯、客户隔离、复用边界、F1–F7 和验收矩阵。 |

### 当前范围

- **已包含**：七个 Skills（项目初始化 + 需求三件套 + 交付/移交/资产归档）、模板与方法说明、跨境电商示例、验收测试资产。
- **明确不包含**：阶段 3 交付开发的具体实现工作、生产 API 权限验证、运行时字段映射 DSL、多客户并行项目管理、自动化 ROI 计算、对外部系统的任何操作（删除/上传/公开发布/外部发送）。

## 目录结构

```text
wbfdetoolkits/
├── README.md
├── shared/                          # 七个 Skill 共用的执行契约与规则（安装时必需）
│   ├── execution-contract.md        # 内部 RunRequest、统一执行顺序（含项目根定位）、异常恢复、两层质量检查
│   ├── merge-rules.md               # 读取范围、证据类型边界、增量合并与冲突规则、初始化保护
│   ├── questioning-rules.md         # 少问不漏的补问规则、一轮对话节奏、每步回应格式
│   └── quality-gates.md             # 三类内容状态、七个阶段质量门
├── skills/
│   ├── fde-init/                    # v0.8：I1–I3 项目脚手架初始化（本项目新增）
│   │   ├── SKILL.md
│   │   ├── references/methods.md
│   │   ├── templates/               # 项目总览.md、交付计划.md 两份空白模板
│   │   └── examples/                # 项目总览.md 填写样例 + 对话缩影
│   ├── fde-discovery-prepare/       # v0.6：A1–A4 访前准备
│   │   ├── SKILL.md
│   │   ├── references/methods.md
│   │   ├── templates/               # 访前准备.md（主要输出）、business-background-input.md（可选输入）
│   │   └── examples/                # 填好的跨境电商实例 + 对话缩影 + 来源说明
│   ├── fde-discovery-capture/       # v0.6：B1–B6 需求探究
│   │   ├── SKILL.md
│   │   ├── references/methods.md
│   │   ├── templates/               # 角色与场景总览.md、scene-requirement.md、两个可选输入模板
│   │   └── examples/
│   ├── fde-design-blueprint/        # v0.6：C1–C8 蓝图设计
│   │   ├── SKILL.md
│   │   ├── references/methods.md
│   │   ├── templates/               # scene-blueprint.md、三个可选输入模板
│   │   └── examples/
│   ├── fde-deliver/                 # v0.7：D1–D5 交付内容与培训
│   │   ├── SKILL.md
│   │   ├── references/delivery-methods.md
│   │   └── assets/templates/        # 交付内容总览.md、场景交付说明.md、培训与使用指南.md
│   ├── fde-transfer/                # v0.7：E1–E5 客户移交
│   │   ├── SKILL.md
│   │   ├── references/transfer-methods.md
│   │   └── assets/templates/        # 客户移交总览.md、场景移交说明.md、内容维护与支持说明.md
│   └── fde-assets-archive/          # v0.7：F1–F7 资产归档
│       ├── SKILL.md
│       ├── references/              # archive-methods.md、workbuddy-asset-types.md、de-identification-rules.md
│       └── assets/templates/        # 资产包总览/清单、场景资产清单、复用指南、客户覆盖模板、MCP 指南、四份治理模板
└── tests/                           # 开发验收资产，不需安装
    ├── acceptance-matrix.md         # v0.6 十六测试 + 金样例 + v0.7 二十四用例 + fde-init 五用例 + 资产完整性检查
    └── fixtures/                    # v0.6 测试输入夹具
```

## 与设计文档的对应

| 设计文档章节 | 本项目落点 |
|---|---|
| v0.6 第 11 节 A1–A4 | [skills/fde-discovery-prepare/SKILL.md](skills/fde-discovery-prepare/SKILL.md) |
| v0.6 第 12 节 B1–B6 | [skills/fde-discovery-capture/SKILL.md](skills/fde-discovery-capture/SKILL.md) |
| v0.6 第 13 节 C1–C8 | [skills/fde-design-blueprint/SKILL.md](skills/fde-design-blueprint/SKILL.md) |
| v0.6 第 15.2 / 15.7 节 + v0.7 第 1.5 / 1.6 / 7.2 节 | [shared/execution-contract.md](shared/execution-contract.md) |
| v0.6 第 15.4 节 + v0.7 第 1.4 / 7.2 / 7.3 节 | [shared/merge-rules.md](shared/merge-rules.md) |
| v0.6 第 2.1 / 2.2 / 10.3 / 15.5 节 + v0.7 第 1.5 / 7.5 节 | [shared/questioning-rules.md](shared/questioning-rules.md) |
| v0.6 第 15.6 节 + v0.7 第 1.3 / 7.4 节 | [shared/quality-gates.md](shared/quality-gates.md) |
| v0.7 第 2 节（D1–D5） | [skills/fde-deliver/SKILL.md](skills/fde-deliver/SKILL.md) |
| v0.7 第 3 节（E1–E5） | [skills/fde-transfer/SKILL.md](skills/fde-transfer/SKILL.md) |
| v0.7 第 4 节（F1–F7） | [skills/fde-assets-archive/SKILL.md](skills/fde-assets-archive/SKILL.md) |
| 本项目新增，无上游设计章节（I1–I3） | [skills/fde-init/SKILL.md](skills/fde-init/SKILL.md) |
| v0.6 第 15.8–15.10 节 + v0.7 第 8–9 节 | [tests/acceptance-matrix.md](tests/acceptance-matrix.md) |
