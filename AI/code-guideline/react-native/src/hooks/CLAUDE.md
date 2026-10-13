# src/hooks - Custom Hooks

Hooks reusable across features, for example `use-debounce.ts`.

## Structure

```text
hooks/
  use-debounce.ts          exports useDebounce
  use-current-user.ts      exports useCurrentUser, built on query hooks from api/
  use-refetch-on-focus.ts  exports useRefetchOnFocus, refetches a query when its screen regains focus
```

- One hook per file. File in `kebab-case`, hook in `camelCase`. The name starts with `use`.

## Rules

- Before you write a hook, check the UI kit's hooks, `expo-router`'s hooks (`useFocusEffect`, `useLocalSearchParams`), React Native's (`useColorScheme`, `useWindowDimensions`), and es-toolkit. Write one only when none covers it.
- If it uses React state, effects, context, or another hook, it is a hook. Otherwise it is a util and goes in `utils/`.
- A hook here may call the query hooks in `api/` when several features need the combined result.
- Keep hooks thin. A hook wires state and effects together. The calculation belongs in `utils/`, the request in `api/`, and the native call in `device/`.
- No JSX in a hook.
- Return a typed object or tuple, never an untyped one.
- Every effect that subscribes, sets a timer, or starts a request returns a cleanup: remove the listener, clear the timer, abort the request. In React Native this includes `AppState`, `Keyboard`, `Linking`, `BackHandler`, and network listeners.
- Work that should run only while a screen is on top uses `useFocusEffect`, not `useEffect`. A screen in a stack stays mounted underneath the next one.
- A hook that needs a platform-specific version ships a `.ios.ts` / `.android.ts` sibling instead of branching on `Platform.OS` inside the body.

## Boundaries

- Follow the `hooks/` row in the import table in `src/CLAUDE.md`.
- Not here: a hook used by one feature stays in its folder under `components/features/{feature}/`.
- Not here: a pure helper with no React in it goes in `utils/`.

## Existing Hooks

Read this list before writing a hook - the one you need may already be here. When you add, rename, or remove a hook, or change its arguments or return value, update this list in the same change.

| File | Hook | What it does |
|------|------|--------------|
