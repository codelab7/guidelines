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

Hand-written product docs in `docs/` (the ones the human doc absorbs) count as changes too: if one changed, check the human doc still covers everything in it.

## 3. Map changes to sections

| Change in... | Architecture doc sections | Human doc sections |
|--------------|---------------------------|--------------------|
| Models, schema, migrations, seeds | 6 Data Model, 15 Recipes (if the steps changed) | 🧱 Building blocks, 🔍 Up close (if a user-visible thing or rule changed) |
| Enums, statuses, lifecycles | 6.4 Enums, 7 Business Rules | 🔍 Up close (state diagrams) |
| Validation, form requests, DTOs | 7 Validation and Business Rules, 10 API conventions | 🔍 Up close / ⚠️ Good to know (if a rule or limit changed) |
| Routes, controllers, handlers, CLI commands, events | 10 API Surface, 11 Key Flows, 5 Request Lifecycle (if a layer changed) | 🔄 How things work, 🧭 How to use it (if a journey changed) |
| Middleware, request pipeline | 5 Request Lifecycle, 8.4 | Usually none |
| Services, jobs, listeners, workers, schedulers, mail | 12 Background Work, 11 Key Flows | 🔄 How things work (if users notice it) |
| Auth, roles, permissions, policies, guards | 8 Auth | 🔐 Who can do what |
| Frontend state, API client, router, offline | 9 Frontend Wiring | 📱 Where it works (offline/install), 🧭 How to use it (new screens) |
| Components, pages, styles, theme | 9 Frontend Wiring (UI system) | 🧭 How to use it (if a screen was added or removed) |
| Manifests, lock files | 2 Tech Stack (key libraries only) | None |
| Config files, `.env.example` | 13 Configuration | None |
| CI, Docker, infra, deploy scripts | 14 Build, Test, Deploy | None |
| New or removed folders/apps/packages | 3 Repository Map, 4 System Wiring | 🗺️ Big picture (if a new app or outside service appeared) |
| A new pattern repeated in 3+ places, or a `CLAUDE.md`/`AGENTS.md` rule change | 15 Patterns and Recipes | None |
| Tests | 14 Build, Test, Deploy, 16 Risks | None |
| External SDKs or API clients | 12 Integrations, 13 Configuration | 🗺️ Big picture, 📱 Where it works |
| Bugs fixed or found, TODO/FIXME added or removed | 16 Risks and Gaps | ⚠️ Good to know (if users notice it) |

The human doc changes less often. Update it only when something a **user** would notice changed: a new feature or screen, a changed rule or limit, a new role or permission, a new journey, a fixed or new bug. Pure code changes (refactors, new libraries, CI) never touch it. Otherwise only its stamp changes.

- A new **domain** table or model (something a user or the business would name, like `comments` or `invoices`) always counts for both docs, even if it has no UI yet (in the human doc, mark it 🚧). Join tables, log tables and framework tables only touch section 6.
- Whenever a heading is added, removed or renamed (a new table in 6.3, a new flow in 11, a new block or journey in the human doc), update that doc's **Index** in the same edit. In the human doc, give the new heading its `<a id>` anchor line too.
- While patching, apply the golden rule (architecture guide section 2): don't add inventory, and if a section you touch has drifted into inventory, compress it.

## 4. Patch

- Use `Edit` on the affected sections only. Do not rewrite untouched sections.
- Keep text a person added by hand. If the code now proves it wrong, fix it and note it in the report.
- Update Mermaid diagrams when their boxes or relations changed.
- Keep each Index matching its headings exactly. The checker reports Index links that point nowhere and headings missing from the Index.
- Always update both stamps (comment line + visible block) to the new HEAD.
- Add one row to the architecture doc's **Appendix: Update Log**: date, new short hash, `incremental`, a one-line summary. Keep the last ~10 rows.
- Refresh the README block: update the stamp line every time, and the "At a glance" line only if the stack or shape changed. Leave the rest of the block's wording as it is (see `references/readme-block.md`).

## 5. When to switch to a full rewrite

Stop patching and regenerate the doc fully if: the stamped commit is not in history (rebased or squashed), more than ~40% of tracked files changed, the architecture style changed (for example a monolith split into services), or the existing doc does not follow the current template headings (for example a doc written by an older version of this skill).
