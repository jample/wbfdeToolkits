---
name: followup-report-builder
description: "根据拜访纪要生成跟进报告草稿（含待办负责人建议）。更新候选 v0.3-candidate：在正式资产 v0.2 三段式基础上合并客户项目增量（待办负责人建议、可选 CRM 回写、四段式输出），未经资产 Owner 评审，不覆盖 v0.2。"
version: v0.3-candidate
---

# followup-report-builder（更新候选 v0.3-candidate，未评审）

> 本文件是**更新候选**，不是正式资产。正式资产 v0.2 位于资产库 `asset-library/followup-report-builder/v0.2/`，本候选不覆盖、不替换它；与 v0.2 的关系（升级为新版本 / 合并 / 放弃）由资产 Owner 决定。

## 工作流（候选）
1. 读取拜访纪要文本；
2. 生成 ${report_section_titles}（默认四段：拜访结论 / 待办与负责人建议 / 风险与升级 / 下一步计划）跟进报告草稿；
3. ${sales_role_name} 确认待办负责人与日期后归档；
4. （可选）经确认的报告通过 ${crm_writeback_target} 写回客户 CRM（写回目标为客户覆盖变量）。

## 变量（由客户覆盖模板提供）
- `${sales_role_name}`：销售角色称谓（合成示例值："客户经理"）
- `${report_section_titles}`：报告分段标题（合成示例值：默认四段）
- `${crm_writeback_target}`：CRM 写回目标说明（合成示例值："CRM 跟进记录"）

## 人工边界（核心约束，不可作为覆盖变量删除）
- 待办负责人与日期 AI 只建议，必须由 ${sales_role_name} 确认后才生效；
- CRM 写回以人工确认为前提，不自动外发；
- 报告内容只基于纪要文本与已确认信息，不编造承诺。

## 来源
- 来源项目文件（受控引用）：`project/workbuddy/skills/followup-report-builder/SKILL.md`（客户版）+ 既有正式资产 v0.2
- 转换动作：参数化 + 合并增量（客户名、写回目标转为变量；v0.2 已确认的人工边界全部保留）
- 复用状态：待脱敏与评审
