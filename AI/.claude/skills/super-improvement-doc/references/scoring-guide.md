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
| Task, one checklist | `T-001`, `T-002`... | `T-004` |
| Task, several checklists | Short UPPERCASE prefix per group + two digits | `SEO-01`, `A11Y-03`, `NAV-02` |
| Decision | `D-01`, `D-02`... | `D-02` |
| Finding | `F-01`, `F-02`... | `F-05` |

- Use one checklist when the plan is small or has one theme. Use several when the work falls into clear groups (by area, page, or kind of change).
- Prefixes: 2–5 letters, easy to read (`SEO`, `A11Y`, `MOB`, `PERF`, `NAV`, `API`).
- IDs are forever. Never reuse or renumber them — new tasks get the next free number, even if it means `SEO-12` sits above `SEO-03` after sorting.

## 2. Priority

| Label | Meaning |
|---|---|
| 🔴 **Must** | The goal fails without it, or it is a serious bug or security hole |
| 🟡 **Should** | Important and valuable, but the goal can be reached without it |
| 🟢 **Could** | Nice to have |

Ideas that are "Won't do now" don't go in the checklist. They go in the **🅿️ Not doing now** section with a reason, so they aren't forgotten.

## 3. Value (business value)

Value = how much finishing this task moves us toward the big goal. Show it as stars plus a number.

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

- Use the file count from the research step (see `research-guide.md` §5).
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
3. **Prerequisites:** if a task needs another task first, move the prerequisite to sit just above it, and write `Needs: X` on the later one. A list that can't be done top to bottom is broken.
4. With several checklists, put the group with the highest-value tasks first, unless one group must come before another (then say why at the top of the group).

The exact technical order (phases) also goes in Part 2 → Execution Order.

## 7. Confirm first

Every task shows `🙋 Confirm first: Yes` or `No`. Set **Yes** when any of these is true:
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

In Part 2, write the reason next to "Confirm first: Yes".

## 8. Status

`TODO` · `DOING` · `BLOCKED` · `DONE` · `SKIPPED`

- A task waiting on a PENDING decision, or on a dependency that isn't done, is `BLOCKED`.
- `SKIPPED` always has a reason (e.g. "Split into SEO-09, SEO-10", "Not needed after D-02").
- Never delete a task.

## 9. Being honest

- If something isn't worth the effort, say so and move it to "Not doing now".
- If you're unsure about a finding, mark it `UNVERIFIED` and lower confidence in its value.
- Don't inflate Value to make the plan look exciting. Don't shrink Risk to make it look easy.
- If the goal can't be fully reached with this repo (e.g. needs a backend that doesn't exist), say it plainly at the top of Part 1.
