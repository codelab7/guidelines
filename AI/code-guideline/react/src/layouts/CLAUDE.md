# src/layouts - Page Shells

- Layouts are the shells a page renders inside: `auth-layout.tsx`, `user-layout.tsx`.
- Read the session and permission context here once and pass what is needed downwards.
- Structure only. No feature logic and no feature data fetching.
- Compose from `sections/` and `widgets/`. Keep the layout file itself short.
