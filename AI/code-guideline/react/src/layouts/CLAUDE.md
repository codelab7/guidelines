# src/layouts - Page Shells

- Layouts are the shells a page renders inside: `auth-layout.tsx`, `user-layout.tsx`.
- One file per layout. No subfolders here.
- The shell's parts - sections such as `side-bar.tsx` and `header.tsx`, widgets such as
  `user-menu.tsx` - are a feature like any other, in `components/features/app-shell/`. The layout
  only places them, the way a page places a feature's sections.
- A layout imports from `features/app-shell/`, `shared/`, and `ui/`. Never from another feature.
- Shell state, such as whether the sidebar is collapsed, lives in the shell's sections, not in the
  layout file.
- Read the session and permission context here once and pass what is needed downwards.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.
