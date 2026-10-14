# src/app - Routes

`expo-router` owns this folder. Every file in it becomes a route. It holds two kinds of file: screens, which are the route pages, and `_layout.tsx` files, which are the layout routes. A screen is layout and core structure only.

## Structure

```text
app/
  _layout.tsx           the root: providers, splash screen, session gate
  (auth)/
    _layout.tsx         the auth group's navigator
    sign-in.tsx         a screen in the auth group
  (app)/
    _layout.tsx         the signed-in navigator
    (tabs)/
      _layout.tsx       the tab bar
      index.tsx         dashboard
      sales/            a feature with more than one screen
        index.tsx       SaleListScreen
        [saleId].tsx    SaleDetailScreen, a dynamic route
  +not-found.tsx        the 404 screen
```

- Never put a helper, a hook, or a plain component here. It would turn into a route the user can navigate to.
- One file per screen. When a feature has more than one screen, group them in a folder with the same name as the feature's folder in `components/features/`.
- Group folders use parentheses: `(auth)`, `(app)`, `(tabs)`. They organise routes without adding a URL segment.
- Dynamic segments are `camelCase` and say what they hold: `[saleId]`, not `[id]`.
- Every screen component ends in `Screen`: `SaleListScreen`, `DashboardScreen`. It is the file's default export, which is what the router renders.

## Rules

### Screens

- A screen reads the route params, passes them to its sections as props, sets the header title, and places the feature's sections.
- Read params with the typed hooks, `useLocalSearchParams`. Set the title with `Stack.Screen` options.
- The layout picks the navigator. A screen never builds its own navigator and never wraps itself in a layout.
- No state, no data fetching, no `fetch`, no calculation, and no business rule. The sections own them.
- State that must be restored from a link is the exception. If a deep link or a notification has to open a screen on a given tab or filter, that value lives in the route params, and the screen reads it to choose the section. Everything else stays in `useState`: the stack keeps a screen mounted while the user goes back and forth, so its local state survives.

### Layouts

- A `_layout.tsx` holds a navigator: `Stack`, `Tabs`, or `Slot`. It places the shell parts from `components/layouts/`, the way a screen places a feature's sections.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.
- The session and permissions live in a store and are read where they are needed. Don't pass them down through the layout.
- Providers are mounted once, in the root `_layout.tsx`: the query client, the theme, the safe area, and the gesture handler when the project uses it. Context is for mounting a library's provider here, never for holding app state - that goes in a store.
- Each layout sets an error boundary by exporting `ErrorBoundary` with a fallback from `components/shared/`. The loading state belongs to the sections, not the layout.

### Gating

- Auth and onboarding checks belong in a `_layout.tsx`, never in a screen. Use `Stack.Protected` when the pinned SDK has it. Otherwise use `<Redirect>` in the layout.
- A screen never redirects itself based on session state. If it did, the user would see the screen flash before being pushed away.
- Hold the splash screen until everything the first render depends on has resolved: the stored session, a persisted store, the language, the theme, the fonts. A gate that runs on a half-loaded state will bounce the user.
- A 401 clears the session. `api/client.ts` reports it through a handler the root layout registers once, the root layout clears the session store, and the gate then moves the user to sign-in. Nothing navigates from `api/`.
- To hide a single element, use `<Can>` from `components/shared/`.

### Navigation

- Navigate with the typed router. Never build a path string by hand.
- A modal or a sheet is a route in the layout's navigator with a `presentation` option, not a component opened from inside a screen.

### Headers

- Decide once, in the layout, whether screens use the native header or render their own.
- Don't mix the two inside one navigator.

## Boundaries

- Follow the `app/` rows in the import table in `src/CLAUDE.md`. A screen imports sections, never another screen.
- Not here: sections, widgets, helpers, hooks, and shell parts. Sections live in `components/features/{feature}/`, shell parts in `components/layouts/`.

## Existing Screens

Read this list to find the screen for a route without opening files. When you add, rename, or remove a screen, or change its route, update this list in the same change.

| File | Route | Feature |
|------|-------|---------|

## Existing Layouts

Read this list before adding a layout. When you add, rename, or remove a layout, or change which screens use it, update this list in the same change.

| File | Navigator | Used by |
|------|-----------|---------|
