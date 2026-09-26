# src/app - Routes and Screens

`expo-router` owns this folder. Every file in it becomes a route. Never put a helper, a hook, or a
plain component here - it would turn into a screen the user can navigate to.

```
app/_layout.tsx           the root navigator, providers, and gating
app/(auth)/sign-in.tsx    a screen inside the auth group
app/(app)/(tabs)/         the tab bar and its screens
app/sale/[saleId].tsx     a dynamic route
```

## The Screen

- A route file default-exports its screen. This is the only default export in the project.
- The screen provides the page structure, wires sections together, and owns the top-level data
  call. Keep logic to a minimum.
- Everything below it lives in `components/{feature}/`. See `components/CLAUDE.md`.
- No `fetch`, no calculation, and no business rule inside a route file.

## Navigation

- Group folders use parentheses: `(auth)`, `(app)`, `(tabs)`. They organise routes without adding
  a URL segment.
- Dynamic segments are `camelCase` and say what they hold: `[saleId]`, not `[id]`.
- `_layout.tsx` files hold the navigators. A screen never builds its own navigator.
- Navigate with the typed router. Never build a path string by hand.

## Gating

- Auth checks and onboarding checks belong in a `_layout.tsx`, not in a screen.
- A screen never redirects itself based on session state. If it did, the user would see the screen
  flash before being pushed away.
- Hold the splash screen until everything the first render depends on has resolved - the stored
  session, the language, the theme. A gate that runs on a half-loaded state will bounce the user.

## Headers

- Decide once, in the layout, whether screens use the native header or render their own.
- Don't mix the two inside one navigator.
