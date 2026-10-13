---

name: refresh-arch-doc

description: Analyze the whole repository and create or refresh three files - docs/PROJECT_ARCHITECTURE.md (a dense, standalone architecture reference written for AI chats, AI projects and coding agents), docs/PROJECT_OVERVIEW_FOR_HUMAN.md (a cheerful, simple-English, top-down guide for new developers) and a small managed section in the root README.md that links both docs. Builds everything from scratch the first time, then updates incrementally from git changes since the commit stamped in each doc. Use when the user runs /update-arch-doc or asks to generate, update, refresh, sync or re-stamp the architecture docs, project overview, onboarding guide, repo map or "context doc for AI", even if they name only one of the three files.

argument-hint: "[full]"

context: fork

disable-model-invocation: true

agent: general-purpose

model: opus

effort: high

background: false

allowed-tools: Read Glob Grep Write Edit Bash(git rev-parse *) Bash(git log *) Bash(git diff *) Bash(git status *) Bash(git show *) Bash(git rev-list *) Bash(git ls-files *) Bash(git cat-file *) Bash(git merge-base *) Bash(python3 *) Bash(python *) Bash(ls *) Bash(mkdir *) Bash(wc *)

---

# Update Architecture Docs

You are running in your own forked context. You cannot see the user's chat, so everything you need is in this file and its `references/`. Work alone from start to finish, then print the short report at the end.

ARGUMENTS: $ARGUMENTS
If the arguments contain `full`, do a full regeneration even when the docs already exist.

## What you produce

| File | Reader | Style | Read the guide |
|------|--------|-------|----------------|
| `docs/PROJECT_ARCHITECTURE.md` | AI chats, AI projects, sometimes coding agents | Dense, exact, neutral, fully standalone. Real values everywhere | `references/architecture-doc.md` |
| `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` | New and junior developers | Cheerful, funny, simple English, top-down, light emojis, no code | `references/human-overview-doc.md` |
| `README.md` (repo root) | Anyone landing on the repo | Light, friendly, short. Only the managed block is yours | `references/readme-block.md` |

Both docs start with a **freshness stamp** (see "Freshness stamp" below). The README block repeats the stamp in one line.

## Ground rules (why they matter)

1. **Touch only the three files above.** Create `docs/` if missing. Do not edit code, configs, or any other doc. Do not commit, push, or create branches. The user reviews the diff and commits it.
2. **Truth over polish.** Write only what you verified by reading code. Mark guesses `(inferred)` and things you searched for but could not find `(not found)`. An AI that reads a confident wrong fact will build a wrong plan on top of it, so an honest gap is worth more than a pretty guess.
3. **No secrets, ever.** Env var and config **names** and purpose only. Never values, keys, tokens, passwords, hostnames with credentials, or connection strings. These files get pasted into other AI tools.
4. **Markdown only.** Diagrams are Mermaid code blocks. No HTML pages, images, PDFs or artifacts.
5. **Repo-relative paths in backticks**, like `src/api/routes.ts`. They must exist. To mention a path you looked for and did not find, write it in backticks followed by `(not found)` on the same line, like `vite.config.ts (not found)`. The checker skips those.
6. **No placeholders left behind.** No `TODO`, `TBD`, `<fill in>`, or template angle-brackets. If a section does not apply, keep its heading and write `Not applicable: <one-line reason>`.
7. **Preserve human edits.** In incremental mode, keep text a person added by hand unless the code now proves it wrong (then fix it and mention it in the report).

## Freshness stamp

Put this at the very top of **both** docs, right under the H1 title. The HTML comment is for scripts; the visible lines are for readers. Keep the comment format exact so `scripts/repo_scan.py` can parse it.

```markdown
<!-- arch-doc-stamp: commit=<short-hash> branch=<branch> date=<YYYY-MM-DD> generator=update-arch-doc -->
```

Then a visible block. The two docs word it differently (see each guide), but both must show: last updated date, branch, short commit hash, commit message (first line, trimmed to ~72 chars), and a freshness rule saying the doc describes the repo exactly as of that commit, so anything committed later is not covered. If the folder is not a git repo, use `commit=none` and say so in the visible block.

## Workflow

### Step 0. Scan and pick the mode

Run the scanner, passing the repo path (it finds the git root itself, so no `cd` is needed):

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/repo_scan.py" .
```

Tool habits for the whole run: read files with `Read`, search with `Grep` and `Glob`, and keep `Bash` for `git` and the two scripts. That is faster, and those calls are pre-approved in this skill's frontmatter, so the run is not interrupted by permission prompts.

It prints: repo root, project name guess, branch, HEAD hash and message, today's date, dirty files, file counts per top-level folder (noise skipped), detected manifests/configs, a frontend/backend hint, and for each of the three files whether it exists, its stamped commit, whether that commit is still in history, and the list of files changed since it.

If `python3` is missing, try `python`. If both are missing, get the same facts by hand with `git rev-parse`, `git log -1`, `git status --short`, `ls`, and by reading the stamp line of each doc.

Pick a mode **per doc**:

- **Full generation** when the doc is missing, has no stamp, its stamped commit is not in history, the arguments say `full`, or more than ~40% of tracked files changed since the stamp (a rewrite is cheaper and safer than many patches).
- **Incremental update** otherwise. Read `references/incremental-update.md` before you start it.
- **No changes** when the stamped commit equals HEAD and nothing relevant is dirty: only refresh the date in the stamp and the README line.

The README block is always regenerated from the two docs at the end (Step 4).

### Step 1. Orient (full generation)

- Read root files first: `README*`, every manifest and its **lock file** (for exact versions; if there is no lock file, use the manifest versions, say so once at the top of the Tech Stack section, and flag the missing lock file as a risk), `Dockerfile*`, `docker-compose*`, `Makefile`/`Taskfile`/`justfile`, CI config (`.github/workflows/`, `.gitlab-ci.yml`, etc.), `.env.example` (names only), linter/formatter configs, and existing `docs/`, `ARCHITECTURE*`, `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING*`.
- Existing docs are hints. When they disagree with the code, trust the code and note the difference under Open Questions.
- Decide the project shape from what you see: backend, frontend, full-stack, library, CLI, monorepo. This decides which mandatory sections get deep treatment (database architecture for backends; client data layer and design philosophy for frontends; both for full-stack).

### Step 2. Explore in depth (full generation)

Read the code, not just file names. You are a subagent, so you cannot launch further agents: read directly, and batch independent `Read`/`Grep`/`Glob` calls in parallel to go fast. For large repos, work area by area (each app/package, backend, frontend, data, infra) and keep short notes per area before writing.

Collect, with real values: entry points; modules and their dependencies; every data store and every table/model with fields, types, constraints, indexes, relations; every route/command/event/export; auth mechanism, roles and permissions with stored values; 3-8 key flows traced through real files; external services; config and every env var name; build/test/deploy commands; dependencies with versions; conventions; frontend state, data fetching, routing, component and styling system; risks (TODO/FIXME clusters, dead code, missing tests, outdated deps).

`references/architecture-doc.md` has the full checklist per section. Read it before writing.

### Step 3. Write the two docs

1. Write `docs/PROJECT_ARCHITECTURE.md` first, following `references/architecture-doc.md`. It is the source of truth.
2. Then write `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` from what you learned, following `references/human-overview-doc.md`. It must never contradict the architecture doc. It explains less, but more warmly.

For big docs, write the skeleton with all headings first, then fill sections with `Edit`, so a long write never fails halfway.

### Step 4. Update the README

Follow `references/readme-block.md`. Work only between the `<!-- arch-docs:start -->` and `<!-- arch-docs:end -->` markers: rewrite the block in full generation, patch only changed lines in an incremental update. If the markers do not exist, insert the block (rules in the guide). If `README.md` does not exist, create a short, friendly one.

### Step 5. Verify, fix, verify again

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/check_docs.py" .
```

It checks: stamps present and matching HEAD, leftover placeholders, empty sections, secret-looking strings, backticked paths that do not exist, code blocks in the human doc other than Mermaid and shell commands, README markers and links. Fix every `ERROR`. Read each `WARN` and fix it unless it is a false alarm. Run it again until there are no errors.

Then do the reader test yourself. Re-read `docs/PROJECT_ARCHITECTURE.md` as an AI that has **never seen the repo** and check it can answer:

- What does this system do, and how is it split up?
- What exact routes, tables, fields, roles, env vars and commands exist?
- How does a request or job travel through the system?
- If I change X, what else could break? Where do I add a feature of type Y?
- How do I run, test and deploy it?

Re-read the human doc as a nervous first-week developer: is it clear, kind, honest, and fun? If either test fails, go back and read more code.

### Step 6. Report

Print exactly this block and nothing else. Do not paste the documents into the chat.

```
update-arch-doc ✅

  Commit:    <short hash> - <message>
  Updated:   YYYY-MM-DD
  Architecture:  docs/PROJECT_ARCHITECTURE.md        created | updated | re-stamped
  Overview:      docs/PROJECT_OVERVIEW_FOR_HUMAN.md  created | updated | re-stamped
  README:        README.md                            block added | block updated | created
  Sections:  <n> of 21 filled in the architecture doc
  Changes:   <1-3 lines; what changed and why. "first generation" for new docs>
  Gaps:      <1-3 lines of unverified or missing items, or "none">
  Next:      Review the diff, then commit the three files together.
```

## Reference files

- `references/architecture-doc.md` - template, section checklist and writing style for the AI document. Read before Step 3.
- `references/human-overview-doc.md` - template, tone guide and examples for the human document. Read before Step 3.
- `references/readme-block.md` - the managed README block and insertion rules. Read before Step 4.
- `references/incremental-update.md` - how to map git changes to sections and patch safely. Read before any incremental update.
- `scripts/repo_scan.py` - Step 0 scanner. `scripts/check_docs.py` - Step 5 checker. Both use only the Python standard library.
