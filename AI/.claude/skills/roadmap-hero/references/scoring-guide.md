# Scoring Guide

How to name, score, sort and flag tasks. Used in Create mode, Step 5 — and whenever a new task is added later.

## Contents

1. IDs
2. Priority
3. Value (business value)
4. Effort and Risk (Fibonacci)
5. Splitting
6. Sorting
7. Confirm first
8. Status
9. Being honest

---

## 1. IDs

| Thing | Format | Example |
|---|---|---|
| Task | 3 UPPERCASE letters + `-` + 3 digits | `SEO-001`, `NAV-012`, `ACC-003` |
| Decision | `D-01`, `D-02`... | `D-02` |
| Finding | `F-01`, `F-02`... | `F-05` |

- Every task ID has exactly this shape, even when the plan has only one checklist. One fixed shape lines up neatly in the checklist, is easy to type ("work on NAV-004"), and never makes the reader wonder whether `SEO-1`, `SEO-01` and `SEO-001` are different things.
- One prefix per checklist group. Pick 3 letters that read as a word or a clear short form: `SEO`, `ACC` (accessibility), `MOB`, `PRF` (performance), `NAV`, `API`, `SEC`, `PSH` (push), `SYC` (sync). For a single-checklist plan, take the prefix from the goal.
- Numbers start at `001` in each group.
- Decisions and findings keep their short `D-01` / `F-01` shape on purpose: they are not tasks, and the different shape stops anyone from asking the AI to "work on" a decision.
- IDs are forever. Never reuse or renumber them. New tasks get the next free number, even if it means `SEO-012` sits above `SEO-003` after sorting.
- Plans written before this format may use other shapes (`SEO-01`, `T-003`). Keep those IDs as they are; don't rename them.

## 2. Priority

| Label | Meaning |
|---|---|
| 🔴 **Must** | The goal fails without it, or it is a serious bug or security hole |
| 🟡 **Should** | Important and valuable, but the goal can be reached without it |
| 🟢 **Could** | Nice to have |

Ideas that are "Won't do now" don't go in the checklist. They go in the **🅿️ Not doing now** section with a reason, so they aren't forgotten.

## 3. Value (business value)

Value = how much finishing this task moves us toward the big goal. In Part 1 show it as stars only (the number goes in Part 2 → Scores).

| Stars | Meaning |
|---|---|
| ⭐⭐⭐⭐⭐ (5) | Core to the goal. Big, visible win for users or the business |
| ⭐⭐⭐⭐ (4) | Strong contributor |
| ⭐⭐⭐ (3) | Clear help |
| ⭐⭐ (2) | Small help |
| ⭐ (1) | Tiny polish |

- Priority says "do we need it?". Value says "how much does it help?". They usually agree (Musts are mostly 4–5) but not always — a Must can be a 3 if it's a boring but required base step.
- Write the "Why it matters" line as a user or business benefit, not a tech change.
  - Good: "People stop getting logged out in the middle of checkout."
  - Bad: "Refactor token refresh."

## 4. Effort and Risk (Fibonacci)

Use only 1, 2, 3, 5, 8. 13 is a signal to split.

| Score | Effort (how much work) | Risk (chance of breaking something) |
|---|---|---|
| 1 | Minutes, tiny change | Almost zero |
| 2 | Under an hour | Very low, one isolated spot |
| 3 | A few hours | Low, a few places |
| 5 | About a day | Medium — shared code, several screens |
| 8 | Several days | High — core flow, data, auth, payments, public API |
| 13 | Too big → split | Too dangerous → split |

- Use the sizing from the research step (see `research-guide.md` §5).
- Raise Risk when: files are widely shared, tests are missing, the change is hard to undo, or users would notice a mistake right away.
- Score honestly. Don't default to 3.
- Any Risk of 5 or more needs a one-line reason in the Part 2 task block.

## 5. Splitting

A task scoring 13 on Effort or Risk must be split before the doc is final. Good ways to split:
- By area (page by page, component by component)
- By step (prepare → switch → clean up)
- Safe part first, risky part second (e.g. add the new path behind a flag, then switch over)

Each piece must still give one clear outcome.

## 6. Sorting

The human works top to bottom, so the list must make sense in that order.

1. Inside each checklist, sort by **Value**, high to low.
2. Ties: Must before Should before Could, then lower Effort first (quick wins rise).
3. **Prerequisites:** if a task needs another task first, move the prerequisite above it. When one prerequisite serves several tasks, it sits just above the first of them. While the prerequisite isn't done, the later task carries a `⛔ {ID}` tag (see §8); the full dependency list lives in Part 2 → Depends on / blocks. A list that can't be done top to bottom is broken.
4. With several checklists, put the group whose best task has the highest Value first (on a tie, the group with more Musts), unless one group must come before another (then say why at the top of the group).

The exact technical order (phases) also goes in Part 2 → Execution Order.

## 7. Confirm first

A task gets the 🙋 mark on its score line when any of these is true (no mark means no need to ask):
- Risk is 5 or more
- It touches auth, login, sessions or permissions
- It touches payments or money
- It touches the database: schema, migrations, or stored data
- It deletes or moves data or files users rely on
- It changes a public API, URLs, or anything other systems call
- It changes shared core code used in many places
- It changes build, deploy, CI or environment config
- It adds or removes a library
- It is hard to undo

In Part 2, write the reason next to "Confirm first: Yes", and "No" for everything else.

## 8. Status

Part 2 and the Execute rules use the words `TODO` · `DOING` · `BLOCKED` · `DONE` · `SKIPPED`. In Part 1 they show like this:

| Status | In Part 1 |
|---|---|
| TODO | `- [ ]` and no tag |
| DOING | `- [ ]` and `🚧 Doing` |
| BLOCKED | `- [ ]` and `⛔ {what it waits for}`, e.g. `⛔ PUS-001, D-02` |
| DONE | `- [x]` and no tag |
| SKIPPED | `- [ ]` and `⏭️ Skipped: {reason}` |

- A task waiting on a PENDING decision, or on a dependency that isn't done, is `BLOCKED`. Its tag lists only its own direct prerequisites and decisions that are still missing, not the ones those depend on, so it shrinks as things get done and disappears when nothing is left.
- `SKIPPED` always has a reason (e.g. "split into SEO-009, SEO-010", "not needed after D-02").
- Never delete a task.

## 9. Being honest

- If something isn't worth the effort, say so and move it to "Not doing now".
- If you're unsure about a finding, mark it `UNVERIFIED` and lower confidence in its value.
- Don't inflate Value to make the plan look exciting. Don't shrink Risk to make it look easy.
- If the goal can't be fully reached with this repo (e.g. needs a backend that doesn't exist), say it plainly at the top of Part 1.
