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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### API-1. Question - Data fetching library

Open in the README checklist: TanStack Query or plain calls. It changes FEAT-7, STORE-3, HOOK-2,
and where loading and cache rules live.

- A: TanStack Query. `api/{resource}.ts` holds the plain request functions and a `{resource}Keys`
  query key factory. Query hooks (`useContacts`) live next to them in the same file.
- B: TanStack Query, but query hooks live in the feature folder.
- C: Plain functions only. Sections handle loading state themselves.

Recommended: A. One file per resource gives the agent one place to look.

**Decision:**

### API-2. Missing - The HTTP client

The structure lists only resource files. Something has to hold the base URL, auth header, JSON
handling, and error normalising once.

- A: `api/client.ts`, a thin `fetch` wrapper. Every resource file uses it.
- B: Same, with axios.

Recommended: A. No extra dependency.

**Decision:**

### API-3. Question - Error shape

Open in the README checklist. Without one shape, every section parses errors its own way.

- Suggested: `client.ts` turns every failure into one `ApiError` type - `status`, `message`,
  `fieldErrors` - defined in `types/api.interface.ts`. Sections show `message`, forms map
  `fieldErrors` (see FEAT-6).

Recommended: Adopt.

**Decision:**

### API-4. Confusing - "One file per resource, grouped by domain"

This can mean flat files, or a subfolder per domain holding resource files. The agent will do both.

- A: Flat. One file per resource. A subfolder only when a domain has more than 3 resources.
- B: Always a subfolder per domain.

Recommended: A.

**Decision:**

### API-5. Decision aid - Function names

No naming rule for request functions.

- Suggested: `getContacts`, `getContact(id)`, `createContact`, `updateContact`, `deleteContact`.
  Anything else is a verb plus the resource: `archiveContact`.

Recommended: Adopt.

**Decision:**

### API-6. Question - Who maps the response

`types/` says a section maps the API response to what it needs. Should `api/` return the raw
backend type, or a mapped frontend model?

- A: `api/` returns the raw type from `api.interface.ts`. Mapping happens in the section (or the
  query `select`).
- B: `api/` maps to frontend models.

Recommended: A. It keeps `api/` a thin layer.

**Decision:**

### API-7. Question - Auth and session

Open in the README checklist: where the token lives (httpOnly cookie, memory, localStorage), and
what happens on a 401 (refresh, redirect to login).

- A: httpOnly cookie set by the backend. `client.ts` sends credentials and redirects to login on
  401.
- B: Bearer token in memory with a refresh call in `client.ts`.
- C: Bearer token in localStorage (simplest, weakest against XSS).

Recommended: A, if the backend can do it.

**Decision:**

### API-8. Question - Loading and retry policy

Open in the README checklist.

- A: With TanStack Query: defaults (3 retries for queries, none for mutations), cache config in one
  `src/query-client.ts`.
- B: No retries.

Recommended: A, following API-1.

**Decision:**
