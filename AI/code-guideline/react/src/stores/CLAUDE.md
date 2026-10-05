# src/stores - Client State

Client state with Zustand. See `code-decisions/preferred-libraries.md`.

## Structure

- One store per area of state, such as the cart or UI preferences. Never one global store holding
  everything.
- File and hook names: `cart-store.ts` exports `useCartStore`.
- Keep the actions in the store next to the state they change, not spread across components.

## Rules

### Where a Piece of State Goes

| State | Home |
|-------|------|
| Server data | the `api/` query hooks and their cache |
| State that should survive a reload or be shareable by link: filters, page number, tab | URL search params |
| Client state shared by components far apart: cart, UI preferences, session | a store |
| State of one component and its children | `useState` and props |

### Using a Store

- Select only what you need: `useCartStore((s) => s.items)`. For several fields, use
  `useShallow`. Never `const store = useCartStore()` - it re-renders on every change.
- Derive values at render time instead of storing a computed copy.
- `persist` may save UI preferences and drafts only. Never a token or personal data.
- A store action never calls `api/`. A section calls `api/`, then updates the store if it needs
  to.

## Boundaries

- Follow the `stores/` row in the import table in `src/CLAUDE.md`.
- Not here: server data. It stays in the `api/` layer and its cache.

## Existing Stores

Read this list before adding a store or a field. When you add, rename, or remove a store, or
change what it holds, update this list in the same change.

| File | Store | Holds |
|------|-------|-------|
