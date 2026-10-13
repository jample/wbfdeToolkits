---
name: customer-brief-summary
description: "汇总 CRM 客户资料与近期跟进记录，生成一页客户摘要，供销售人员人工确认。通用核心版本，由客户项目参数化而来。"
---

# customer-brief-summary（通用核心，参数化草稿）

## 工作流
1. 从客户 CRM 读取客户主档与最近 ${followup_lookback_days} 天跟进记录；
2. 按 ${brief_section_titles}（默认四段：基本概况 / 业务往来 / 关键联系人 / 风险提示）生成摘要；
3. 输出给 ${sales_role_name} 人工确认。

## 变量（由客户覆盖模板提供）
- `${sales_role_name}`：销售角色称谓（合成示例值："客户经理"）
- `${customer_data_root}`：客户资料根目录（合成示例值：`/crm/customers/`）
- `${brief_title}`：摘要抬头（合成示例值："客户摘要"）
- `${contact_role_levels}`：关键联系人分级（合成示例值："决策人/影响人/执行人"）
- `${followup_lookback_days}`：跟进回看天数（合成示例值：90）

## 人工边界（核心约束，不可作为覆盖变量删除）
- 摘要仅供内部使用；AI 不自动外发。
- 摘要内容只基于 CRM 真实记录，不得编造联系人或往来记录。

## 来源
- 来源项目文件（受控引用）：`project/workbuddy/skills/customer-brief-summary/SKILL.md`（v1.1）
- 转换动作：参数化（客户名称、目录、称谓、抬头转为变量；工作流与人工边界保留）
- 复用状态：待脱敏与评审
