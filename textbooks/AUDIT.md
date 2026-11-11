# Repository Comparison and Curriculum Audit

**Review date:** 2026-11-10 (America/Chicago)  
**Fork:** [LUNCY579/ai-engineering-hub](https://github.com/LUNCY579/ai-engineering-hub) at `386cfc3647c63987f10345cf38ee522373f5dfa0` (last fork commit observed 2026-05-05)  
**Original:** [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) at `042aeb5067384981eeba6a07fa882f436bb1660d` (upstream head commit dated 2026-10-30)

## 1. Git history comparison

GitHub's cross-fork compare for `patchy631:main...LUNCY579:main` returned **behind by 32 commits, ahead by 0, status: behind**. All root entries present in the fork matched the same-name upstream entry's Git tree/blob SHA during this read. This means no fork-specific code changes were detected in the compared snapshot; it does not prove that every executable project is safe, tested or up to date.

## 2. Inventory and index findings

- Fork root: 109 directories, of which `assets` and `resources` are shared support folders; **107 potential lesson/project directories** remain.
- README index: **88 lesson links**. Of these, **86 target existing fork folders** and **2 are broken**.
- **21 existing project folders are absent from the README lesson index**.
- The README's advertised **93+ projects** and its displayed difficulty counts do not match the 88 actual lesson links found in the Markdown. This is an indexing/counting issue, not necessarily a deletion of source code.
- The official repository has 117 top-level directories (8 more than the fork), plus one extra root `.gitignore` file.

### Missing upstream directories

1. `biotech-agentic-analyst`
2. `build-code-harness`
3. `conversational-support-flow`
4. `courses` (contains `anthropic-academy-courses` in the inspected directory)
5. `grpo-finetuning-qwen3`
6. `omnigraph-multi-agent`
7. `run-jev-inside-agent-harness`
8. `zep-observations`

### Broken links in fork README

- `attention-is-all-you-need-impl`
- `nvidia-demo`

### Unindexed fork directories (21)

- `agent2agent-demo`
- `ai-avatar-demo`
- `ai-podcast-generation`
- `ai-podcast-generator`
- `amazon-product-analysis-server`
- `art_mcp_rl`
- `colbert-rag`
- `context-engineering-pipeline`
- `corrective-rag`
- `database-memory-agent`
- `finetune-studio-mcp-app`
- `flight-booking-crew`
- `hugging-face-skills`
- `knowledge distillation`
- `minimaxm2-vs-sonnet4-5-vs-kimik2-vs-gemini3`
- `multi-modal-rag`
- `open-agent-builder`
- `openai-swarm-ollama`
- `openclaw-secure-deployment`
- `sales-analytics-agent`
- `train-yolo26-object-detection`

## 3. Spot checks of lesson contents

The `simple-rag-workflow` folder contains a README, `workflow.py`, `workflow.ipynb` and `evaluation.ipynb`; the README documents LlamaIndex with Ollama. The `agentic_rag` folder has application variants, notebooks and a `src` directory, with its README describing CrewAI, document lookup and FireCrawl fallback. The `mcp-agentic-rag` folder includes `server.py`, `rag_code.py` and `notebook.ipynb`; its README opening also contains a potentially misleading generic book-writing description that deserves an editorial review. `Build-reasoning-model` contains a GRPO notebook and short README. `ai-engineering-roadmap` contains a ten-topic learning outline.

**Audit limit:** This was a live GitHub root-tree, history and selected-folder review, not a full runtime/security audit of 107 projects. No dependencies were installed and no execution benchmark was run. This distinction matters before treating tutorials as production-ready.

## 4. Prioritized improvements

1. **Synchronize upstream deliberately.** Review the 32 upstream commits, preserve a reproducible fork baseline, and merge/update only after checking API keys, package drift, and new content licensing. Do not blindly overwrite user-authored downstream work in future updates.
2. **Repair the README catalog.** Remove or correctly restore the two broken links; add the 21 uncataloged folders; generate displayed counts from an explicit catalog file.
3. **Add source-backed lesson metadata.** Record folder path, title, difficulty, dependencies, run instructions, estimated hardware, expected costs, sample data, whether external APIs are required, and last verified run.
4. **Add automated checks.** CI can validate Markdown links, parse notebooks, inspect for committed secrets, smoke-test dependency manifests, and check reproducibility of a sample tutorial matrix.
5. **Separate tutorials from production claims.** Introduce reproducible acceptance tests, explicit risk notices for side effects, and evidence-based metrics before describing a lesson as production-ready.
6. **Maintain the textbook collection.** Each independent companion volume should gain a project-file walkthrough and verified runnable lab after hands-on validation; rebuild the PDFs from editable Markdown when code changes.

## 5. Deliverable scope

This bundle includes **107 separate, editable project companion textbooks and 107 matching PDFs**, plus **10 shorter roadmap-module books and PDFs** corresponding to the ten headings within the fork's `ai-engineering-roadmap/README.md`. The books contain technical foundations, conceptual example code, projects to inspect, original exercises, solved numerical problems and evaluation guides. They are explicitly **study companions**, not certified line-by-line reproductions of all repository source files.

## 6. License and source notes

The original repository is published under an MIT License; source material remains credited and linked. The textbooks are new educational writing derived from high-level lesson descriptions and broadly established technical ideas. They do not reproduce complete upstream notebooks, datasets or third-party course content. Check each linked subproject and upstream asset for any additional licensing information before commercial redistribution.