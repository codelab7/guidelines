# src/components/layouts - Layout Components

The parts a layout is built from: the sidebar, header, footer, and the pieces inside them. The
layout files themselves live in `src/layouts/` and only place these components.

## Rules
- Only layout-related components go here. A component used by a feature goes in `features/` or `shared/`.
- Sections sit directly in the folder. Small pieces go in `widgets/`, the same as a feature.
- Shell state, such as whether the sidebar is collapsed, lives in these sections, not in the layout file.
- Import from `shared/` and `ui/` only. Never from a feature.

```
components/layouts/side-bar.tsx            a section: shell logic and state
components/layouts/header.tsx              another section
components/layouts/widgets/user-menu.tsx   a small piece used only by the shell
```
