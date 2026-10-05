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
