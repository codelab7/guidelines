# src/layouts/sections - Layout Sections

- Large parts of a shell: `side-bar.tsx`, `header.tsx`.
- Used by layouts only. A section that belongs to a feature goes in
  `components/features/{feature}/sections/`.
- Holds the layout's own state, for example whether the sidebar is collapsed.
- Compose from `layouts/widgets/`, `components/shared/`, and `components/ui/`.
