# resources/js/utils - Shared Helpers

- Read this folder before writing any helper. The one you need often already exists.
- Pure functions only: same input, same output, no side effects.
- No React, no hooks, no component state, no Inertia props.
- Group by topic and name the file for what it handles: `number.enums.ts` for number and currency
  formatting, `date.enums.ts` for dates.
- `validation.utils.ts` is the single home for validation helpers. Each is a pure function
  returning a boolean or a simple typed result. Add a reusable rule here instead of redefining it
  in a component.
- Never duplicate a validation rule anywhere else in the codebase.
- `cn`, the class name merger, lives here and is the standard for conditional classes.
