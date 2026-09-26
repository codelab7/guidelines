# src/hooks - Custom Hooks

- Only hooks reusable across features live here. A hook used by one feature stays in its folder
  under `components/features/{feature}/`.
- One hook per file. File in `kebab-case`, hook in `camelCase`: `use-debounce.ts` exports
  `useDebounce`.
- Name starts with `use`.
- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.
- Read this folder before writing a new hook. `use-is-mobile.ts` and `use-appearance.ts` already
  exist in most projects.
