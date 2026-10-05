# src/stores - Client State

Client state with Zustand. See `code-decisions/preferred-libraries.md`.

## Structure

- One store per domain. Not one global store holding everything.
- Keep the actions in the store next to the state they change, not spread across components.

## Rules

- Client state only. Server data belongs to the `api/` layer and its cache - never copy it into a
  store where it can go stale.
- Derive values at render time instead of storing a computed copy.

## Boundaries

- Not here: state used by one component and its children. Use `useState` and props instead.
- Not here: server data. It stays in the `api/` layer and its cache.

## Existing Stores

Read this list before adding a store or a field. When you add, rename, or remove a store, or
change what it holds, update this list in the same change.

| File | Store | Holds |
|------|-------|-------|
