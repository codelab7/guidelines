<!--
TEMPLATE for /docs/PLAN__{name}.md
- Keep every heading, in this order. Write "None" if a section is empty.
- Replace everything in {curly braces}. Delete these HTML comments in the final doc.
- Part 1 follows references/writing-style.md. Part 2 is for the AI/coder.
-->

# 🗺️ Plan: {Goal in plain words}

> **🎯 Big goal:** {1–2 sentences, plain English}
> **🤔 Why:** {benefit for users or the business}
> **🏁 Done means:** {how we'll know it worked — something you can see or measure}

- 📅 Created: {YYYY-MM-DD} · 🔄 Version: v1 · 📌 Status: Draft
- 🌿 Repo / branch / commit: {repo} / {branch} / {short commit or "not a git repo"}

---

# Part 1 — The Checklist 👀 (for you)

## 👋 How to use this plan
1. Read the checklist below. Ticked boxes = done.
2. Answer the decisions in "🤔 Decisions for you" — just reply in chat, e.g. "D-01: A".
3. Ask the AI to start: `work on {ID}`, `do {ID} to {ID}`, or `next task`.
4. Anything marked 🙋 — the AI will explain first and wait for your "yes".

**Legend**
- Priority: 🔴 Must (goal fails without it) · 🟡 Should (important, not essential) · 🟢 Could (nice to have)
- Value: ⭐ to ⭐⭐⭐⭐⭐ — how much it moves us toward the big goal
- Effort 🛠️ and Risk ⚠️: 1 · 2 · 3 · 5 · 8 — bigger = more work / more chance to break something
- Status: TODO · DOING · BLOCKED · DONE · SKIPPED
- 🙋 Confirm first: the AI asks you before touching it

## 📸 Where we are today
- ✅ **Already good:** {1–3 bullets}
- 😬 **What's hurting:** {1–4 bullets, plain words, most important first}
- ⚠️ **Heads-up:** {anything honest the user must know, e.g. "part of this needs a backend we don't have" — or "None"}

## 📊 Quick summary
- 📋 Tasks: {N} (🔴 {n} · 🟡 {n} · 🟢 {n})
- ✅ Progress: 0 / {N} done
- 🛠️ Total effort points: 🔴 {n} · 🟡 {n} · 🟢 {n}
- 🚀 Quick wins: {ID}, {ID}, {ID}
- ⚠️ Handle with care: {ID} ({short reason}), {ID}

## 🤔 Decisions for you

### D-01: {Simple question?}
- **Why it matters:** {one or two lines}
- **Options:**
  - **A:** {option} — 👍 {pro} · 👎 {con}
  - **B:** {option} — 👍 {pro} · 👎 {con}
- 💡 **AI suggests:** {A/B}, because {reason}
- **Blocks:** {IDs}
- **Your answer:** PENDING

## ✅ Checklist: {Group name} {emoji}
> {One line: what this group is about. If it must come before/after another group, say why.}

- [ ] **{ID} · {What will be true when done}** — 🔴 Must
  - Value ⭐⭐⭐⭐⭐ (5) · Effort 🛠️ {n} · Risk ⚠️ {n} · ~{n} files
  - 💬 {Why it matters — benefit, 1–3 sentences, friendly and honest}
  - Needs: {IDs or —} · Decision: {D-xx or —} · 🙋 Confirm first: {Yes/No}
  - Status: TODO

<!-- Repeat items, sorted by Value (high → low), prerequisites just above the task that needs them.
     Repeat "## ✅ Checklist: ..." for each group. Use T-001 style IDs if there is only one checklist. -->

## 🅿️ Not doing now
- **{Idea}** — {honest reason: low value, too risky for now, out of scope, waiting on something}

---

# Part 2 — Vibe Coding Instructions 🤖 (for AI / coder)

> Humans can stop reading here. This part tells the AI or coder exactly how to do each checklist item.

## 2.1 North Star
- **Goal:** {precise goal}
- **Success criteria:** {measurable checks, e.g. "All pages pass axe with 0 serious issues", "LCP < 2.5s on mobile for top 5 pages"}
- **In scope:** {areas}
- **Out of scope:** {non-goals}
- **Constraints:** {stack, versions, deadlines, areas not to touch}
- **Guiding principles:** (every task must respect these)
  1. {e.g. Keep all current URLs working}
  2. {e.g. Use existing design tokens; no new colors}
  3. {e.g. No new libraries without asking}

## 2.2 Research Notes
| Source | Link | Checked | Version | Key rules we apply |
|---|---|---|---|---|
| {name} | {url} | {YYYY-MM-DD} | {e.g. WCAG 2.2} | {short} |

- **Conflicts / judgement calls:** {where sources disagree and what we chose — or "None"}

## 2.3 Repo Map
- **Stack:** {framework + version, language, styling, state, test tools}
- **Docs read:** {e.g. /docs/PROJECT_ARCHITECT.md, /docs/PLAN__x.md — or "None found"}
- **Areas the goal touches:**
  - `{path}` — {what it does} — ~{n} files — {shared by n places}
- **Patterns to follow:** {naming, folders, how styles/state/data are done}
- **Tests:** {what exists, how to run}
- **Already good — don't break:** {list}

## 2.4 Findings

### F-01: {Short title}
- **Area:**
- **Problem:**
- **Evidence:** `{path/file:line}` (or UNVERIFIED)
- **Source rule:** {link to Research Notes row, if any}
- **Impact if ignored:**
- **Tasks:** {IDs}

## 2.5 Execution Order & Blockers
- **Phase 1 — {name}:** {IDs} — {why first}
- **Phase 2 — {name}:** {IDs}
- **Blocking changes:** {changes other tasks depend on, e.g. "SEO-01 adds the shared meta helper used by SEO-03..05"}
- **Dependency notes:** {ID needs ID because ...}

## 2.6 Task Blocks

### {ID}: {Title}
- **Goal:** {one clear outcome}
- **Why:** {F-xx} — {one line}
- **Files (~{n}):**
  - `{path}` — {change | new}
- **Plan:**
  1. {step}
  2. {step}
- **Impact & blast radius:** {what else uses these files; what could break; who notices}
- **Depends on / blocks:** {IDs, D-xx}
- **🙋 Confirm first:** {No | Yes — reason}
- **Acceptance criteria:**
  - [ ] {checkable statement}
- **How to verify:** {commands, tests, manual checks, tools}
- **Do NOT:** {limits, e.g. "don't touch the checkout flow"}
- **Rollback:** {how to undo}
- **Scores:** Value {n} · Effort {n} · Risk {n} — {reason if Risk ≥ 5}
- **Work log:** —

<!-- One block per checklist item, same order as Part 1. -->

## 2.7 Working Rules
{Copy the "Execute mode — Working on the plan" rules from the skill here, word for word.}

## 2.8 Assumptions & Open Questions
- **Assumptions:** {mark UNVERIFIED if not confirmed}
- **Open questions:** {anything not yet a formal decision}

## 2.9 Change Log
| Date | Version | Change | By |
|---|---|---|---|
| {YYYY-MM-DD} | v1 | Created | AI |
