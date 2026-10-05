# src/components/layouts - Layout Components

The parts a layout is built from: the sidebar, header, footer, and the pieces inside them. The
layout files themselves live in `src/layouts/` and only place these components.

## Structure

```text
components/layouts/
  side-bar.tsx            a section: shell logic and state
  header.tsx              another section
  widgets/user-menu.tsx   a small piece used only by the shell
```

- Sections sit directly in the folder. Small pieces go in `widgets/`, the same as in a feature.

## Rules

- Only layout-related components go here.
- Shell state, such as whether the sidebar is collapsed, lives in these sections, not in the
  layout file.

## Boundaries

- Import from `shared/` and `ui/` only. Never from a feature.
- Not here: a component used by a feature goes in `features/` or `shared/`. A layout file goes in
  `src/layouts/`.

## Existing Layout Parts

Read this list before opening the files here. When you add, rename, or remove a part, or change
what it does, update this list in the same change.

| File | Role | What it does |
|------|------|--------------|
