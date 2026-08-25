# src/hooks - Custom Hooks

- Only hooks reusable across features live here. A hook used by one feature stays in that
  feature's folder.
- One hook per file. File in `kebab-case`, hook in `camelCase`: `use-debounce.ts` exports
  `useDebounce`.
- Name starts with `use`.
- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.
- Keep hooks thin. A hook wires state and effects together. The calculation belongs in `utils/`
  and the request belongs in `api/`.
- A hook that needs a platform-specific version ships a `.ios.ts` / `.android.ts` sibling instead
  of branching on `Platform.OS` inside the body.
- Read this folder before writing a new hook. The one you need often already exists.
