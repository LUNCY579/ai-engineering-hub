#!/usr/bin/env python3
"""Validate the 117 tracked Markdown textbooks against their catalog."""
import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXPECTED = {"project": 107, "roadmap-module": 10}

def main() -> int:
    with (HERE / "catalog.csv").open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    counts = {k: 0 for k in EXPECTED}
    seen_paths = set()
    errors = []
    for row in rows:
        kind = row["kind"].strip().lower()
        if kind not in counts:
            errors.append(f"unknown kind: {kind}")
            continue
        counts[kind] += 1
        md_path = row["markdown"].strip()
        md = HERE / md_path
        if not md_path.startswith("markdown/") or not md_path.endswith(".md") or ".." in pathlib.PurePosixPath(md_path).parts:
            errors.append(f"invalid source path: {md_path}")
        elif not md.is_file():
            errors.append(f"missing textbook: {md_path}")
        if md_path in seen_paths:
            errors.append(f"duplicate textbook path: {md_path}")
        seen_paths.add(md_path)
    if counts != EXPECTED:
        errors.append(f"expected {EXPECTED} but counted {counts}")
    if len(seen_paths) != 117:
        errors.append(f"expected 117 unique paths; saw {len(seen_paths)}")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {len(rows)} books, 107 project volumes, 10 roadmap volumes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
