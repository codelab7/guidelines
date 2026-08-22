# src/layouts/sections - Layout Sections

- Large parts of a shell: `side-bar.tsx`, `header.tsx`.
- Used by layouts only. A section that belongs to a page goes in `pages/{module}/sections/`.
- Holds the layout's own state, for example whether the sidebar is collapsed.
- Compose from `layouts/widgets/` and `components/`.
