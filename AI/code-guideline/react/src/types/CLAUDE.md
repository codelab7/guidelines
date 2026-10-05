# src/types - Shared Types

Types shared across features: what the backend returns, the enums it sends, and the `ApiError` type.

## Structure

```text
types/
  api.interface.ts   every backend response type, plus ApiError
  general.enum.ts    enums that come from the backend and are used across features
```

- `api.interface.ts` stays one file. Keep structures shared by several endpoints at the top.
- When the backend publishes an OpenAPI schema, generate `api.interface.ts` from it. Never edit a generated file by hand.

## Rules

### Writing Types

- `interface` for object shapes, `type` for unions and helper types.
- Never a TypeScript `enum`. Use a `const` object with a derived union type:

  ```ts
  export const InvoiceStatus = { Draft: 'draft', Paid: 'paid' } as const;
  export type InvoiceStatus = (typeof InvoiceStatus)[keyof typeof InvoiceStatus];
  ```

### Changing a Backend Type

- Change `api.interface.ts` only when the user says the backend changed, or a real response shows
  the mismatch. Never edit a backend type to make a TypeScript error go away.
- Extend `general.enum.ts` only when the backend introduces a new enum.

## Boundaries

- Follow the `types/` row in the import table in `src/CLAUDE.md`.
- Not here: a props type, or a type used only inside one feature. It stays in the file that uses
  it.
