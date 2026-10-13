# SCN-VISIT-PREP 场景需求（蓝湾家居，合成夹具）

## 1. 场景概述
- 主体：客户经理王晓琳等一线销售
- 触发：拜访日程前一天 17:00
- 起点：读取蓝湾 CRM 客户资料与历史跟进
- 终点：生成"五段式拜访简报"，销售总监陈立群审批通过后下发
- 业务结果：拜访准备时间从 2 小时降至 30 分钟

## 2. 主流程
1. 调用 `customer-brief-summary` Skill 汇总客户资料（与 SCN-INQ-SUMMARY 共用）；
2. 调用拜访简报 Prompt（`workbuddy/prompts/visit-brief-prompt.md`）生成五段式简报；
3. 客户经理核对；销售总监审批（蓝湾策略：拜访简报必须总监审批）；
4. 简报存入客户资料目录 `/bluebay/crm/customers/<客户编号>/visits/`。

## 3. 人工边界
- 价格与折扣信息只展示、不生成承诺；
- 简报未经总监审批不得发送给客户。

## 4. 依赖
- Skill `customer-brief-summary`；Prompt `visit-brief-prompt`；蓝湾 CRM MCP 集成（`integration/mcp-config-bluebay.md`）
