# src/layouts - Page Shells

The shells a page renders inside, such as `auth-layout.tsx` and `user-layout.tsx`. Each layout is
a layout route: the router renders it, and it renders the page through `<Outlet />`.

## Structure

```text
layouts/
  auth-layout.tsx
  user-layout.tsx
```

- One file per layout. No subfolders here.
- The shell's parts - sections such as `app-sidebar.tsx` and `app-header.tsx`, widgets such as
  `user-menu.tsx` - live in `components/layouts/`. The layout only places them, the way a page
  places a feature's sections.

## Rules

- The router picks the layout for each route in `router.tsx`. A page never wraps itself in a
  layout.
- The session and permissions live in a store and are read where they are needed. Don't pass them
  down through the layout.
- Auth redirects happen in the router, not in the layout: `beforeLoad` in TanStack Router, a
  loader in React Router. To hide one element, use `<Can>` from `components/shared/`.
- Each layout sets an error boundary and a loading fallback around its outlet: the router's error
  and pending components, or an error boundary plus `Suspense`.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.

## Boundaries

- Follow the `layouts/` row in the import table in `src/CLAUDE.md`. Never import from a feature.
- Not here: shell parts and shell state live in `components/layouts/`.

## Existing Layouts

Read this list before adding a layout. When you add, rename, or remove a layout, or change which
pages use it, update this list in the same change.

| File | Used by |
|------|---------|
