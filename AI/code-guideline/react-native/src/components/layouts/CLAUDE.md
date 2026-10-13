# src/components/layouts - Shell Components

The parts the app shell is built from: the tab bar, the header, the drawer, and the pieces inside them. The `_layout.tsx` files themselves live in `src/app/` and only place these components.

## Structure

```text
components/layouts/
  nav-items.ts            the route list with its labels and icons
  app-tab-bar.tsx         a section: shell logic and state
  app-header.tsx          another section
  widgets/user-menu.tsx   a small piece used only by the shell
```

- Sections sit directly in the folder. Small pieces go in `widgets/`, the same as in a feature.
- Name shell parts with an `app-` prefix, so they don't clash with the UI kit's own components, such as a `TabBar`.
- The navigation table - the route list, its labels and icons - lives flat at the folder root, in `nav-items.ts`. Both the tab bar and the navigator read from that one table.

## Rules

- Only shell-related components go here. This is the shell, not screen content.
- Shell sections may load data, such as the current user or a notification count, through the query hooks in `api/` - the same as feature sections.
- Mount a shell section once, in the navigator. Never re-create it per screen. A route that needs the shell's chrome without being a registered tab reuses the section component. Never fork it.
- A section reads the navigation table. It does not define it.
- Shell state, such as whether the drawer is open: use the navigator's own state when it has one. Otherwise keep it in the section, or in a store with `persist` when it must survive an app restart. Never in the layout file.
- Respect the safe area in the header and the tab bar. Keep the tab bar's touch targets at least 44pt.

## Boundaries

- Sections follow the Sections row and widgets the Widgets row in the import table in `src/CLAUDE.md`. Never import from a feature.
- Not here: a component used by a feature goes in `features/` or `shared/`. A `_layout.tsx` file goes in `src/app/`.

## Existing Layout Parts

Read this list before opening the files here. When you add, rename, or remove a part, or change what it does, update this list in the same change.

| File | Role | What it does |
|------|------|--------------|
