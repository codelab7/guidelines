# src/api - Backend Calls

- Every call to the backend goes through this folder. A component never calls `fetch` directly.
- One file per resource, grouped by domain: `contacts.ts`, `invoices.ts`.
- A shared `client.ts` builds the request: base URL, headers, auth token, timeout. Every other
  file in this folder goes through it. Never call `fetch` directly, even here.
- Type every request and response against `types/api.interface.ts`. No `any`.
- Handle failures in one place. A shared error handler reads the status code and throws a typed
  error. Never repeat status-code branching in a resource file.
- No UI concerns: no toasts, no component state, no navigation. Return data or throw, and let the
  caller decide what to show.
- No caching and no retry logic here. That belongs to whatever the project uses to fetch.
- The base URL comes from config, never inline in a call. On a device, `localhost` is the device
  itself, so a dev build needs a real host address.
