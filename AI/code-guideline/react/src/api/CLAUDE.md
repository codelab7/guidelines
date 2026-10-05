# src/api - Backend Calls

Every call to the backend goes through this folder, together with the TanStack Query hooks that
wrap the calls.

## Structure

```text
api/
  client.ts     thin fetch wrapper: base URL, auth, JSON, error shape
  contacts.ts   one file per resource
  invoices.ts
```

- One file per resource, flat. When one feature has more than 3 resources, group them in a
  subfolder named for the feature.
- A resource file holds three things: the request functions, a query key factory, and the query
  and mutation hooks.

  ```ts
  export const contactKeys = {
      all: ['contacts'] as const,
      detail: (id: string) => ['contacts', id] as const,
  };

  export function getContacts() { /* uses client.ts */ }
  export function useContacts() {
      return useQuery({ queryKey: contactKeys.all, queryFn: getContacts });
  }
  ```

## Rules

### Requests

- Every request goes through `client.ts`. The base URL comes from `config.ts`, never inline.
- Name request functions `getContacts`, `getContact(id)`, `createContact`, `updateContact`,
  `deleteContact`. Anything else is a verb plus the resource: `archiveContact`. Hooks follow the
  same names: `useContacts`, `useContact(id)`, `useCreateContact`.
- Type every request and response against `types/api.interface.ts`. No `any`.
- Return the raw backend type. Mapping to what a section needs happens in the section, or in the
  query's `select`.
- No UI concerns: no toasts, no component state, no rendering. Return data or throw, and let the
  caller decide what to show.

### Errors

- `client.ts` turns every failure into one `ApiError` type - `status`, `message`, `fieldErrors` -
  defined in `types/api.interface.ts`.
- A section shows `message`. A form maps `fieldErrors` to its fields.

### Auth

- Follow the backend's auth style. Only `client.ts` touches the session.
- httpOnly cookie: `client.ts` sends credentials with every request and redirects to login on a
  401.
- Bearer token: `client.ts` keeps the token in localStorage, sends it in the `Authorization`
  header, and on a 401 clears it and redirects to login.

### Cache and Retry

- The defaults live in `src/query-client.ts`: queries retry 3 times, mutations never retry.
  Change a default there, not per call, unless one call really needs it.
- After a mutation, invalidate the query keys it changes.

## Boundaries

- Follow the `api/` row in the import table in `src/CLAUDE.md`. Never import from a component, a
  hook, or a store.
- Not here: a component never calls `fetch` directly. It goes through a hook in this folder.

## Existing Resources

Read this list before adding a call - the endpoint may already be wrapped. When you add, rename,
or remove a call or a hook, update this list in the same change.

| File | Calls | Hooks |
|------|-------|-------|
