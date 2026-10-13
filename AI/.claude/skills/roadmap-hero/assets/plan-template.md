<!--
TEMPLATE for /docs/PLAN__{name}.md
- Keep every heading, in this order. Write "None" if a section is empty.
- Replace everything in {curly braces}. Delete these HTML comments in the final doc.
- Part 1 follows references/writing-style.md. Part 2 is for the AI/coder.
- Markdown rules (references/writing-style.md, "Markdown rules") apply to the whole doc.
- Every field gets real content. Write "None" only where nothing applies; for "Impact if ignored" say how small the impact is instead.
-->

# 🗺️ Plan: {Goal in plain words}

> **🎯 Big goal:** {1-2 sentences, plain English}
>
> **🤔 Why:** {benefit for users or the business}
>
> **🏁 Done means:** {how we'll know it worked - something you can see or measure}

- 📅 Created: {YYYY-MM-DD} · 🔄 Version: v1 · 📌 Status: Draft
- 🌿 Repo / branch / commit: {repo} / {branch} / {short commit or "not a git repo"}

{Optional: one short paragraph, e.g. which older docs this plan replaces. Delete if not needed.}

---

## Part 1 - The Checklist 👀 (for you)

### 👋 How to use this plan

1. Read the checklist below. Ticked boxes are done.
2. Answer the decisions in "🤔 Decisions for you". Just reply in chat, e.g. "D-01: A".
3. Ask the AI to start: `work on {ID}`, `do {ID} to {ID}`, or `next task`.

### 🔑 Legend

| Mark | Meaning |
| --- | --- |
| 🔴 🟡 🟢 | Must (goal fails without it) · Should (important) · Could (nice to have) |
| ⭐ to ⭐⭐⭐⭐⭐ | Value: how much it moves us toward the big goal |
| 🛠️ 1-8 | Effort: 1 · 2 · 3 · 5 · 8, bigger = more work |
| ⚠️ 1-8 | Risk: 1 · 2 · 3 · 5 · 8, bigger = more chance to break something |
| 🙋 | The AI explains first and waits for your "yes" |
| 🚧 ⛔ ⏭️ | Doing · Blocked (shows what it waits for) · Skipped (shows why) |

### 📸 Where we are today

- ✅ **Already good:**
  - {1-5 nested bullets}
- 😬 **What's hurting:**
  - {1-4 nested bullets, plain words, most important first}
- 📢 **Heads-up:** {anything honest the user must know, e.g. "part of this needs a backend we don't have" - or "None"}

### 📊 Quick summary

| Checklist | 🔴 | 🟡 | 🟢 | 🛠️ Effort | ✅ Done |
| --- | --- | --- | --- | --- | --- |
| {emoji} {Group name} | {n} | {n} | {n} | {sum} | 0 / {n} |
| **Total** | **{n}** | **{n}** | **{n}** | **{sum}** | **0 / {N}** |

- 🚀 **Quick wins:** {ID}, {ID}, {ID}
- 🧨 **Handle with care:** {ID} ({short reason}), {ID} ({short reason})
- ⛔ **Waiting on you:** {D-xx} ({n} tasks), {D-xx} ({n} tasks) - or "Nothing"

### 🤔 Decisions for you

#### D-01: {Simple question?}

{Why it matters - one or two short sentences.}

| Option | 👍 | 👎 |
| --- | --- | --- |
| **A:** {option} | {pro} | {con} |
| **B:** {option} | {pro} | {con} |

💡 **AI suggests A:** {reason}

**Blocks:** {IDs}
**Your answer:** PENDING

### ✅ Checklist: {Group name} {emoji}

{One line: what this group is about. If it must come before/after another group, say why.}

- [ ] 🔴 **{ID}** {What will be true when done}
  - ⭐⭐⭐⭐⭐ · 🛠️ {n} · ⚠️ {n} · 🙋
  - 💬 {Why it matters - benefit, 1-3 sentences, friendly and honest}

- [ ] 🟡 **{ID}** {What will be true when done}
  - ⭐⭐⭐⭐ · 🛠️ {n} · ⚠️ {n} · ⛔ {prerequisite IDs and/or D-xx}
  - 💬 {Why it matters}

<!-- Repeat items, sorted by Value (high to low), prerequisites just above the task that needs them.
     Score line: stars · 🛠️ n · ⚠️ n, then 🙋 only if confirm first, then a status tag only if not plain to-do.
     Repeat "### ✅ Checklist: ..." for each group. -->

### 🅿️ Not doing now

- **{Idea}:** {honest reason: low value, too risky for now, out of scope, waiting on something}

---

## Part 2 - Vibe Coding Instructions 🤖 (for AI / coder)

> Humans can stop reading here. This part tells the AI or coder exactly how to do each checklist item.

### 2.1 North Star

- **Goal:** {precise goal}
- **Success criteria:** {measurable checks, e.g. "All pages pass axe with 0 serious issues", "LCP < 2.5s on mobile for top 5 pages"}
- **In scope:** {areas}
- **Out of scope:** {non-goals}
- **Constraints:** {stack, versions, deadlines, areas not to touch}
- **Guiding principles:** (every task must respect these)
  1. {e.g. Keep all current URLs working}
  2. {e.g. Use existing design tokens; no new colors}
  3. {e.g. No new libraries without asking}

### 2.2 Research Notes

| Source | Checked | Version | Key rules we apply |
| --- | --- | --- | --- |
| [{name}]({url}) | {YYYY-MM-DD} | {e.g. WCAG 2.2} | {short} |

- **Conflicts / judgement calls:** {where sources disagree and what we chose - or "None"}

### 2.3 Repo Map

- **Stack:** {framework + version, language, styling, state, test tools}
- **Docs read:** {e.g. /docs/PROJECT_ARCHITECT.md, /docs/PLAN__x.md - or "None found"}
- **Areas the goal touches:**
  - `{path}` - {what it does} - {shared by n places}
- **Patterns to follow:** {naming, folders, how styles/state/data are done}
- **Tests:** {what exists, how to run}
- **Already good - don't break:** {list}

### 2.4 Findings

#### F-01: {Short title}

- **Area:**
- **Problem:**
- **Evidence:** `{path/file:line}` (or UNVERIFIED)
- **Source rule:** {Research Notes source name, or "None"}
- **Impact if ignored:**
- **Tasks:** {IDs}

### 2.5 Execution Order & Blockers

- **Phase 1 - {name}:** {IDs} - {why first}
- **Phase 2 - {name}:** {IDs}
- **Blocking changes:** {changes other tasks depend on, e.g. "SEO-001 adds the shared meta helper used by SEO-003 to SEO-005"}
- **Dependency notes:** {ID needs ID because ...}

### 2.6 Task Blocks

#### {ID}: {Title}

- **Goal:** {one clear outcome}
- **Why:** {F-xx} - {one line}
- **Files:**
  - `{path}` - {change | new}
- **Plan:**
  1. {step}
  2. {step}
- **Impact & blast radius:** {what else uses these files; what could break; who notices}
- **Depends on / blocks:** {IDs, D-xx}
- **🙋 Confirm first:** {No | Yes - reason}
- **Acceptance criteria:**
  - [ ] {checkable statement}
- **How to verify:** {commands, tests, manual checks, tools}
- **Do NOT:** {limits, e.g. "don't touch the checkout flow"}
- **Rollback:** {how to undo}
- **Scores:** Value {n} · Effort {n} · Risk {n} - {reason if Risk >= 5}
- **Work log:** None yet

<!-- One block per checklist item, same order as Part 1. -->

### 2.7 Working Rules

{Copy the "Execute mode - Working on the plan" rules from the skill here, word for word. Turn their headings into ####.}

### 2.8 Assumptions & Open Questions

- **Assumptions:** {mark UNVERIFIED if not confirmed}
- **Open questions:** {anything not yet a formal decision}

### 2.9 Change Log

| Date | Version | Change | By |
| --- | --- | --- | --- |
| {YYYY-MM-DD} | v1 | Created | AI |
