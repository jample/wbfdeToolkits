#!/usr/bin/env python3
"""Run repeatable, spec-driven functional smoke checks for the document Skills.

The Skills are prompts/document contracts rather than executable business code.  This
runner therefore checks the observable contract that can be verified locally: package
completeness, routing and safety rules in SKILL.md, required output sections, and the
committed conversation-simulation artefacts under tests/sandbox/.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SANDBOX = ROOT / "tests" / "sandbox"


class Runner:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passes = 0

    def check(self, condition: bool, message: str) -> None:
        if condition:
            self.passes += 1
        else:
            self.failures.append(message)

    def file(self, relative: str) -> Path:
        return ROOT / relative

    def run(self) -> int:
        self.package_checks()
        self.skill_checks()
        self.output_contract_checks()
        self.simulation_checks()
        total = self.passes + len(self.failures)
        print(f"functional smoke checks: {self.passes}/{total} passed")
        if self.failures:
            print("failures:")
            for failure in self.failures:
                print(f"- {failure}")
            return 1
        return 0

    def package_checks(self) -> None:
        expected = {
            "fde-init": (
                "templates/项目总览.md",
                "templates/交付计划.md",
                "examples/项目总览.md",
                "examples/dialogue-walkthrough.md",
                "references/methods.md",
            ),
            "fde-discovery-prepare": (
                "templates/访前准备.md",
                "templates/business-background-input.md",
                "examples/访前准备.md",
                "references/methods.md",
            ),
            "fde-discovery-capture": (
                "templates/角色与场景总览.md",
                "templates/scene-requirement.md",
                "templates/interview-input.md",
                "templates/task-observation-input.md",
                "examples/角色与场景总览.md",
                "examples/scene-requirement.md",
                "references/methods.md",
            ),
            "fde-design-blueprint": (
                "templates/scene-blueprint.md",
                "templates/design-input.md",
                "templates/system-context-input.md",
                "templates/knowledge-rules-input.md",
                "examples/scene-blueprint.md",
                "references/methods.md",
            ),
            "fde-deliver": (
                "assets/templates/交付内容总览.md",
                "assets/templates/场景交付说明.md",
                "assets/templates/培训与使用指南.md",
                "references/delivery-methods.md",
            ),
            "fde-transfer": (
                "assets/templates/客户移交总览.md",
                "assets/templates/场景移交说明.md",
                "assets/templates/内容维护与支持说明.md",
                "references/transfer-methods.md",
            ),
            "fde-assets-archive": (
                "assets/templates/资产包总览.md",
                "assets/templates/资产包清单.md",
                "assets/templates/场景资产清单.md",
                "assets/templates/场景复用指南.md",
                "assets/templates/客户覆盖模板.md",
                "assets/templates/培训材料模板.md",
                "assets/templates/mcp-configuration-guide.md",
                "assets/templates/来源与转换追溯.md",
                "assets/templates/客户隔离检查.md",
                "assets/templates/权利与复用边界.md",
                "assets/templates/资产包评审记录.md",
                "references/archive-methods.md",
                "references/workbuddy-asset-types.md",
                "references/de-identification-rules.md",
            ),
        }
        for name, files in expected.items():
            skill = SKILLS / name
            self.check((skill / "SKILL.md").is_file(), f"{name}: SKILL.md missing")
            for relative in files:
                self.check((skill / relative).is_file(), f"{name}: missing {relative}")

    def skill_checks(self) -> None:
        required = {
            "fde-init": (
                ("00_项目总览/项目总览.md", "uses the scaffold marker"),
                ("不覆盖", "never overwrites existing non-empty files"),
                ("待补", "marks unknowns instead of inventing facts"),
                ("幂等", "stays idempotent"),
                ("重复执行", "deduplicates repeated runs"),
            ),
            "fde-discovery-prepare": (
                ("最多", "limits directed questions"),
                ("假设", "marks hypotheses"),
                ("不补造 KPI", "does not invent metrics"),
                ("01_预检/访前准备.md", "writes the preparation output"),
            ),
            "fde-discovery-capture": (
                ("冲突并列", "keeps conflicting role statements"),
                ("SCREAMING-KEBAB-CASE", "uses stable scene IDs"),
                ("重复执行同一输入", "deduplicates repeated inputs"),
                ("02_需求探究", "writes the capture outputs"),
            ),
            "fde-design-blueprint": (
                ("用户动作", "separates human and AI actions"),
                ("不虚构系统", "does not invent integrations"),
                ("需求追溯", "keeps requirement traceability"),
                ("自动合并", "protects against overreach requests"),
                ("场景间承接", "supports upstream/downstream handoff"),
            ),
            "fde-deliver": (
                ("真实路径", "requires real content paths"),
                ("共享", "deduplicates shared content"),
                ("三类角色", "creates role-based training"),
                ("客户确认", "limits confirmation scope"),
                ("06_交付与培训", "writes the delivery outputs"),
            ),
            "fde-transfer": (
                ("权利不清", "blocks unclear rights"),
                ("文档已生成/材料已发", "does not infer receipt"),
                ("逐场景", "supports partial transfer"),
                ("触发条件", "uses trigger-based responsibilities"),
                ("条件接收", "supports conditional receipt"),
            ),
            "fde-assets-archive": (
                ("独立资产暂存目录", "isolates the asset output"),
                ("不复制", "excludes unsafe source files"),
                ("shared/", "deduplicates shared assets"),
                ("参数化", "parameterizes customer values"),
                ("不覆盖已有正式资产", "protects formal assets"),
                ("仅分析", "supports analysis-only mode"),
            ),
        }
        for name, needles in required.items():
            skill_dir = SKILLS / name
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            # Detailed execution rules live in references/ for the v0.7 packages.
            for reference in (skill_dir / "references").glob("*.md"):
                text += "\n" + reference.read_text(encoding="utf-8")
            for needle, description in needles:
                self.check(needle in text, f"{name}: {description} rule missing ({needle})")
            frontmatter = text.split("---", 2)
            self.check(
                len(frontmatter) == 3 and re.search(r"^name:\s*\S+", frontmatter[1], re.M),
                f"{name}: invalid frontmatter",
            )

    def output_contract_checks(self) -> None:
        contracts = {
            "skills/fde-init/templates/项目总览.md": ("## 1.", "## 3.", "## 5.", "## 6."),
            "skills/fde-init/templates/交付计划.md": ("## 1.", "## 2.", "## 5."),
            "skills/fde-discovery-prepare/templates/访前准备.md": ("## 1.", "## 6.", "6.2", "6.3"),
            "skills/fde-discovery-capture/templates/角色与场景总览.md": ("## 1.", "## 6."),
            "skills/fde-discovery-capture/templates/scene-requirement.md": ("## 1.", "## 8."),
            "skills/fde-design-blueprint/templates/scene-blueprint.md": ("## 1.", "## 8.", "### 8.1", "### 8.2", "### 8.3"),
            "skills/fde-deliver/assets/templates/交付内容总览.md": tuple(f"## {i}." for i in range(1, 9)),
            "skills/fde-deliver/assets/templates/场景交付说明.md": tuple(f"## {i}." for i in range(1, 12)),
            "skills/fde-deliver/assets/templates/培训与使用指南.md": tuple(f"## {i}." for i in range(1, 10)),
            "skills/fde-transfer/assets/templates/客户移交总览.md": tuple(f"## {i}." for i in range(1, 10)),
            "skills/fde-transfer/assets/templates/场景移交说明.md": tuple(f"## {i}." for i in range(1, 10)),
            "skills/fde-transfer/assets/templates/内容维护与支持说明.md": tuple(f"## {i}." for i in range(1, 8)),
            "skills/fde-assets-archive/assets/templates/资产包总览.md": tuple(f"## §{i}" for i in range(1, 9)),
            "skills/fde-assets-archive/assets/templates/资产包清单.md": ("## 1.", "## 2.", "## 3.", "## 4."),
            "skills/fde-assets-archive/assets/templates/场景资产清单.md": ("## 1.", "## 2.", "## 3.", "## 4."),
            "skills/fde-assets-archive/assets/templates/场景复用指南.md": tuple(f"## {i}." for i in range(1, 7)),
            "skills/fde-assets-archive/assets/templates/客户覆盖模板.md": tuple(f"## {i}." for i in range(1, 6)),
            "skills/fde-assets-archive/assets/templates/客户隔离检查.md": ("## 1.", "## 2."),
            "skills/fde-assets-archive/assets/templates/权利与复用边界.md": ("## 1.", "## 2.", "## 3."),
            "skills/fde-assets-archive/assets/templates/来源与转换追溯.md": ("## 1.", "## 2."),
            "skills/fde-assets-archive/assets/templates/资产包评审记录.md": ("## 1.", "## 2.", "## 3."),
        }
        for relative, headings in contracts.items():
            text = self.file(relative).read_text(encoding="utf-8")
            for heading in headings:
                self.check(heading in text, f"{relative}: required section missing ({heading})")

    def simulation_checks(self) -> None:
        # Existing committed artefacts are conversation-simulation evidence, not runtime output.
        expected = {
            "I1": "sandbox/i1/00_项目总览/项目总览.md",
            "P1": "sandbox/p1/01_预检/访前准备.md",
            "P2": "sandbox/p2/01_预检/访前准备.md",
            "C1": "sandbox/chain/02_需求探究/scenes/SCN-INQUIRY-INTAKE/scene-requirement.md",
            "C2": "sandbox/c2/02_需求探究/scenes/SCN-INQUIRY-TRIAGE/scene-requirement.md",
            "B1": "sandbox/chain/03_场景设计/scenes/SCN-INQUIRY-INTAKE/scene-blueprint.md",
            "D1": "sandbox/chain/06_交付与培训/交付内容总览.md",
            "T1": "sandbox/chain/07_支持移交归档/客户移交总览.md",
            "A1": "sandbox/assets-staging",
            "X4": "sandbox/retest-x4/02_需求探究/scenes/SCN-INQUIRY-TRIAGE/scene-requirement.md",
            "X6": "sandbox/x6/project/02_需求探究/scenes/SCN-INQUIRY-TRIAGE/scene-requirement.md",
        }
        for case, relative in expected.items():
            path = SANDBOX / relative.removeprefix("sandbox/")
            self.check(path.exists(), f"{case}: simulation artefact missing ({relative})")

        # A1 is intentionally analysis-only: the sandbox must remain empty.
        assets_staging = SANDBOX / "assets-staging"
        self.check(
            assets_staging.is_dir() and not any(assets_staging.iterdir()),
            "A1/A9: analysis-only sandbox unexpectedly contains copied assets",
        )

        # X6 must show that the oversized bundle was narrowed and the untouched range was stated.
        x6_overview = SANDBOX / "x6/project/02_需求探究/角色与场景总览.md"
        if x6_overview.exists():
            text = x6_overview.read_text(encoding="utf-8")
            self.check("已读/未读范围" in text, "X6: read/unread scope not recorded")
            self.check("未静默截断" in text, "X6: silent truncation guard not recorded")

        # The transfer artefact must not claim both aggregate receipt and pre-receipt in one scope.
        transfer = SANDBOX / "t3-t6/07_支持移交归档/客户移交总览.md"
        if transfer.exists():
            text = transfer.read_text(encoding="utf-8")
            metadata = re.search(r"\| 交付状态 \| ([^|]+)\|", text)
            scope = re.search(r"\| 交付状态 \| ([^|]+)\|", text[text.find("## 1."):])
            if metadata and scope:
                metadata_state = metadata.group(1).strip().split("（", 1)[0]
                scope_state = scope.group(1).strip().split("（", 1)[0]
                self.check(
                    metadata_state == scope_state,
                    "T3/T5: transfer overview has inconsistent aggregate and scope delivery states",
                )


if __name__ == "__main__":
    sys.exit(Runner().run())
