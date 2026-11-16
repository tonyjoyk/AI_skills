#!/usr/bin/env python3
"""Create a new skill from the template and add it to the README map.

Usage:
  python3 scripts/new_skill.py <skill-name> "<Category>" "<one-line summary>"

Example:
  python3 scripts/new_skill.py poster-maker "Documents and visuals" "Design a clear one-page poster."
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

if len(sys.argv) != 4:
    sys.exit(__doc__)

name, category, summary = sys.argv[1:]
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
    sys.exit("Skill name must be lowercase words joined by hyphens, e.g. poster-maker")

target = ROOT / "skills" / name
if target.exists():
    sys.exit(f"skills/{name} already exists")

template = (ROOT / "templates" / "SKILL.md").read_text(encoding="utf-8")
title = name.replace("-", " ").capitalize()
text = (
    template.replace("{{name}}", name)
    .replace("{{title}}", title)
    .replace("{{category}}", category)
    .replace("{{summary}}", summary.replace('"', '\\"'))
)
target.mkdir(parents=True)
(target / "SKILL.md").write_text(text, encoding="utf-8")
print(f"Created skills/{name}/SKILL.md")

subprocess.run([sys.executable, str(ROOT / "scripts" / "build_index.py")], check=True)
print("Next: fill in the description and steps in the new SKILL.md.")
