---
name: master-doc
description: Create or execute a "Master Doc" — one planning .md file in /docs with a human checklist (Task ID, business value, MoSCoW, Fibonacci effort/complexity/risk), decisions, findings and step-by-step task instructions. Use when asked to analyze a repo and create a master doc / master plan, or to work on tasks from an existing master doc.
---

# Master Doc Skill

A Master Doc is ONE Markdown file that turns a repo analysis into a checklist the human can track and instructions a coder (or AI) can follow, one task at a time.

This skill has two modes:
- **Create mode** — the user asks to analyze the repo and create a Master Doc.
- **Execute mode** — the user asks to work on task(s) from an existing Master Doc.

---

## Create Mode

### Rules
- Planning only. Do NOT change any code.
- The user's prompt gives: context, goal, scope, constraints, file name, ID format. If anything is missing, use the defaults below and list them under "Assumptions".
- Write in simple English. Short sentences. Explain technical terms in a few words the first time.
- Only report what you can see in the code. If unsure, mark it `UNVERIFIED`. Never invent files, functions or libraries.

### Defaults (when the prompt doesn't say)
- File: `/docs/master-plan-YYYY-MM-DD.md`
- Task ID: `T-001`, `T-002`, ... (or `AREA-NN` if the user gives area prefixes)
- Decision ID: `D-01`; Finding ID: `F-01`
- Lenses: bugs, security, code quality, tests, error handling

### Steps
1. Read folder structure, config/package files, entry points, README and any docs the user names.
2. Read the code for each in-scope area, using only the lenses asked for.
3. For every finding, record evidence: `path/to/file:line` or function name.
4. Turn findings into tasks. Group small related problems into one task. One task = one clear outcome, small enough to finish and test in one sitting.
5. Score each task (see Scoring). Split any task that gets a 13.
6. Work out the order: what must come first so later tasks are easier or safer. Group into phases.
7. Write the doc using the exact structure below.
8. Run the Self-Check. Fix anything that fails.
9. Reply in chat with ONLY: file path, number of tasks, count by MoSCoW, and the list of decisions the human must make.

### Scoring

**MoSCoW**
- **Must** — goal fails without it, or it's a serious bug / security hole
- **Should** — important and valuable, but the goal can be reached without it
- **Could** — nice to have
- **Won't** — not now; listed so it isn't forgotten

**Fibonacci (1, 2, 3, 5, 8, 13)** for Effort, Complexity, Risk:

| Score | Effort (work size) | Complexity (how hard to think through) | Risk (chance of breaking something) |
|-------|--------------------|----------------------------------------|-------------------------------------|
| 1 | Minutes, tiny change | Obvious | Almost zero |
| 2 | Under an hour | Simple | Very low, isolated |
| 3 | Few hours | Some logic | Low, few places |
| 5 | About a day | Several parts interact | Medium, shared code |
| 8 | Several days | Hard, unclear edge cases | High, core flow or data |
| 13 | Too big → split | Too unclear → split | Very high → split |

- Score honestly. Don't default to 3.
- If the user asks for a Value score, use the same Fibonacci scale (1 tiny → 13 critical).

**Status:** `TODO` / `DOING` / `BLOCKED` / `DONE` / `SKIPPED`

### Business Value rule
Write it as a user or business benefit, not a tech change.
- Good: "Users stop getting logged out randomly"
- Bad: "Refactor token refresh"

---

## Master Doc Structure (use exactly, in this order)

Keep every heading. If a section has nothing, write "None".

```markdown
# <Title>

## 1. Header
- Date:
- Version: v1
- Repo / branch / commit:
- Goal:
- Status: Draft

## 2. Legend
- Task ID format:
- MoSCoW: Must / Should / Could / Won't (one line each)
- Scores: Fibonacci 1–13 for Effort, Complexity, Risk (13 = must split)
- Status: TODO / DOING / BLOCKED / DONE / SKIPPED

## 3. Human Checklist

| Done | ID | Task (simple English) | Business Value | MoSCoW | Effort | Complexity | Risk | Depends On | Decision | Status |
|------|----|-----------------------|----------------|--------|--------|------------|------|------------|----------|--------|
| [ ] | T-001 | ... | ... | Must | 3 | 2 | 5 | — | D-01 | BLOCKED |

**Summary**
- Total tasks: N (Must: n, Should: n, Could: n, Won't: n)
- Total effort points: Must n, Should n, Could n
- Highest-risk tasks: ...

## 4. Decisions Needed

### D-01: <simple question>
- Why it matters:
- Options:
  - A: ... (pros / cons)
  - B: ... (pros / cons)
- AI recommendation: <option> because ...
- Blocks: T-00x
- **Human decision:** PENDING

## 5. Findings Summary
- Repo overview (max 10 lines):
- Key problems (most important first):
- What is already good (don't break it):

## 6. Detailed Findings

### F-01: <short title>
- Area:
- Problem:
- Evidence: `path/file:line`
- Impact if ignored:
- Tasks: T-00x

## 7. Task Instructions

### T-001: <title>
- **Goal:**
- **Why:** F-0x
- **Files:**
- **Steps:**
  1. ...
- **Acceptance criteria:**
  - [ ] ...
- **How to verify:** commands / tests / manual checks
- **Do NOT:**
- **Depends on:** tasks / decisions
- **Rollback:**
- **Scores:** E? C? R? — reason if Risk ≥ 5

## 8. Execution Plan
- Phase 1: T-001, T-002 — why first
- Phase 2: ...

## 9. Assumptions and Open Questions
- Assumptions (mark UNVERIFIED if not confirmed):
- Questions:

## 10. Working Rules
<copy the Execute Mode rules from the skill here, so any AI opening this doc follows them>

## 11. Change Log
| Date | Version | Change | By |
|------|---------|--------|----|
| ... | v1 | Created | AI |
```

### Checklist table rules
- Sort by phase (execution order), then MoSCoW.
- Every row in section 3 has a matching block in section 7, and the other way round.
- "Decision" links to a real D-xx, or "—".
- A task waiting on a PENDING decision has Status `BLOCKED`.

### Self-Check (before replying)
- [ ] File is at the right `/docs/` path
- [ ] All 11 sections exist, in order
- [ ] Every task has ID, value, MoSCoW, Effort, Complexity, Risk
- [ ] No 13s left
- [ ] Section 3 and Section 7 match one-to-one
- [ ] Every finding has evidence or is marked UNVERIFIED
- [ ] Every decision link points to a real D-xx
- [ ] Simple English throughout
- [ ] No code was changed

---

## Execute Mode

When asked to work on a Master Doc task:

1. Open the Master Doc. Read the Legend, the task's block in section 7, and its dependencies.
2. If a linked decision is PENDING or a dependency is not DONE → stop and ask the human.
3. Do **only** the requested task(s). Default: one task at a time, in checklist order.
4. Follow the task's Steps and Do NOT rules. Stay inside its Files list unless clearly needed; if you go outside, say so.
5. Run the "How to verify" steps. Don't mark done if they fail.
6. Update the doc:
   - Tick `[x]` and set Status `DONE` in section 3
   - Tick its acceptance criteria in section 7
   - Add a Change Log line
7. New problem found while working → add it as a new task at the end with a new ID. Don't fix it silently.
8. Task bigger than its score → stop, tell the human, suggest a split.
9. Never delete tasks. Use `SKIPPED` with a reason.
10. Reply with: what changed (files), verify result, next task ID.

## Re-analysis
If asked to refresh an existing Master Doc: keep existing IDs, add new tasks with new IDs, bump the version (v1 → v2), and log it in the Change Log. Don't create a second Master Doc for the same goal.
