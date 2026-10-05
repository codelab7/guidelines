# src/hooks - Custom Hooks

## Rules
- Only hooks reusable across features live here. A hook used by one feature stays in its folder
  under `components/features/{feature}/`.
- One hook per file. File in `kebab-case`, hook in `camelCase`: `use-debounce.ts` exports `useDebounce`.
- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.
- The Existing Hooks part contains what we have already. Keep it up to date in case of change in hooks.

## Existing Hooks