#!/usr/bin/env python3
"""Offline structural checks for the portable skill; Python 3.9+, no packages."""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED = (
    "SKILL.md", "README.md", "agents/openai.yaml",
    "references/visual-system.md", "references/information-patterns.md",
    "references/platforms.md", "references/interaction-motion.md",
    "references/evaluation.md", "references/user-control.md",
    "references/sources.md", "references/design-case-research.md",
    "research/design-method-evolution.md", "research/apple-hig-reading-map.md",
)


def anchors(text):
    seen = {}
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        heading = re.sub(r"[^\w\s\-]", "", heading.lower()).replace(" ", "-")
        suffix = seen.get(heading, 0)
        seen[heading] = suffix + 1
        result.add(heading if not suffix else f"{heading}-{suffix}")
    return result


def check(root, forbidden=()):
    root = root.resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    entry = root / "SKILL.md"
    if entry.is_file():
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            errors.append("SKILL.md: missing YAML frontmatter")
        else:
            for field in ("name", "description"):
                if not re.search(rf"^{field}:\s*\S", match[1], re.M):
                    errors.append(f"SKILL.md: missing {field}")
    files = []
    links = 0
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in (".git", "__pycache__") for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f"Symlink must be replaced with a bundled file: {relative}")
            continue
        if not path.is_file():
            continue
        files.append(path)
        if path.suffix not in (".md", ".yaml", ".json", ".txt"):
            continue
        text = path.read_text(encoding="utf-8")
        for value in forbidden:
            if value and value in text:
                errors.append(f"Forbidden private marker in {relative}")
        # These patterns detect local file references, not all personal information.
        if re.search(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\|file://)", text):
            errors.append(f"Machine-specific path in {relative}")
        if path.suffix != ".md":
            continue
        for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            href = href.strip().strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme in ("https", "http", "mailto"):
                continue
            if parsed.scheme or parsed.netloc:
                errors.append(f"Nonportable link in {relative}: {href}")
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            links += 1
            if not target.is_relative_to(root):
                errors.append(f"Link leaves package in {relative}: {href}")
            elif not target.exists():
                errors.append(f"Missing link target in {relative}: {href}")
            elif parsed.fragment and target.suffix == ".md":
                fragment = unquote(parsed.fragment)
                if fragment not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"Missing heading in {relative}: {href}")
    return files, links, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--forbid", action="append", default=[], help="Private marker to reject (not printed)")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error("root must be a skill directory")
    files, links, errors = check(root, args.forbid)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"{'FAIL' if errors else 'PASS'}: {len(files)} files, {links} local links, {len(errors)} errors")
    print("Scope: file structure only; web availability, privacy and behavior need separate review.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
