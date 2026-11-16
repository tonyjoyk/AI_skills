#!/usr/bin/env python3
"""Rebuild the skills map in README.md from each skills/*/SKILL.md frontmatter.

Usage:
  python3 scripts/build_index.py          # rewrite README.md
  python3 scripts/build_index.py --check  # exit 1 if README.md is out of date

No dependencies. Reads: name, description, metadata.summary, metadata.category.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
START, END = "<!-- SKILLS:START -->", "<!-- SKILLS:END -->"

# Display order. Any other category is listed after these, alphabetically.
CATEGORY_ORDER = [
    "Writing",
    "Documents and visuals",
    "Product and delivery",
    "Meetings and admin",
    "Creative",
]


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1].replace('\\"', '"')
    return v


def frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        sys.exit(f"Missing frontmatter: {path}")
    data, meta, in_meta = {}, {}, False
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("metadata:"):
            in_meta = True
            continue
        key, _, val = line.strip().partition(":")
        if in_meta and line.startswith((" ", "\t")):
            meta[key] = unquote(val)
        else:
            in_meta = False
            data[key] = unquote(val)
    data["metadata"] = meta
    return data


def first_sentence(text: str) -> str:
    return re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]


def build() -> str:
    rows = {}
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        fm = frontmatter(skill_md)
        folder = skill_md.parent.name
        name = fm.get("name") or folder
        if name != folder:
            sys.exit(f"name '{name}' must match folder '{folder}'")
        meta = fm["metadata"]
        summary = meta.get("summary") or first_sentence(fm.get("description", ""))
        category = meta.get("category") or "Other"
        rows.setdefault(category, []).append((name, summary))

    order = CATEGORY_ORDER + sorted(c for c in rows if c not in CATEGORY_ORDER)
    total = sum(len(v) for v in rows.values())
    out = [START, "", f"**{total} skills.** Click a name to open it.", ""]
    for cat in order:
        if cat not in rows:
            continue
        out += [f"### {cat}", "", "| Skill | What it does |", "|---|---|"]
        for name, summary in rows[cat]:
            out.append(f"| [`{name}`](skills/{name}/SKILL.md) | {summary} |")
        out.append("")
    out.append(END)
    return "\n".join(out)


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        sys.exit(f"README.md needs {START} and {END} markers")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), build(), readme, flags=re.S)
    if "--check" in sys.argv:
        if new != readme:
            sys.exit("README.md skills map is out of date. Run: python3 scripts/build_index.py")
        print("README.md is up to date.")
        return
    README.write_text(new, encoding="utf-8")
    print("README.md skills map updated.")


if __name__ == "__main__":
    main()
