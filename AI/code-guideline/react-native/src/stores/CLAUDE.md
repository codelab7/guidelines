# src/stores - Client State

- Zustand. See `code-decisions/preferred-libraries.md`.
- One store per domain. Not one global store holding everything.
- Client state only. Server data belongs to the `api/` layer and its cache - never copy it into a
  store where it can go stale.
- Derive values at render time instead of storing a computed copy.
- Keep the actions in the store next to the state they change, not spread across components.
- If the state is used by one component and its children, use `useState` and props instead.
- Don't use React context to hold state. Context is for mounting a library provider in
  `app/_layout.tsx`, nothing more.
- State that must survive an app restart is persisted deliberately, and a token or secret goes to
  secure storage. Never persist a whole store by default.
