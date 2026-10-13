---
name: customer-brief-summary
description: "汇总蓝湾家居 CRM 客户资料，生成一页客户摘要。被 SCN-INQ-SUMMARY 与 SCN-VISIT-PREP 两个场景明确引用。"
---

# customer-brief-summary（蓝湾家居客户版 v1.1）

## 工作流
1. 从蓝湾 CRM 读取客户主档与最近 90 天跟进记录；
2. 按"基本概况 / 业务往来 / 关键联系人 / 风险提示"四段生成摘要；
3. 输出给客户经理（蓝湾内部称谓"客户管家"）人工确认。

## 客户专属点
- 摘要存放目录：`/bluebay/crm/customers/<客户编号>/briefs/`
- 摘要抬头固定写"蓝湾家居客户摘要"
- 关键联系人段落需列出蓝湾定义的"决策人/影响人/执行人"三级角色

## 人工边界
- 摘要仅供内部使用；AI 不自动外发。
