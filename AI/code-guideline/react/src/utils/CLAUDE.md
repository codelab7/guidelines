# src/utils - Shared Helpers

Shared helper functions. Read this folder before writing any helper - the one you need often
already exists.

## Structure

```text
utils/
  number.enums.ts       number and currency formatting
  date.enums.ts         dates
  validation.utils.ts   the single home for validation helpers
```

- Group by topic and name the file for what it handles.
- `cn`, the class name merger, lives here and is the standard for conditional classes.

## Rules

- Pure functions only: same input, same output, no side effects.
- Each validation helper is a pure function returning a boolean or a simple typed result. Add a
  reusable rule to `validation.utils.ts` instead of redefining it in a component.
- Never duplicate a validation rule anywhere else in the codebase.

## Boundaries

- No React, no hooks, no component state. Anything that needs them goes in `hooks/`.
- Not here: a helper used by one feature stays in its `{feature}-utils.ts` under
  `components/features/{feature}/`.

## Existing Helpers

Read this list before writing a helper. When you add, rename, or remove a helper, or change its
arguments or return value, update this list in the same change.

| File | Helpers | What they do |
|------|---------|--------------|
