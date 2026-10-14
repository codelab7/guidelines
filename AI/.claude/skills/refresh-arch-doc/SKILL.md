---

name: refresh-arch-doc

description: Analyze the whole repository and create or refresh three files - docs/PROJECT_ARCHITECTURE.md (a standalone architecture map for AI chats, AI projects and coding agents - how the system is wired, its data, validation and business rules, and the patterns to copy for new work), docs/PROJECT_OVERVIEW_FOR_HUMAN.md (a fun, emoji-rich, no-code "how it works" guide for anyone - what the product does, how to use it, who can do what, with lots of tables and diagrams) and a small managed section in the root README.md that links both docs. Builds everything from scratch the first time, then updates incrementally from git changes since the commit stamped in each doc. Use when the user runs /refresh-arch-doc or asks to generate, update, refresh, sync or re-stamp the architecture docs, project overview, onboarding guide, repo map or "context doc for AI", even if they name only one of the three files.

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
| `docs/PROJECT_ARCHITECTURE.md` | AI planners without the repo, coding agents with it, small models too | Neutral, table-first, standalone. How things are wired, the data and rules, the patterns to copy. Contracts (tables, enums, roles, env var names) in full; no catalogue of every class or function | `references/architecture-doc.md` |
| `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` | Anyone who wants to understand the product: owners, sales, support, new teammates | Fun, simple English, emojis and indicators, many tables and diagrams. How it works and how to use it. No code, no paths, no setup | `references/human-overview-doc.md` |
| `README.md` (repo root) | Anyone landing on the repo | Light, friendly, short. Only the managed block is yours. The README stays the home of setup and run steps | `references/readme-block.md` |

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
<!-- arch-doc-stamp: commit=<short-hash> branch=<branch> date=<YYYY-MM-DD> generator=refresh-arch-doc -->
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

Pick a mode **per doc**. The scanner suggests a mode but never sees the arguments, so `full` in the arguments always wins over its suggestion.

- **Full generation** when the doc is missing, has no stamp, its stamped commit is not in history, the arguments say `full`, or more than ~40% of tracked files changed since the stamp (a rewrite is cheaper and safer than many patches).
- **Incremental update** otherwise. Read `references/incremental-update.md` before you start it.
- **No changes** when the stamped commit equals HEAD and nothing relevant is dirty: only refresh the date in the stamp and the README line.

In any mode, replace an older generator name in the stamps and the README block (for example `update-arch-doc`) with `refresh-arch-doc`.

The README block is always regenerated from the two docs at the end (Step 4).

### Step 1. Orient (full generation)

- Read root files first: `README*`, every manifest and its **lock file** (for exact versions; for a huge lock file, Grep for the package names you need instead of reading it whole; if there is no lock file, use the manifest versions, say so once at the top of the Tech Stack section, and flag the missing lock file as a risk), `Dockerfile*`, `docker-compose*`, `Makefile`/`Taskfile`/`justfile`, CI config (`.github/workflows/`, `.gitlab-ci.yml`, etc.), `.env.example` (names only), linter/formatter configs, and existing `docs/`, `ARCHITECTURE*`, `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING*`.
- Existing docs are hints. When they disagree with the code, trust the code and note the difference under Open Questions.
- **Find the hand-written product docs** (any human guide to what the product does and its rules, such as `docs/PROJECT_GUIDELINES.md`, `docs/PRODUCT.md`, a docs wiki). The human doc must cover everything they cover, checked against the code. List them in your notes.
- **Note what the README already explains** (setup, commands, stack, deploy). The human doc must not repeat it.
- Decide the project shape from what you see: backend, frontend, full-stack, library, CLI, monorepo. This decides which mandatory sections get deep treatment (database architecture for backends; client data layer and design philosophy for frontends; both for full-stack).

### Step 2. Explore in depth (full generation)

Read the code, not just file names. You are a subagent, so you cannot launch further agents: read directly, and batch independent `Read`/`Grep`/`Glob` calls in parallel to go fast. For large repos, work area by area (each app/package, backend, frontend, data, infra) and keep short notes per area before writing.

Collect two kinds of facts.

**Contracts, with exact values:** every data store; every domain table with columns, types, null/default, keys and relations; every enum value; role strings and the permission matrix; every env var name; the API's resource groups and conventions; key library versions; build/test/deploy commands.

**How it works:** the path a request takes through the layers; where validation and each business rule are enforced; how auth and tenancy checks are wired; how the frontend gets and caches data; 3-8 key flows end to end; background work and integrations; the **patterns the code repeats** (look at 3+ examples of each kind of thing, note one file to copy, and note the places that break the pattern); risks and bugs.

While reading, also note what a **user** sees: screens, journeys, rules, limits, lifecycles, roles. The human doc is built from these.

Don't collect a catalogue of every class, function or route: an agent can search for those, and long lists bury the wiring. `references/architecture-doc.md` (section 2, "the golden rule") says exactly what to keep, compress and leave out. Read it before writing.

### Step 3. Write the two docs

1. Write `docs/PROJECT_ARCHITECTURE.md` first, following `references/architecture-doc.md`. It is the source of truth.
2. Then write `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` from what you learned, following `references/human-overview-doc.md`. It describes the product, not the code: no paths, no setup, nothing the README already says. Cover every feature and rule from the hand-written product docs. It must never contradict the architecture doc.

For big docs, write the skeleton with all headings first, then fill sections with `Edit`, so a long write never fails halfway.

Both docs open with an **Index**: a nested list linking every heading, so a reader can jump anywhere in one click. Write each Index last, from the final headings. The architecture doc links to GitHub-style heading links; the human doc links to `<a id>` anchors placed above its emoji headings. Each guide shows the exact rule.

### Step 4. Update the README

Follow `references/readme-block.md`. Work only between the `<!-- arch-docs:start -->` and `<!-- arch-docs:end -->` markers: rewrite the block in full generation, patch only changed lines in an incremental update. If the markers do not exist, insert the block (rules in the guide). If `README.md` does not exist, create a short, friendly one.

### Step 5. Verify, fix, verify again

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/check_docs.py" .
```

It checks: stamps present and matching HEAD, leftover placeholders, empty sections, secret-looking strings, backticked paths that do not exist, the 18 architecture sections, that each Index links every heading and every link lands, signs of inventory in the architecture doc (long route tables, many function names), code, paths and README-repeated commands in the human doc, too few tables or diagrams in the human doc, README markers and links. Fix every `ERROR`. Read each `WARN` and fix it unless it is a false alarm. Run it again until there are no errors.

Then do the reader tests yourself. Re-read `docs/PROJECT_ARCHITECTURE.md` as a **small AI model that has never seen the repo** and check it can answer:

- What does this system do, how is it split up, and how are the parts wired together?
- How does a request travel through the layers, and where is input validated and permission checked?
- What tables, fields, enums, roles and env vars exist, exactly?
- What business rules apply, and where are they enforced?
- I need to add a new entity, field, endpoint or page: which pattern do I follow and which file do I copy?
- If I change X, what else could break?

Also check the opposite: is there a long list a planner would never miss if it were gone (every class, every function, every response key)? Compress or remove it.

Re-read the human doc as **a new sales or support teammate who never codes**: do they understand what the product does, how to use it, and who can do what, without meeting a single file name or tech word? Is it fun and honest? Does it cover everything the hand-written product docs covered, without repeating the README? If any test fails, fix it (or go back and read more code).

### Step 6. Report

Print exactly this block and nothing else. Do not paste the documents into the chat.

```
refresh-arch-doc ✅

  Commit:    <short hash> - <message>
  Updated:   YYYY-MM-DD
  Architecture:  docs/PROJECT_ARCHITECTURE.md        created | regenerated | updated | re-stamped
  Overview:      docs/PROJECT_OVERVIEW_FOR_HUMAN.md  created | regenerated | updated | re-stamped
  README:        README.md                            block added | block updated | created
  Sections:  <n> of 18 filled in the architecture doc
  Changes:   <1-3 lines; what changed and why. "first generation" for new docs>
  Gaps:      <1-3 lines: unverified or missing items, hand-written docs now fully covered by the human doc, problems outside the README block (stale pointers, secret-looking values - name the line, never repeat the value), or "none">
  Next:      Review the diff, then commit the three files together.
```

## Reference files

- `references/architecture-doc.md` - template, section checklist and writing style for the AI document. Read before Step 3.
- `references/human-overview-doc.md` - template, tone guide and examples for the human document. Read before Step 3.
- `references/readme-block.md` - the managed README block and insertion rules. Read before Step 4.
- `references/incremental-update.md` - how to map git changes to sections and patch safely. Read before any incremental update.
- `scripts/repo_scan.py` - Step 0 scanner. `scripts/check_docs.py` - Step 5 checker. Both use only the Python standard library.
