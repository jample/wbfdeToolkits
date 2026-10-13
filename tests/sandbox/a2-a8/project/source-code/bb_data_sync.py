#!/usr/bin/env python3
"""蓝湾 CRM -> 蓝湾 BI 跟进报告同步脚本。

历史背景：由 2025 年外包商"恒讯软件"交付，合同中未明确源代码许可归属，
悦智能与蓝湾家居均未提供可复用授权证明。权利状态：未知。
"""
import os
import requests  # 第三方依赖，许可状态未登记

BLUEBAY_BI_ENDPOINT = "https://bi.bluebay-home.cn/api/v1/reports"  # 客户内网/域名常量
BI_TOKEN = os.environ.get("BLUEBAY_BI_TOKEN")  # 凭证引用


def sync_report(report: dict) -> bool:
    resp = requests.post(
        BLUEBAY_BI_ENDPOINT,
        json={"cust_no": report["BB_CUST_NO"], "payload": report},
        headers={"Authorization": f"Bearer {BI_TOKEN}"},
        timeout=10,
    )
    return resp.status_code == 200
