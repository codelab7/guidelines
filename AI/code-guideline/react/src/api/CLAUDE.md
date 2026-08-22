# src/api - Backend Calls

- Every call to the backend goes through this folder. A component never calls `fetch` directly.
- One file per resource, grouped by domain: `contacts.ts`, `invoices.ts`.
- Type every request and response against `types/api.interface.ts`. No `any`.
- No UI concerns: no toasts, no component state, no rendering. Return data or throw, and let the
  caller decide what to show.
- The base URL comes from config, never inline in a call.
