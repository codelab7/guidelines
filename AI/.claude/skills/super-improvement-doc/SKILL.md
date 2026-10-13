---
name: super-improvement-doc

description: Plan big changes before coding, then build them step by step. Researches current best practices online, analyzes the repo, and writes ONE plan at /docs/PLAN__{name}.md — Part 1 a fun, simple checklist for the human (IDs, Must/Should/Could, value stars, Fibonacci effort and risk, decisions), Part 2 detailed vibe-coding instructions for the AI. Also works through an existing PLAN__ doc by task ID, asks before risky work, and ticks items off. Use this whenever the user wants a plan, roadmap, improvement doc, master plan or checklist for a big task, redesign, design shift, architecture change, refactor, migration, or a focused improvement like SEO, accessibility (WCAG), mobile experience, performance or security — even if they don't say "doc". Also use when they say "work on T-003", "do SEO-01 to SEO-04", "next task from the plan", or ask about a PLAN__ file in /docs. Not for small one-file fixes.

argument-hint: "[goal to plan] | [task IDs, e.g. SEO-01 SEO-02 | next]"

model: opus
effort: high
allowed-tools: Read Grep Glob WebSearch WebFetch

---

# Create Improvement Doc

Big changes go wrong when they are planned on the fly. This skill writes the plan down first, lets the human read and approve it, and then works through it one ID at a time.

The plan is ONE Markdown file: `/docs/PLAN__{name}.md`. It has two parts:
- **Part 1 — The Checklist (for the human).** Fun, simple, honest. The human reads only this.
- **Part 2 — Vibe Coding Instructions (for the AI or coder).** Detailed and technical. The human never needs to read it.

Input from the user: $ARGUMENTS

**Why this runs in the main chat (not a forked subagent):** the user must be able to answer questions, approve risky steps and see progress. You may use an Explore subagent to search a very big repo faster, but you do the research thinking, write the plan and make the calls yourself.

## Files in this skill

Read these when the step says so. Don't skip them — they hold the details.

| File | Read it when |
|------|--------------|
| `references/research-guide.md` | Create mode, Step 2–4 (what to search, how to read the repo, how to size work) |
| `references/scoring-guide.md` | Create mode, Step 5 (priority, value, effort, risk, IDs, sorting, "confirm first") |
| `references/writing-style.md` | Create mode, Step 7 (tone and words for Part 1) |
| `assets/plan-template.md` | Create mode, Step 7 (exact structure of the doc) |

## Pick the mode

| The user says something like... | Mode |
|---|---|
| "create a plan / improvement doc for X", "plan the redesign", "let's document this before we change Y" | **Create** |
| "work on T-003", "do SEO-01 to SEO-04", "next task", "continue the plan" | **Execute** |
| "what does SEO-03 mean?", "why is this a Must?" | **Answer** — reply from the doc in simple English, change nothing |
| "refresh the plan", "re-check the repo", "update the plan" | **Refresh** |

If a `PLAN__` file for the same goal already exists in `/docs`, never create a second one. Use Refresh (or Execute) on the existing file.

---

## Create mode

Planning only. Do not change any code in this mode.

### Step 1 — Understand the goal
- Say the goal back in one plain sentence.
- Name the type of change: big feature, design shift, architecture change, migration, or focused improvement (SEO, accessibility, mobile UX, performance, security, i18n...).
- Find out: what "done" looks like, what is in and out of scope, and any limits (deadline, stack, areas not to touch).
- **If the goal is unclear, ask before going further.** Unclear means two fair readings would lead to different plans. Ask at most 3 short questions (use AskUserQuestion if available). If the user is not around to answer, take the most sensible reading and write it under Assumptions.

### Step 2 — Research the goal online
Follow `references/research-guide.md`. Look up current standards and best practices with WebSearch/WebFetch (for example search engine guidelines for SEO, WCAG for accessibility, platform guidelines for mobile UX). Do this even if you think you know the answer — standards change and memory goes stale. Write each source, link and date checked into Part 2 → Research Notes. Keep only rules that matter for this repo.

### Step 3 — Read the project
- First read `/docs/PROJECT_ARCHITECT.md` if it exists, then every other file in `/docs` (old plans, decisions, notes). Also glance at `README`, `CLAUDE.md`, `ARCHITECTURE.md` if present. These are the house rules.
- Then read the code the goal touches: routes/pages, components, styles, config, and the libraries in package files.
- For every finding, write evidence as `path/to/file:line` (or a function name). If unsure, mark it `UNVERIFIED`. Never invent files, functions or libraries.
- Note what is already good, so the plan doesn't break it.

### Step 4 — Estimate the size
For each idea, count roughly how many files it touches (Grep/Glob help). Also check how widely shared those files are. A one-line change in a component used in 40 places is risky. This count feeds Effort and Risk.

### Step 5 — Build and score the tasks
Follow `references/scoring-guide.md`.
- One task = one clear outcome that can be finished and checked in one sitting. Group tiny related fixes together.
- Give each task: ID, Priority, Value, Effort, Risk, file count, dependencies, decision link, and "Confirm first?".
- Anything that scores 13 must be split. No 13s in the final doc.
- Questions only the human can answer become decisions `D-01, D-02...`. A task waiting on a PENDING decision gets status `BLOCKED`.
- Ideas not worth doing now go to "Not doing now" with an honest reason.

### Step 6 — Check the plan is real
Before writing, test every task:
- **Correct?** Based on evidence and research, not guesses.
- **Workable?** Someone can do it with what is in this repo.
- **Worth it?** The value is worth the effort and risk. If not, drop it or move it to "Not doing now".
- **Complete?** If all the Musts are done, is the goal reached? If not, something is missing.
- No duplicate tasks. No 13s.

### Step 7 — Write the doc
- Use `assets/plan-template.md` exactly. Keep every heading; write "None" if a section is empty.
- Write Part 1 with `references/writing-style.md`: cheerful, simple English, a few emojis, no code, honest.
- Write Part 2 for a coder: clear goal, exact files, step plan, impact, blockers, how to verify, rollback.
- Copy the "Working on the plan" rules below into Part 2 → Working Rules, so any AI that opens the doc later follows them.
- Save as `/docs/PLAN__{name}.md`. `{name}` = the name the user gave, or a short kebab-case slug of the goal (`PLAN__seo.md`, `PLAN__mobile-experience.md`). Create `/docs` if it doesn't exist.

### Step 8 — Self-check
- [ ] File is at `/docs/PLAN__{name}.md`
- [ ] Every template section exists, in order
- [ ] Every task has ID, Priority, Value, Effort, Risk, file count, Confirm first, Status
- [ ] Each checklist is sorted by Value (prerequisites placed just above the task that needs them)
- [ ] No 13s
- [ ] Every Part 1 task has a matching Part 2 task block, and the other way round
- [ ] Every finding has evidence or is marked UNVERIFIED
- [ ] Every decision link points to a real D-xx; tasks on PENDING decisions are BLOCKED
- [ ] Every research rule used has a source link
- [ ] Part 1 has no code and reads easily for a non-native English speaker
- [ ] No code was changed

### Step 9 — Reply
Keep it short:
- File path
- Number of tasks (🔴 Must n · 🟡 Should n · 🟢 Could n)
- Top 3 quick wins (high value, low effort)
- Decisions the user must make (one line each)
- How to start: "Say `work on SEO-01`, `do SEO-01 to SEO-03`, or `next task`."

---

## Execute mode — Working on the plan

These rules are also copied into every plan doc.

### Before you start
1. **Read the whole doc** — Part 1 and Part 2 — and understand the big goal first. A task done without the big picture can fight the goal.
2. **Find the requested IDs.** "next task" = the first `TODO` item in checklist order whose dependencies are `DONE`.
3. **Check before starting.** If the task is `BLOCKED`, a linked decision is `PENDING`, or a dependency is not `DONE` → stop, tell the user what is missing, and suggest what to do.
4. **Ask before risky work.** If the task says "Confirm first: Yes", or it touches auth, payments, the database (schema, migrations, data), deletes data, public APIs, shared core code, build/deploy config, or needs a new library → explain the plan in simple English (what changes, which files, what could break, how to undo) and wait for a clear "yes" before changing anything. Do the same if, once you are in the code, the task turns out riskier than the doc says.

### While working
5. **Do only the requested IDs.** For a series (e.g. SEO-01 to SEO-04), go one by one in checklist order: finish and verify one before starting the next, and pause at any task that needs confirmation. Never start a task the user did not ask for.
6. **Stay in scope.** Change only the files listed in the task block. If you need another file, say so before editing it.
7. **Keep changes small.** No unrelated refactors, renames or style changes.
8. **Follow the repo.** Match existing patterns, folder structure and naming. No new library without asking first.
9. **User + plan together.** Follow the user's latest instructions and the task block. If they clash, the user wins — say so and note it in the task's Work log.
10. **Found a new problem?** Add it as a new task at the end of the right checklist with a new ID (plus a Part 2 block). Don't fix it silently.
11. **Task too big?** Stop, explain why, and suggest how to split it. After the user agrees, add the new tasks and mark the old one `SKIPPED — split into X, Y`.
12. **Unsure or blocked?** Set status to `BLOCKED`, write the reason in the task's Work log, and stop.

### After finishing
13. **Verify.** Run the task's "How to verify" steps. If they fail, don't tick the box — fix within scope, or report it.
14. **Update the doc.** In Part 1: tick `[x]`, set `Status: DONE`, update the progress count. In Part 2: tick acceptance criteria and add a short Work log line (what changed, which files). Add a Change Log line. Never delete tasks — use `SKIPPED` with a reason.
15. **Reply short, in simple English.** Short sentences. Explain any technical term the first time. Use this format per task:

```
✅ SEO-01 — Done
Result: <what is better now, in one or two lines>
Impact: <files changed, anything the user should know or test>
Next: SEO-02 — <title>
```

Use ⏸️ instead of ✅ when waiting for confirmation, and ⛔ when blocked (with the reason).

---

## Answer mode
Answer from the doc in simple English. Don't change code or the doc. If the question shows the plan is wrong or missing something, say so and offer to update it.

## Refresh mode
- Keep all existing IDs. Add new tasks with new IDs; never reuse an ID.
- Re-check `DONE` tasks are still true and `TODO` tasks still make sense. Mark outdated ones `SKIPPED` with a reason.
- Redo research only where standards may have changed.
- Re-sort by Value, bump the version (v1 → v2), and add a Change Log line.
