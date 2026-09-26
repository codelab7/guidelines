# resources/js/stores - Client State

- Zustand. See `code-decisions/preferred-libraries.md`.
- One store per domain. Not one global store holding everything.
- Client state only. Server data stays in the Inertia page props - never copy it into a store
  where it can go stale.
- Derive values at render time instead of storing a computed copy.
- Keep the actions in the store next to the state they change, not spread across components.
- If the state is used by one component and its children, use `useState` and props instead.
