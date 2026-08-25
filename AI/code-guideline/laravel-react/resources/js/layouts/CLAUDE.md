# resources/js/layouts - Page Shells

- Layouts are the shells a page renders inside: `auth-layout.tsx`, `user-layout.tsx`.
- Read the Inertia shared props here once - `auth`, `permissions`, `flash` - and pass what is
  needed downwards.
- Structure only. No module logic and no module data fetching.
- Compose from `sections/` and `widgets/`. Keep the layout file itself short.
