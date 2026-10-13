# Guide: incremental updates

Goal: bring both docs up to date with the least rewriting, so human edits survive and the git diff stays easy to review.

## 1. Get the changes

`scripts/repo_scan.py` already printed, per doc, the stamped commit and the files changed since. To see more:

```bash
git log --oneline <stamped_hash>..HEAD
git diff --name-status <stamped_hash>..HEAD
git diff <stamped_hash>..HEAD -- <path>
```

**Ignore the three output files** (`docs/PROJECT_ARCHITECTURE.md`, `docs/PROJECT_OVERVIEW_FOR_HUMAN.md`, `README.md`) when listing changes and when computing the ~40% threshold. The docs are usually committed after their stamp, so they always show up in the diff, but they are not code changes. The scanner already filters them out.

Also consider uncommitted changes (`git status --short`). The stamp records HEAD, so describe committed code only, but mention large uncommitted work under Open Questions.

The two docs may carry different stamps (for example, someone regenerated only one). Compute changes for each doc from its own stamp.

## 2. Read every changed file

Open each changed file and read the diff and the surrounding code. Never infer the change from the file name. For deleted or renamed files, search both docs for the old path and fix every mention.

## 3. Map changes to sections

| Change in... | Architecture doc sections | Human doc sections |
|--------------|---------------------------|--------------------|
| Models, schema, migrations, seeds | 7 Database, 5 Modules, 18 Cheat sheet | 🗄️ The data |
| Routes, controllers, handlers, CLI commands, GraphQL, events | 10 API, 11 Key Flows | 🔄 How things flow (if a main journey changed) |
| Services, jobs, listeners, workers, schedulers | 5 Modules, 6 Entry Points, 11 Key Flows, 15 Conventions | 🧱 Building blocks (if a new block appeared) |
| Auth, roles, permissions, policies, guards | 12 Auth | 🔄 flows if login changed |
| Frontend state, stores, API clients, router | 8 Frontend Data Layer, 5 Modules | 🗄️ The data |
| Components, styles, tokens, theme, design system | 9 Design Philosophy | 🎨 Design philosophy |
| Manifests, lock files | 2 Tech Stack, 19 Dependencies | 🛠️ Run it (if versions or commands changed) |
| Config files, `.env.example` | 13 Configuration | 🛠️ Run it (if setup steps changed) |
| CI, Docker, infra, deploy scripts | 14 Build/Deploy | 🛠️ Run it |
| New or removed folders/apps/packages | 3 Structure, 4 System Architecture, 18 Cheat sheet | 📁 Code organization, 🧱 Building blocks |
| Tests | 14 Build/Deploy, 17 Risks | ⚠️ Honest corner (if coverage story changed) |
| External SDKs or API clients | 16 External Integrations, 13 Config | 🗺️ Big picture |
| TODO/FIXME added or removed | 17 Risks | ⚠️ Honest corner |

The human doc changes far less often. Update it only when a change alters something a newcomer would notice: a new building block, a changed journey, new setup steps, a new main entity, a new rough edge. Otherwise only its stamp changes.

- A new **domain** table or model (something a user or the business would name, like `comments` or `invoices`) always counts, even if it has no UI yet. Join tables, log tables and framework tables do not.
- Always refresh numbers that drift with any file change, even in unmapped sections: file counts in section 3 and in the human code tree, counts of routes or tables quoted in the summaries.
- If the Table of Contents wording does not match the headings, fix it while you are there.

## 4. Patch

- Use `Edit` on the affected sections only. Do not rewrite untouched sections.
- Keep text a person added by hand. If the code now proves it wrong, fix it and note it in the report.
- Update Mermaid diagrams when their boxes or relations changed.
- Update the Table of Contents only if a heading changed (headings are stable, so this should be rare).
- Always update both stamps (comment line + visible block) to the new HEAD.
- Add one row to the architecture doc's **Appendix: Update Log**: date, new short hash, `incremental`, a one-line summary. Keep the last ~10 rows.
- Refresh the README block: update the stamp line every time, and the "At a glance" line only if the stack or shape changed. Leave the rest of the block's wording as it is (see `references/readme-block.md`).

## 5. When to switch to a full rewrite

Stop patching and regenerate the doc fully if: the stamped commit is not in history (rebased or squashed), more than ~40% of tracked files changed, the architecture style changed (for example a monolith split into services), or the existing doc does not follow the current template headings.
