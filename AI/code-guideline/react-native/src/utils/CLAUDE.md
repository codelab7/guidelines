# src/utils - Shared Helpers

Everything shared that is not a component, a hook, or an API call. Read this folder before writing
any helper. The one you need often already exists.

## Rules

- Group by topic and name the file for what it handles: `date.ts`, `number.ts`, `validation.ts`,
  `storage.ts`, `notifications.ts`.
- One topic per file. A file that needs "and" to describe it is two files.
- No React, no hooks, no component state, no JSX.
- Export named functions. No default export.
- A helper used by one feature only stays in that feature's folder, as `{feature}-utils.ts`.

## Keeping It From Becoming A Dump

This folder holds two kinds of code, and mixing them inside one file is how it rots.

- **Pure helpers** - same input, same output, no side effects. Formatting, parsing, validation,
  calculation.
- **Platform integrations** - storage, notifications, permissions, analytics, deep links. These do
  have side effects, and they wrap a native API behind a small typed function.

Keep the two in separate files. A pure helper file must stay pure, so it can be tested with no
mocks and no native runtime.

- `validation.ts` is the single home for validation helpers. Each is a pure function returning a
  boolean or a simple typed result. Never redefine a validation rule in a component.
- An integration file exposes what the app needs, not the whole native API. The rest of the app
  should never import the native module directly.
