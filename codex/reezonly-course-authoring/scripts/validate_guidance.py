#!/usr/bin/env python3
"""Read-only structural and safety checks for this portable Codex skill."""

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
        joined = " ".join(text(path) for path in FILES.values())
        required = ("tools/list", "input/output schemas", "prepare_existing_course_authority", "delete_once", "preview_cleanup", "full_access", "returned server selector", "exactly one direct", "execute_cleanup", "authoritative absence", "not_found", "retryable:false", "nextaction")
        for term in required:
            if term not in joined:
                failures.append(f"missing safety/runtime term: {term}")
        if "raw course text, or block content in tool arguments, journals, or reports" in joined:
            failures.append("stale blanket educational-content tool-argument prohibition")
        if "учебный content разрешён только в точных опубликованных mutation-полях" not in joined:
            failures.append("missing exact mutation-field content boundary")
    if failures:
        print("Guidance validation failed:", *[f"- {item}" for item in failures], sep="\n")
        return 1
    print("Guidance validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
