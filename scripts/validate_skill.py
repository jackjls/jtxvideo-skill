#!/usr/bin/env python3
"""Validate a Codex skill folder for required structure and metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("Missing dependency: PyYAML. Install with `python3 -m pip install PyYAML`.") from exc


NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")


def load_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md frontmatter must be closed with ---")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise ValueError("SKILL.md frontmatter must be a mapping")
    return data


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_skill.py <skill-folder>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    skill_md = root / "SKILL.md"
    openai_yaml = root / "agents" / "openai.yaml"

    errors: list[str] = []
    if not root.is_dir():
        errors.append(f"Skill folder not found: {root}")
    if not skill_md.is_file():
        errors.append("Missing SKILL.md")
    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    try:
        frontmatter = load_frontmatter(skill_md)
    except Exception as exc:
        errors.append(str(exc))
        frontmatter = {}

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not NAME_RE.match(name):
        errors.append("Frontmatter `name` must be lowercase hyphen-case, max 63 chars")
    if not isinstance(description, str) or len(description.strip()) < 80:
        errors.append("Frontmatter `description` must be a descriptive string")
    extra_keys = set(frontmatter) - {"name", "description"}
    if extra_keys:
        errors.append(f"Frontmatter has non-standard keys: {', '.join(sorted(extra_keys))}")

    if not openai_yaml.is_file():
        errors.append("Missing recommended agents/openai.yaml")
    else:
        try:
            yaml.safe_load(openai_yaml.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid agents/openai.yaml: {exc}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print(f"[OK] Skill is valid: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

