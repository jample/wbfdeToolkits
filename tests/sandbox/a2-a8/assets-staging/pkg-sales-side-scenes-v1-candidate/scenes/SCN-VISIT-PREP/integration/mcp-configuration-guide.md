# MCP 配置说明

| 元数据 | 值 |
|---|---|
| 能力名称 | CRM 读写集成（客户主档/跟进/简报回写） |
| 关联场景 | SCN-VISIT-PREP（步骤 1 读取、步骤 4 回写）；SCN-INQ-SUMMARY 复用参考 |
| 所属资产包 | pkg-sales-side-scenes-v1-candidate |
| 内容版本 | 通用化草稿 |
| 编制日期 | 2026-09-14 |
| 复用状态 | 待脱敏与评审 |

> 本说明只描述业务语义、配置变量和映射方法；不含客户地址、Token、账号、真实字段或真实数据。来源项目文件（受控引用）：`project/integration/mcp-config-bluebay.md`，转换动作：参数化+合成重制。

## 1. 业务用途

| 字段 | 内容 |
|---|---|
| 服务哪个场景步骤 | SCN-VISIT-PREP 步骤 1（读取客户资料与历史跟进）、步骤 4（回写审批后简报）；SCN-INQ-SUMMARY 步骤 1 可参考 |
| WorkBuddy 需要取得/提交什么信息 | 取得：客户主档、近期跟进；提交：经审批的拜访简报 |

## 2. 工具清单

| 工具名称 | 意图 | 主要输入 | 主要输出 | 人工边界 |
|---|---|---|---|---|
| `get_customer_profile` | 读取客户主档 | 客户编号 | 客户主档语义对象 | 只读 |
| `list_recent_followups` | 读取近期跟进 | 客户编号、回看天数 | 跟进记录列表 | 只读 |
| `write_visit_brief` | 回写拜访简报 | 客户编号、简报内容 | 回写结果 | 仅写入经人工审批的简报；不自动外发 |

## 3. 数据含义

| 业务对象 | 字段语义（语义变量，非客户真实 Schema） | 说明 |
|---|---|---|
| 客户主档 | `${f_customer_id}` 客户编号、`${f_customer_name}` 客户名称、`${f_annual_amount}` 年采购额、`${f_last_visit_date}` 最近拜访日期 | 字段名为业务语义变量，部署时映射到客户真实字段 |

## 4. 配置变量

| 变量 | 含义 | 必填/可选 | 合成示例值 | 说明 |
|---|---|---|---|---|
| 服务地址占位 `${crm_mcp_base_url}` | CRM MCP 服务地址 | 必填 | `https://crm.example.internal/mcp/v1` | 客户部署时填写真实地址；禁止把真实域名写入模板 |
| 认证方式 `${crm_token_env_var}` | Token 环境变量名 | 必填 | `CRM_MCP_TOKEN` | 只写引用方式（环境变量名），不写任何明文凭证 |
| 租户 `${crm_tenant}` | 租户标识 | 可选 | `tenant-demo` | 客户部署时填写 |
| 超时/范围 `${crm_timeout_seconds}` | 请求超时 | 可选 | `10` | — |

## 5. 映射说明

| 场景输入 | 对应工具/参数 | 工具结果 | 场景输出 | 可调整点 |
|---|---|---|---|---|
| 客户编号 | `get_customer_profile` / `${f_customer_id}` | 客户主档 | 简报"客户近况"段 | 字段映射 |
| 客户编号+回看天数 | `list_recent_followups` | 跟进列表 | 简报"沟通要点"段 | 回看天数 |
| 审批后简报 | `write_visit_brief` | 回写确认 | 步骤 4 归档记录 | 触发条件固定为"人工审批后" |

## 6. 客户覆盖

| 客户需要填写什么 | 说明 |
|---|---|
| 服务地址、租户、环境变量名、字段映射 | 见 `configuration-templates/crm-mcp.template.yaml` 与本文件 §4 |

| 禁止放入通用模板的内容 | 原因 |
|---|---|
| 真实域名、Token/账号、真实字段 Schema、真实调用样例与日志 | 违反客户隔离规则 |

## 7. 使用限制

| 字段 | 内容 |
|---|---|
| 只读/可编辑说明 | `get_*`/`list_*` 只读；`write_visit_brief` 仅在人工审批后调用 |
| 权限要求 | 客户侧最小权限账号；权限范围待客户 IT 确认 |
| 错误处理 | 读取失败→提示人工补录，不编造；回写失败→保留简报并重试由人触发 |
| 不适用情形 | 客户无 CRM API 或禁止外部系统写入时 |

## 8. 合成示例

> 以下为合成配置片段，不含客户地址、Token、账号、字段或真实数据。

```yaml
# 合成配置示例（占位变量，非真实配置）
server:
  base_url: "${crm_mcp_base_url}"     # 例：https://crm.example.internal/mcp/v1
  tenant: "${crm_tenant}"             # 例：tenant-demo
auth:
  type: bearer
  token_env_var: "${crm_token_env_var}"  # 例：CRM_MCP_TOKEN；只引用环境变量名
tools:
  - name: get_customer_profile
    input_mapping:
      customer_id: "${f_customer_id}"
  - name: list_recent_followups
    input_mapping:
      customer_id: "${f_customer_id}"
      lookback_days: "${followup_lookback_days}"
  - name: write_visit_brief
    guard: "仅在人工审批通过后调用"
timeout_seconds: "${crm_timeout_seconds}"
```

| 权限或用途待确认项 | 状态 |
|---|---|
| 回写工具的客户侧权限范围 | 待评审 |
