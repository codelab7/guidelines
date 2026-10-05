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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### STORE-1. Missing - File and hook names

No naming rule for store files or hooks.

- Suggested: `cart-store.ts` exporting `useCartStore`.

Recommended: Adopt.

**Decision:**

### STORE-2. Decision aid - Select slices, not the whole store

`const store = useCartStore()` re-renders the component on every change in the store. It is the
most common Zustand mistake.

- Suggested: always select what you need - `useCartStore((s) => s.items)`. For several fields, use
  `useShallow`.

Recommended: Adopt.

**Decision:**

### STORE-3. Decision aid - Where a piece of state goes

Open in the README checklist: what is allowed in a store and where it stops against the data cache.
A table makes the choice mechanical.

- Server data - the `api/` layer and its cache.
- State that should survive a reload or be shareable by link (filters, page number, tab) - URL
  search params.
- Client state shared by components far apart (cart, UI preferences) - a store.
- State of one component and its children - `useState` and props.

Recommended: Adopt the table here.

**Decision:**

### STORE-4. Question - Persisting a store

Zustand's `persist` saves to localStorage. Nothing says what may be saved there.

- A: Only UI preferences and drafts. Never tokens or personal data.
- B: No persisting.

Recommended: A.

**Decision:**

### STORE-5. Question - May a store action call api/

A store action that fetches would hold server data in the store, which this file forbids. But it is
not said outright.

- A: No. A section calls `api/`, then updates the store if it needs to.
- B: Yes, for actions that change client state after a call.

Recommended: A.

**Decision:**
