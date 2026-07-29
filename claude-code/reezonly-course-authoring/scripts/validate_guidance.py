#!/usr/bin/env python3
"""Read-only structural and safety checks for this portable Claude Code skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = {"skill": ROOT / "SKILL.md", **{name: ROOT / "references" / f"{name}.md" for name in ("runtime-gate", "authoring-pipeline", "course-design", "block-catalog", "active-html")}}


def text(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8").lower()).strip()


def main() -> int:
    failures: list[str] = []
    for name, path in FILES.items():
        if not path.is_file():
            failures.append(f"missing {name}")
    if not failures:
        skill = text(FILES["skill"])
        joined = " ".join(text(path) for path in FILES.values())
        for term in ("tools/list", "prepare_existing_course_authority", "delete_once", "preview_cleanup", "full_access", "returned server selector", "exactly one direct", "authoritative absence", "not_found", "retryable:false", "nextaction"):
            if term not in joined:
                failures.append(f"missing safety/runtime term: {term}")
        if "точное fully-qualified mcp tool name из фактически доступного каталога" not in skill:
            failures.append("missing exact catalog-qualified Claude tool-name rule")
        if "не выдумывать mcp server prefix" not in skill or "mcp__" in skill:
            failures.append("Claude MCP prefix rule invalid")
        structural = " ".join(
            text(FILES[name]) for name in ("skill", "runtime-gate", "authoring-pipeline")
        )
        for term in (
            "canonical structural delete",
            "lesson_authoring_delete_entity",
            "preview_cleanup",
            "delete_once",
            "parent chain",
            "action",
            "entityid",
            "authoritative absence",
            "unknown",
            "nextaction",
            "delete_course",
            "course-index",
            "client cascade",
            "ownership/grant/selector",
            "module/lesson/page/block",
        ):
            if term not in structural:
                failures.append(f"missing canonical structural-delete term: {term}")
        if "ровно один dispatch" not in structural and "exactly once" not in structural:
            failures.append("canonical structural delete must require one dispatch")
        catalog = text(FILES["block-catalog"])
        for term in (
            "webinar11",
            "integration13",
            "current rich-media schema",
            "currently required `type` and `duration`",
            "before dispatch",
            "typed canonical readback",
            "opaque extensions",
            "copy server-owned opaque extensions into writes",
            "authority",
            "traverse",
            "project",
            "log",
            "typed drift/error",
            "guessed payload adaptation",
        ):
            if term not in catalog:
                failures.append(f"missing Webinar opaque-safety term: {term}")
        if "raw course text, or block content in tool arguments, journals, or reports" in joined:
            failures.append("stale blanket educational-content tool-argument prohibition")
    if failures:
        print("Guidance validation failed:", *[f"- {item}" for item in failures], sep="\n")
        return 1
    print("Guidance validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
