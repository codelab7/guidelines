# src/api - Backend Calls

Every call to the backend goes through this folder, together with the TanStack Query hooks that wrap the calls.

## Structure

```text
api/
  client.ts     thin fetch wrapper: base URL, auth, JSON, timeout, error shape
  contacts.ts   one file per resource
  invoices.ts
```

- One file per resource, flat. When one feature has more than 3 resources, group them in a subfolder named for the feature.
- A resource file holds three things: the request functions, a query key factory, and the query and mutation hooks.

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

- Every request goes through `client.ts`. Never call `fetch` directly, even here. The base URL comes from `config.ts`, never inline.
- On a device, `localhost` is the device itself. A dev build needs the host machine's address, set through the env variable. On the Android emulator the host is `10.0.2.2`.
- `client.ts` sets a timeout on every request. A phone on a weak network can hang a request for a long time.
- Name request functions `getContacts`, `getContact(id)`, `createContact`, `updateContact`, `deleteContact`. Anything else is a verb plus the resource: `archiveContact`. Hooks follow the same names: `useContacts`, `useContact(id)`, `useCreateContact`.
- Type every request and response against `types/api.interface.ts`. No `any`.
- Return the raw backend type. Mapping to what a section needs happens in the section, or in the query's `select`.
- No UI concerns: no toasts, no component state, no navigation, no rendering. Return data or throw, and let the caller decide what to show.
- Uploading a file: send a `FormData` with the file's `uri`, `name`, and `type`. Don't read the file into memory as a string.

### Errors

- `client.ts` turns every failure into one `ApiError` type - `status`, `message`, `fieldErrors` - defined in `types/api.interface.ts`.
- A failure with no response at all - no network, a timeout - becomes an `ApiError` with `status: 0`. A section shows a "check your connection" message for it, not the raw message.
- A section shows `message`. A form maps `fieldErrors` to its fields.

### Auth

- Follow the backend's auth style. Only `client.ts` touches the session.
- Bearer token: `client.ts` reads the token from secure storage through `device/`, keeps a copy in memory, and sends it in the `Authorization` header. On a 401 it deletes the token and calls the unauthorized handler registered in the root layout. See `app/CLAUDE.md`.
- Cookie session: `client.ts` sends credentials with every request and reacts to a 401 the same way.
- Never store the token anywhere but secure storage. Never log it.

### Cache and Retry

- The defaults live in `src/query-client.ts`: queries retry 3 times, mutations never retry. Change a default there, not per call, unless one call really needs it.
- The query client follows the app: it refetches when the app returns to the foreground, and it pauses while the device is offline. Set that up once in `src/query-client.ts` with the app state and network listeners, not per query.
- After a mutation, invalidate the query keys it changes.

## Boundaries

- Follow the `api/` row in the import table in `src/CLAUDE.md`. Never import from a component, a hook, or a store. Only `client.ts` may import from `device/`.
- Not here: a component never calls `fetch` directly. It goes through a hook in this folder.

## Existing Resources

Read this list before adding a call - the endpoint may already be wrapped. When you add, rename, or remove a call or a hook, update this list in the same change.

| File | Calls | Hooks |
|------|-------|-------|
