# src/components/layouts - Layout Components

The parts a layout is built from: the sidebar, header, footer, and the pieces inside them. The layout files themselves live in `src/layouts/` and only place these components.

## Structure

```text
components/layouts/
  app-sidebar.tsx         a section: shell logic and state
  app-header.tsx          another section
  widgets/user-menu.tsx   a small piece used only by the shell
```

- Sections sit directly in the folder. Small pieces go in `widgets/`, the same as in a feature.
- Name shell parts with an `app-` prefix, so they don't clash with the UI library's own components, such as a `Sidebar`.

## Rules

- Only layout-related components go here.
- Shell sections may load data, such as the current user or a notification count, through the query hooks in `api/` - the same as feature sections.
- Shell state, such as whether the sidebar is collapsed: use the UI library's shell state when it has one, for example Mantine's `AppShell`. Otherwise keep it in the section, or in a store with `persist` when it must survive a reload. Never in the layout file.

## Boundaries

- Sections follow the Sections row and widgets the Widgets row in the import table in `src/CLAUDE.md`. Never import from a feature.
- Not here: a component used by a feature goes in `features/` or `shared/`. A layout file goes in `src/layouts/`.

## Existing Layout Parts

Read this list before opening the files here. When you add, rename, or remove a part, or change what it does, update this list in the same change.

| File | Role | What it does |
|------|------|--------------|
