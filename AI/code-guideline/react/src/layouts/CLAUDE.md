# src/layouts - Page Shells

- Layouts are the shells a page renders inside: `auth-layout.tsx`, `user-layout.tsx`.
- One file per layout. No subfolders here.
- The shell's parts - sections such as `side-bar.tsx` and `header.tsx`, widgets such as
  `user-menu.tsx` - live in `components/layouts/`. The layout only places them, the way a page
  places a feature's sections.
- A layout imports from `components/layouts/`, `shared/`, and `ui/`. Never from a feature.
- Read the session and permission context here once and pass what is needed downwards.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.
