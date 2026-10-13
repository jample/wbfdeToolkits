# SCN-INQ-SUMMARY 场景需求（蓝湾家居，合成夹具）

## 1. 场景概述
- 主体：客户经理（蓝湾家居内部称谓"客户管家"）
- 触发：蓝湾 CRM 中出现新询盘记录
- 起点：收到新询盘提醒
- 终点：客户经理确认一页客户摘要并决定是否跟进
- 业务结果：30 分钟内形成摘要，减少人工翻查

## 2. 主流程
1. 从蓝湾 CRM 拉取新询盘与客户主档；
2. 调用 `customer-brief-summary` Skill 生成一页摘要；
3. 客户经理人工确认摘要；
4. 确认后在 CRM 标记"已摘要"。

## 3. 人工边界
- 是否跟进由客户经理决定，AI 不自动承诺回复。

## 4. 依赖
- WorkBuddy Skill：`customer-brief-summary`（客户版，路径 `workbuddy/skills/customer-brief-summary/`）
