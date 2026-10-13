# examples/ 说明

本目录是 `fde-design-blueprint` 的跨境电商示例包。来源约定遵循设计文档 Simple v0.6 第 10.4 节：

- **业务内容**来自跨境电商既有访谈、观察和确认需求原件（`fde跨境电商/02_需求探究/` 与 `03_场景设计/` 下的 confirmed 文件及联合设计访谈记录）。
- 各文件中的表格内容是**按 Simple v0.6 模板重组后的教学表达**，并非声称原文件逐字如此。
- **Hyp-sys 系统内容**直接采用 `fde跨境电商/03_场景设计/Hyp-sys.md` 作为本次仿真企业环境；用 Hyp-sys 展开的技术映射属于**本次补充设计**，不表示原项目已经完成技术接入。原实例蓝图 §4 把系统列为“概念来源、不接入”。
- 示例中的对话与“FDE 补充”是示范表达，不是新取得的客户确认；实际执行中必须记录真实收到的补充。

## 文件清单

| 文件 | 角色 | 内容来源 |
|---|---|---|
| `design-input.md` | 设计讨论输入实例（可选输入） | 业务内容来自原件 `fde跨境电商/03_场景设计/scene-interviews/scenes-interviews.md`（`WKS-DESIGN-SIM-001`）；按 `templates/design-input.md` 重组的教学表达 |
| `system-context-input.md` | 系统上下文输入实例（可选输入） | 直接采用 `fde跨境电商/03_场景设计/Hyp-sys.md` 仿真环境（ChannelHub/SalesCRM/ProductCatalogLite）；Hyp-sys 展开的技术部分属本次补充设计；按 `templates/system-context-input.md` 重组 |
| `knowledge-rules-input.md` | 知识与规则输入实例（可选输入） | 业务规则来自既有访谈原件（销售访谈 `SALES-02/03`、任务回放）与确认需求；按 `templates/knowledge-rules-input.md` 重组的教学表达 |
| `scene-blueprint.md` | 蓝图输出实例（主要输出） | 业务流程与人机边界来自原件 `fde跨境电商/03_场景设计/confirmed/scenes/SCN-INQUIRY-TRIAGE/scene-blueprint.md`；系统映射部分来自 Hyp-sys（本次补充设计）；按 `templates/scene-blueprint.md` 重组的教学表达 |
| `dialogue-walkthrough.md` | 连续对话缩影 | 基于设计文档第 6.7 节和第 14.1/14.2 节轮次 6–9 编写；示范对话，非新确认 |
