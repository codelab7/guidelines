# src/hooks - Custom Hooks

Hooks reusable across features, for example `use-debounce.ts`.

## Structure

```text
hooks/
  use-debounce.ts      exports useDebounce
  use-is-mobile.ts     exports useIsMobile, true below the md breakpoint (768px)
  use-current-user.ts  exports useCurrentUser, built on query hooks from api/
```

- One hook per file. File in `kebab-case`, hook in `camelCase`.

## Rules

- Before you write a hook, check the UI library's hooks (for example `@mantine/hooks`) and es-toolkit. Write one only when none covers it.
- If it uses React state, effects, context, or another hook, it is a hook. Otherwise it is a util and goes in `utils/`.
- A hook here may call the query hooks in `api/` when several features need the combined result.
- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.
- Every effect that subscribes, sets a timer, or starts a request returns a cleanup: remove the listener, clear the timer, abort the request.

## Boundaries

- Follow the `hooks/` row in the import table in `src/CLAUDE.md`.
- Not here: a hook used by one feature stays in its folder under `components/features/{feature}/`.
- Not here: a pure helper with no React in it goes in `utils/`.

## Existing Hooks

Read this list before writing a hook - the one you need may already be here. When you add, rename, or remove a hook, or change its arguments or return value, update this list in the same change.

| File | Hook | What it does |
|------|------|--------------|
