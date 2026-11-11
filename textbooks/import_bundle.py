#!/usr/bin/env python3
"""Import the independently authored 117-book archive without changing lesson code."""
import argparse
import pathlib
import sys
import zipfile

PREFIX = "AI_Engineering_Hub_Textbooks/"
ALLOW = {".md", ".csv", ".json", ".pdf"}

def import_bundle(bundle: pathlib.Path, dest: pathlib.Path, source_only: bool = False):
    written = []
    with zipfile.ZipFile(bundle) as zf:
        bad = zf.testzip()
        if bad:
            raise ValueError(f"Corrupted archive entry: {bad}")
        members = [x for x in zf.infolist() if not x.is_dir()]
        md = [x for x in members if x.filename.startswith(PREFIX + "markdown/") and x.filename.endswith(".md")]
        pdf = [x for x in members if x.filename.startswith(PREFIX + "pdf/") and x.filename.endswith(".pdf")]
        if len(md) != 117 or len(pdf) != 117:
            raise ValueError(f"Unexpected textbook count: {len(md)} Markdown, {len(pdf)} PDF")
        targets = []
        for info in members:
            if not info.filename.startswith(PREFIX):
                raise ValueError(f"Unexpected root: {info.filename}")
            rel = pathlib.PurePosixPath(info.filename[len(PREFIX):])
            if rel.is_absolute() or ".." in rel.parts or not rel.parts or rel.suffix.lower() not in ALLOW:
                raise ValueError(f"Unsafe or unsupported entry: {info.filename}")
            if source_only and rel.suffix.lower() == ".pdf":
                continue
            targets.append((info, dest.joinpath(*rel.parts)))
        for info, target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(zf.read(info))
            written.append(target)
    return written

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=pathlib.Path)
    parser.add_argument("--source-only", action="store_true", help="Import editable Markdown and metadata; omit PDF binaries")
    args = parser.parse_args()
    target = pathlib.Path(__file__).resolve().parent
    files = import_bundle(args.bundle, target, args.source_only)
    print(f"Imported {len(files)} files into {target}")
if __name__ == "__main__":
    main()
