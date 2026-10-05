# src/api - Backend Calls

Every call to the backend goes through this folder.

## Structure

```text
api/
  contacts.ts    one file per resource, grouped by domain
  invoices.ts
```

## Rules

- Type every request and response against `types/api.interface.ts`. No `any`.
- No UI concerns: no toasts, no component state, no rendering. Return data or throw, and let the
  caller decide what to show.
- The base URL comes from config, never inline in a call.

## Boundaries

- Import from `types/` and config only. Never from a component, a hook, or a store.
- Not here: a component never calls `fetch` directly. It goes through a file in this folder.

## Existing Resources

Read this list before adding a call - the endpoint may already be wrapped. When you add, rename,
or remove a call, update this list in the same change.

| File | Calls |
|------|-------|
