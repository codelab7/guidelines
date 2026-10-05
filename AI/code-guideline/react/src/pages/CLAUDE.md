# src/pages - Pages

One file per route page. A page is layout and core structure only.

## Structure

- One file per route page.
- When a domain has more than one page, group them in a folder named for that domain.

## Rules

- A page reads the route params, picks the layout, and places the feature's sections.
- No state and no data fetching. The sections own both.

## Boundaries

- Import from `layouts/` and `components/features/{feature}/`.
- Not here: sections, widgets, helpers, and hooks. They live in `components/features/{feature}/`.

## Existing Pages

Read this list to find the page for a route without opening files. When you add, rename, or
remove a page, or change its route, update this list in the same change.

| File | Route | Feature |
|------|-------|---------|
