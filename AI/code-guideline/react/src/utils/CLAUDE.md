# src/utils - Shared Helpers

Shared pure helper functions, constants shared across features, and validation helpers.

## Structure

```text
utils/
  number.utils.ts       number and currency formatting
  date.utils.ts         dates, built on date-fns
  validation.utils.ts   the single home for validation helpers
  constants.utils.ts    constants shared across features
```

- Group by topic and name the file for what it handles. Every file ends in `.utils.ts`.

## Rules

- Before you write a helper, check es-toolkit, date-fns, and the list below. Write a new one only
  when none of them covers it. A library helper always beats hand-written code. Never lodash.
- Pure functions only: same input, same output, no side effects.
- `validation.utils.ts` is the single home for validation helpers. When the project uses Zod, it
  holds the shared schema pieces - phone, email, money - that the schemas in `src/schemas/`
  combine. Otherwise each helper is a pure function returning a boolean or a simple typed result.
- Never duplicate a validation rule anywhere else in the codebase.

## Boundaries

- Follow the `utils/` row in the import table in `src/CLAUDE.md`.
- No React, no hooks, no component state. Anything that needs them goes in `hooks/`.
- Not here: a helper or constant used by one feature stays in that feature's `*-utils.ts` or
  `*-constants.ts`.

## Existing Helpers

Read this list before writing a helper or a constant. When you add, rename, or remove one, or
change its arguments or return value, update this list in the same change.

| File | Exports | What they do |
|------|---------|--------------|
