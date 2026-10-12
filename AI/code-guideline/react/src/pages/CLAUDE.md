# src/pages - Pages

One file per route page. A page is layout and core structure only.

## Structure

```text
pages/
  dashboard.tsx       a feature with a single page
  sales/              a feature with more than one page
    sale-list.tsx
    sale-detail.tsx
  not-found.tsx       the 404 page
  error.tsx           the generic error page
```

- One file per route page. When a feature has more than one page, group them in a folder with the same name as the feature's folder in `components/features/`.
- Every page component ends in `Page`: `SaleListPage`, `DashboardPage`. It is the file's default export, so the router can lazy-load it.

## Rules

- A page reads the path params, passes them to its sections as props, sets the document title, and places the feature's sections.
- The router picks the layout. A page never wraps itself in one.
- No state and no data fetching. The sections own both.
- State that belongs in the URL is the exception. Tab state lives in the URL search params, and the page reads it to choose the section. A section that owns filters or pagination reads and writes its own search params.
- Every page is lazy-loaded through the router.

## Boundaries

- Follow the `pages/` row in the import table in `src/CLAUDE.md`.
- Not here: sections, widgets, helpers, and hooks. They live in `components/features/{feature}/`.

## Existing Pages

Read this list to find the page for a route without opening files. When you add, rename, or remove a page, or change its route, update this list in the same change.

| File | Route | Feature |
|------|-------|---------|
