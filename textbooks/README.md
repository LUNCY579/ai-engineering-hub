# AI Engineering Hub · Independent Textbook Library

**117 individual textbooks**: 107 project companions + 10 books expanding the roadmap headings. Each has an editable Markdown source here; a separate PDF edition is distributed in the companion archive. Built from a verified inventory of the linked fork on 2026-11-10.

The original repository is credited and pinned in every book. Content is independently written: theory, diagrams as text pipelines, framework-neutral pseudocode, reading labs, ablations, benchmarks, numerical exercises, worked answers and glossary. **No project code was executed; detailed code-path verification remains a recommended next step.** See [AUDIT.md](AUDIT.md) for the discrepancy report.

## How to use this library
1. Start with the 10 roadmap module Markdown volumes (or the separately distributed PDFs) for foundations (the parent roadmap is also covered as a project companion).
2. Read beginner project books in any order; follow source links and reproduce a baseline.
3. Continue to intermediate and advanced topics and document test results separately from the suggested examples.
4. Edit Markdown if an upstream README or API changes, then regenerate PDFs. Do not blindly assume that historical installation commands still work.

## Directory layout
- `markdown/projects/{beginner,intermediate,advanced}/`: one editable original companion per actual fork project folder.
- `pdf/projects/{beginner,intermediate,advanced}/`: optional local PDFs after importing the separate PDF bundle.
- `markdown/roadmap-modules/`: 10 standalone foundation modules; `pdf/roadmap-modules/` can be imported locally.
- `CURRICULUM.md`: full linked course index.
- `AUDIT.md`: fork/upstream comparison and repository improvements.
- `catalog.csv`, `manifest.json`: machine-readable inventory.
- `SOURCE_AND_LICENSE.md`: credits and reuse considerations.

## Scope limits
These are compact instructional textbooks, not transcriptions or fully source-verified tutorials. The source directory names, fork README descriptions, comparison history and a set of selected README/file checks were inspected; every project was **not** executed or dependency-audited. All proposed laboratory work is labeled as such.

## Repository integration (November 2026)
All **117 editable Markdown books** (107 project companions plus 10 roadmap modules) and their `manifest.json` are versioned in this directory. Use [CURRICULUM.md](CURRICULUM.md) to browse each book.

The **117 PDF editions** are available in the separately supplied companion ZIP, not committed into Git history. To add those PDFs to a local clone without touching the tracked Markdown, run:

```bash
python textbooks/import_bundle.py /path/to/AI_Engineering_Hub_117_Textbooks.zip --pdf-only
```

These books are independently authored study companions and should not be confused with verified executable tutorials. See [AUDIT.md](AUDIT.md) and [SOURCE_AND_LICENSE.md](SOURCE_AND_LICENSE.md).
