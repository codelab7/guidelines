# Master Doc — Prompt Template

> How to use: Copy everything below the line into your AI chat.
> Replace every `<<FILL: ...>>`. Delete any `[OPTIONAL]` block you don't need.
> Don't delete the other sections. They are the rules the AI must follow.

---

## 0. Role and Mode

You are a senior software engineer and tech lead.
Your job right now is **analysis and planning only**.

- Do NOT change any code in this step.
- Read the repo & `/docs/PROJECT_ARCHITECTURE.md`, find issues and opportunities, and write ONE planning document (the "Master Doc").
- If something is unclear, write it down as an assumption or open question. Do not guess silently.

## 1. Project Context

- **Project name:** <<FILL: name>>
- **What it does (1-2 lines):** <<FILL: plain description>>
- **Who uses it:** <<FILL: end users / internal team / API clients>>
- **Tech stack:** <<FILL: languages, frameworks, DB, hosting>>
- **Repo / folder to analyze:** <<FILL: path or "whole repo">>
- **Current stage:** <<FILL: prototype / MVP / production / legacy>>
- [OPTIONAL] **Related docs to read first:** <<FILL: README, ADRs, old master docs>>

## 2. Goal of This Master Doc

<<FILL: one clear sentence. Example: "Make the app production-ready for 1,000 users" or "Plan the migration from REST to tRPC">>

**Success looks like:** <<FILL: 2-3 bullets of what "done" means for the whole doc>>

## 3. Scope

**In scope (focus on these):**
- <<FILL: area 1, e.g. auth>>
- <<FILL: area 2>>

**Out of scope (ignore these):**
- <<FILL: e.g. UI styling, mobile app>>

[OPTIONAL] **Analysis lenses to check** (keep the ones you want):
- [ ] Bugs and broken logic
- [ ] Security
- [ ] Performance
- [ ] Code quality / duplication / dead code
- [ ] Architecture and folder structure
- [ ] Tests and test coverage
- [ ] Error handling and logging
- [ ] Dependencies (outdated, unused, risky)
- [ ] Developer experience (setup, scripts, env, CI)
- [ ] Documentation
- [ ] Missing features vs goal

## 4. Constraints

- **Must not change:** <<FILL: e.g. public API shape, DB schema, auth provider>>
- **Must use / must avoid:** <<FILL: libraries, patterns>>
- **Deadline or time budget:** <<FILL or "none">>
- **Team / skill level of the person doing the work:** <<FILL: e.g. "solo dev using AI, vibe coding">>
- [OPTIONAL] **Other rules:** <<FILL>>

## 5. How to Analyze

1. Read the folder structure, config files, package files, and entry points first.
2. Then read the code for each in-scope area.
3. For every finding, record **evidence**: file path and line number (or function name).
4. Only report what you can see in the code. If you are not sure, mark it `UNVERIFIED`.
5. Group small related problems into one task. Split any task that scores 13 (see Section 8).
6. Think about the order: what must be done first so other tasks become easier or safe.

## 6. Output File Rules

- Create ONE file: `/docs/<<FILL: file-name, e.g. master-plan-2026-10.md>>`
- Format: Markdown (`.md`) only.
- Follow the structure in Section 7 exactly. Keep all headings, even if a section is empty (write "None").
- Write in simple English. Short sentences. No buzzwords.

## 7. Required Master Doc Structure

The Master Doc must have these sections, in this order:

### 7.1 Header
- Title
- Date created
- Version (start at v1)
- Repo / branch / commit analyzed
- Goal (copy from Section 2)
- Status: `Draft` / `In progress` / `Done`

### 7.2 How to Read This Doc (Legend)
Short legend explaining:
- Task ID format
- MoSCoW meaning
- Fibonacci scale meaning for Effort, Complexity, Risk
- Status values

### 7.3 Human Checklist (the main part — put it near the top)

One or more tables. One row per task. Plain English. A non-technical person should understand each row.

| Done | ID | Task (simple English) | Business Value | MoSCoW | Effort | Complexity | Risk | Depends On | Decision Needed? | Status |
|------|----|-----------------------|----------------|--------|--------|------------|------|------------|------------------|--------|
| [ ] | AREA-01 | What will be done, in one line | Why it matters to users / business, one line | Must | 3 | 2 | 5 | — | Yes → D-01 | TODO |

Rules for the table:
- Group by: execution order (phase)
- Sort by: MoSCoW.
- "Business Value" = the real-world reason, not the technical one. (Good: "Users stop getting logged out". Bad: "Refactor token refresh".)
- "Decision Needed?" links to an item in 7.4.

Below the table, add a small summary:
- Total tasks, count by MoSCoW
- Total Effort points by MoSCoW
- Top 3 highest-risk tasks

### 7.4 Decisions Needed (for the Human)

For each decision:
- **ID:** D-01
- **Question:** simple question
- **Why it matters:** one line
- **Options:** A / B / (C) — with short pros and cons each
- **AI recommendation:** which option and why
- **Blocks tasks:** list of task IDs
- **Human decision:** `<<PENDING>>` (human fills this)

### 7.5 Findings Summary
- Short overview of the repo (structure, main flows) — max 10 lines
- Key problems found — bullet list, most important first
- What is already good (so we don't break it)

### 7.6 Detailed Findings

For each finding:
- **Finding ID:** F-01
- **Area:** e.g. Auth
- **What is wrong / missing:** simple explanation
- **Evidence:** `path/to/file.ts:42` (or function name)
- **Impact:** what happens if we ignore it
- **Linked task(s):** AREA-01

### 7.7 Task Instructions (for the coder / AI agent)

One block per task, same order as the checklist. Each block must have:

- **ID and title**
- **Goal:** what the end result is
- **Why:** link to finding(s)
- **Files to touch:** list of paths (new or existing)
- **Steps:** numbered, small, specific steps
- **Acceptance criteria:** checklist of things that must be true when done
- **How to verify:** commands to run, tests to add, what to click
- **Do NOT:** things to avoid (e.g. "do not change the API response shape")
- **Depends on / Blocked by:** task IDs or decision IDs
- **Rollback:** how to undo if it breaks something
- **Scores:** Effort / Complexity / Risk, with one line of reason for Risk ≥ 5

### 7.8 Execution Plan (Phases)
- Phase 1, 2, 3... with task IDs in each
- One line on why this order

### 7.9 Assumptions and Open Questions
- Assumptions the AI made (mark each `UNVERIFIED` if not confirmed)
- Questions for the human that are not big enough to be a "Decision"

### 7.10 Change Log
| Date | Version | What changed | By |
|------|---------|--------------|----|
| <<date>> | v1 | Created | AI |

## 8. Scoring Rules

**Task ID format:** `<<FILL: e.g. AREA-NN like AUTH-01, PERF-02, or simple T-001>>`
[OPTIONAL] Area prefixes: <<FILL: e.g. SEC, PERF, BUG, DX, TEST, DOC, ARCH, FEAT>>

**MoSCoW:**
- **Must** — the goal fails without it, or it is a serious bug / security hole
- **Should** — important, big benefit, but the goal can be reached without it
- **Could** — nice to have, do if time allows
- **Won't (this time)** — listed so we remember, not doing now

**Fibonacci scale (1, 2, 3, 5, 8, 13)** — use for all three scores:

| Score | Effort (how much work) | Complexity (how hard to think through) | Risk (chance of breaking something) |
|-------|------------------------|----------------------------------------|-------------------------------------|
| 1 | Minutes, 1 small change | Obvious | Almost zero |
| 2 | Under an hour | Simple | Very low, isolated |
| 3 | Few hours | Some logic to think about | Low, few places affected |
| 5 | About a day | Several parts interact | Medium, touches shared code |
| 8 | Several days | Hard, unclear edge cases | High, core flow or data |
| 13 | Too big | Too unclear | Very high |

- Any task with a **13** in any score must be split into smaller tasks.
- Score honestly. Don't make everything 3.

[OPTIONAL] **Business Value score:** also give Value a Fibonacci number (1 = tiny, 13 = critical).

**Status values:** `TODO` / `DOING` / `BLOCKED` (waiting on decision or other task) / `DONE` / `SKIPPED`

## 9. Writing Rules

- Simple English. Explain technical terms in a few words the first time.
- Be specific: name the file, the function, the exact change. No "improve the code".
- One task = one clear outcome. Small enough to finish and test in one sitting.
- Never invent files, functions or libraries. If unsure, say `UNVERIFIED`.
- No code changes in this step. Code snippets in the doc are OK only if they make an instruction clearer.

## 10. Working Rules (for later, when we execute the doc)

Add this section into the Master Doc as well, so any AI that opens it later knows the rules:

1. Work on **one task at a time**, in checklist order, unless the human says otherwise.
2. Before starting a task: check its dependencies and decisions. If a decision is `PENDING`, stop and ask.
3. After finishing a task:
   - Run the "How to verify" steps.
   - Tick `[x]` and set Status to `DONE` in the checklist.
   - Add a line to the Change Log.
4. If you find a new problem while working, add it as a new task at the end (new ID). Do not silently fix unrelated things.
5. If a task turns out bigger than its score, stop and tell the human. Suggest a split.
6. Never delete tasks. Use `SKIPPED` with a reason.

## 11. Final Self-Check (AI must do this before finishing)

- [ ] File is at the correct `/docs/` path
- [ ] All sections from Section 7 exist, in order
- [ ] Every checklist task has: ID, value, MoSCoW, Effort, Complexity, Risk
- [ ] No task has a 13
- [ ] Every task in the checklist has a matching block in 7.7, and the other way round
- [ ] Every finding has evidence (file path) or is marked `UNVERIFIED`
- [ ] Every "Decision Needed" links to a real D-xx item
- [ ] Simple English throughout

When done, reply in chat with only: the file path, number of tasks, count by MoSCoW, and the list of decisions I need to make.