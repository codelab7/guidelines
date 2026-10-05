# src/utils - Shared Helpers

Shared helper functions. Read this folder before writing any helper - the one you need often
already exists.

## Structure

```text
utils/
  number.enums.ts       number and currency formatting
  date.enums.ts         dates
  validation.utils.ts   the single home for validation helpers
```

- Group by topic and name the file for what it handles.
- `cn`, the class name merger, lives here and is the standard for conditional classes.

## Rules

- Pure functions only: same input, same output, no side effects.
- Each validation helper is a pure function returning a boolean or a simple typed result. Add a
  reusable rule to `validation.utils.ts` instead of redefining it in a component.
- Never duplicate a validation rule anywhere else in the codebase.

## Boundaries

- No React, no hooks, no component state. Anything that needs them goes in `hooks/`.
- Not here: a helper used by one feature stays in its `{feature}-utils.ts` under
  `components/features/{feature}/`.

## Existing Helpers

Read this list before writing a helper. When you add, rename, or remove a helper, or change its
arguments or return value, update this list in the same change.

| File | Helpers | What they do |
|------|---------|--------------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### UTIL-1. Correction - The .enums.ts suffix

Open in the README checklist: formatters are `number.enums.ts` and `date.enums.ts`, but they hold
no enum. The agent may put enums there, or name new helpers `.enums.ts`.

- A: `.utils.ts` for every file: `number.utils.ts`, `date.utils.ts`, `validation.utils.ts`,
  `cn.utils.ts`.
- B: No suffix: `number.ts`, `date.ts`.

Recommended: A.

**Decision:**

### UTIL-2. Question - Where cn lives

"`cn` lives here" does not name the file, and shadcn expects it in `lib/utils.ts`. See UI-1.

Recommended: Follows UI-1 and UTIL-1.

**Decision:**

### UTIL-3. Correction - "Read this folder before writing any helper" never loads

The rule sits in a file that loads only while the agent is already in `utils/`. When it writes a
helper inside a feature, it never sees this. See SRC-1.

Recommended: Move the rule to `src/CLAUDE.md`, as in SRC-1.

**Decision:**

### UTIL-4. Question - Validation helpers vs a schema library

If forms use zod (FEAT-6), most rules live in schemas, not in boolean helpers. Then
`validation.utils.ts` either holds shared zod pieces or shrinks a lot.

- A: `validation.utils.ts` holds shared zod schema pieces (phone, email, money) that forms combine.
- B: Keep boolean helpers, and schemas call them.

Recommended: A, if FEAT-6 picks zod.

**Decision:**

### UTIL-5. Decision aid - Before writing a helper

The agent may write its own `groupBy` or date formatter.

- Suggested order: native JavaScript, then lodash, then date-fns, then an existing helper here.
  Write a new one only when none of them covers it.

Recommended: Adopt.

**Decision:**

### UTIL-6. Missing - Tests for helpers

Pure functions are the cheapest code to test. Depends on SRC-13.

- A: Every helper here gets a test file next to it.
- B: No rule.

Recommended: A, if SRC-13 picks Vitest.

**Decision:**
