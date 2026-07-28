#!/usr/bin/env python3
"""Read-only completeness checks for portable Reezonly skill variants."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REFERENCE_NAMES = ("runtime-gate.md", "authoring-pipeline.md", "course-design.md", "block-catalog.md", "active-html.md")
PACKAGES = {
    "codex": ROOT / "codex" / "reezonly-course-authoring",
    "claude": ROOT / "claude-code" / "reezonly-course-authoring",
}


def normalized(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8").lower()).strip()


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def package_text(folder: Path) -> str:
    paths = [folder / "SKILL.md", *(folder / "references" / name for name in REFERENCE_NAMES)]
    return " ".join(normalized(path) for path in paths if path.is_file())


def validate_package(name: str, folder: Path, failures: list[str]) -> None:
    skill = folder / "SKILL.md"
    references = folder / "references"
    validator = folder / "scripts" / "validate_guidance.py"
    expected = [skill, validator, *(references / ref for ref in REFERENCE_NAMES)]
    for path in expected:
        require(path.is_file(), f"{name}: missing {path.relative_to(folder)}", failures)
    if not skill.is_file():
        return
    raw = skill.read_text(encoding="utf-8")
    require(raw.startswith("---\nname: reezonly-course-authoring\n"), f"{name}: portable frontmatter missing", failures)
    for ref in REFERENCE_NAMES:
        require(f"[{' '.join(ref[:-3].split('-')).replace('Runtime', 'runtime').replace('Authoring', 'authoring').replace('Course', 'course').replace('Block', 'block').replace('Active', 'active')}.md](references/{ref})" in raw or f"](references/{ref})" in raw, f"{name}: SKILL.md lacks direct link to {ref}", failures)
    forbidden = [path for path in folder.rglob("*") if path.is_file() and path.name.lower() in {"readme.md", "changelog.md"}]
    require(not forbidden, f"{name}: auxiliary README/CHANGELOG present", failures)
    if validator.is_file():
        result = subprocess.run([sys.executable, str(validator)], cwd=folder, capture_output=True, text=True)
        require(result.returncode == 0, f"{name}: package validator failed: {result.stdout}{result.stderr}", failures)


def main() -> int:
    failures: list[str] = []
    for name, folder in PACKAGES.items():
        validate_package(name, folder, failures)

    codex = PACKAGES["codex"]
    require((codex / "agents" / "openai.yaml").is_file(), "codex: agents/openai.yaml missing", failures)
    if (codex / "agents" / "openai.yaml").is_file():
        require("interface:" in (codex / "agents" / "openai.yaml").read_text(encoding="utf-8"), "codex: openai interface metadata missing", failures)
    require(not (PACKAGES["claude"] / "agents" / "openai.yaml").exists(), "claude: agents/openai.yaml must not be present", failures)

    for name, folder in PACKAGES.items():
        text = package_text(folder)
        for term in ("tools/list", "input/output schemas", "prepare_existing_course_authority", "delete_once", "preview_cleanup", "full_access", "authoritative absence", "not_found", "retryable:false", "nextaction"):
            require(term in text, f"{name}: missing core term {term}", failures)
        require("raw course text, or block content in tool arguments, journals, or reports" not in text, f"{name}: stale blanket educational-content prohibition", failures)
        require("учебный content разрешён только в точных опубликованных mutation-полях" in text, f"{name}: content mutation/audit boundary missing", failures)

    claude_skill = normalized(PACKAGES["claude"] / "SKILL.md")
    require("точное fully-qualified mcp tool name из фактически доступного каталога" in claude_skill, "claude: exact catalog-qualified name instruction missing", failures)
    require("не выдумывать mcp server prefix" in claude_skill and "mcp__" not in claude_skill, "claude: MCP prefix rule invalid", failures)

    lite = ROOT / "reezonly-course-authoring-lite.md"
    lite_text = normalized(lite)
    require(lite.is_file() and not lite.read_text(encoding="utf-8").startswith("---"), "lite: standalone metadata-free file missing", failures)
    for term in ("tools/list", "prepare_existing_course_authority", "delete_once", "authoritative absence", "retryable:false", "nextaction"):
        require(term in lite_text, f"lite: missing core term {term}", failures)

    if failures:
        print("Skill variant validation failed:", *[f"- {item}" for item in failures], sep="\n")
        return 1
    print("Skill variant validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
