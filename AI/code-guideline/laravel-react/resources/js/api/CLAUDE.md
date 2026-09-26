# resources/js/api - Direct Backend Calls

This folder is the exception, not the default.

- Page data comes through Inertia props. Don't fetch what the controller already passed.
- Only a genuine endpoint belongs here: autocomplete, polling, an upload, a lookup that must not
  reload the page.
- One file per resource, named for the resource.
- Type every response against `types/api.interface.ts`. No `any`.
- No UI concerns: no toasts, no component state, no rendering. Return data and let the caller
  decide what to show.
