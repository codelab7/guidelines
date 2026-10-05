# src/layouts - Page Shells

The shells a page renders inside, such as `auth-layout.tsx` and `user-layout.tsx`.

## Structure

```text
layouts/
  auth-layout.tsx
  user-layout.tsx
```

- One file per layout. No subfolders here.
- The shell's parts - sections such as `side-bar.tsx` and `header.tsx`, widgets such as
  `user-menu.tsx` - live in `components/layouts/`. The layout only places them, the way a page
  places a feature's sections.

## Rules

- Read the session and permission context here once and pass what is needed downwards.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.

## Boundaries

- Import from `components/layouts/`, `shared/`, and `ui/`. Never from a feature.
- Not here: shell parts and shell state live in `components/layouts/`.

## Existing Layouts

Read this list before adding a layout. When you add, rename, or remove a layout, or change which
pages use it, update this list in the same change.

| File | Used by |
|------|---------|
