# 共享资产使用说明

| 元数据 | 值 |
|---|---|
| 所属资产包 | pkg-sales-side-scenes-v1-candidate |
| 编制日期 | 2026-09-14 |
| 复用状态 | 待脱敏与评审 |

## 共享资产清单

| Asset ID | 名称 | 路径 | 引用场景 | 共享依据 |
|---|---|---|---|---|
| AST-SKILL-CBS-001 | customer-brief-summary | `../workbuddy/skills/customer-brief-summary/SKILL.md` | SCN-INQ-SUMMARY、SCN-VISIT-PREP | 两场景需求文档均明确声明调用本 Skill（非"可能以后共用"） |

## 引用方式
- 场景 `资产清单.md` 通过相对路径引用本目录文件；共享文件只保存一份，不在场景目录复制副本。
- 共享资产发生修改时，须检查全部引用场景的清单与复用指南，但不自动修改场景结论。

## 引用场景清单
- `../../scenes/SCN-INQ-SUMMARY/资产清单.md`
- `../../scenes/SCN-VISIT-PREP/资产清单.md`
