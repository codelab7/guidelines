# src/hooks - Custom Hooks

Hooks reusable across features, for example `use-debounce.ts`.

## Structure

```text
hooks/
  use-debounce.ts    exports useDebounce
  use-is-mobile.ts   exports useIsMobile
```

- One hook per file. File in `kebab-case`, hook in `camelCase`.

## Rules

- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.

## Boundaries

- Not here: a hook used by one feature stays in its folder under `components/features/{feature}/`.
- Not here: a pure helper with no React in it goes in `utils/`.

## Existing Hooks

Read this list before writing a hook - the one you need may already be here. When you add,
rename, or remove a hook, or change its arguments or return value, update this list in the same
change.

| File | Hook | What it does |
|------|------|--------------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### HOOK-1. Correction - shadcn ships use-mobile.ts

The shadcn sidebar installs `hooks/use-mobile.ts`, which exports `useIsMobile`. This file's example
is `use-is-mobile.ts`. The agent may create a second hook or rename the generated one.

- A: Keep shadcn's `use-mobile.ts` and fix the example here.
- B: Rename shadcn's file to `use-is-mobile.ts` and record it.

Recommended: A. Don't rename generated files.

**Decision:**

### HOOK-2. Question - Data hooks here

Can a hook here call `api/`, for example `use-current-user.ts`? It depends on API-1: with TanStack
Query, query hooks may live in `api/` instead.

- A: Yes, a hook here may call `api/` when several features need it.
- B: No. Data hooks live in `api/` (API-1 option A).

Recommended: Follows API-1.

**Decision:**

### HOOK-3. Decision aid - Hook or util

The line between `hooks/` and `utils/` is implied, not stated.

- Suggested: if it uses React state, effects, context, or another hook, it is a hook. Otherwise it
  is a util.

Recommended: Adopt.

**Decision:**

### HOOK-4. Missing - Effect cleanup

Shared hooks often add listeners, timers, or requests. Nothing says to clean them up.

- Suggested: every effect that subscribes, sets a timer, or starts a request returns a cleanup
  (remove listener, clear timer, abort the request).

Recommended: Adopt.

**Decision:**
