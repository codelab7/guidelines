# src/types - Shared Types

Types shared across features: what the backend returns and the enums it sends.

## Structure

```text
types/
  api.interface.ts   the contract for everything the backend returns
  general.enum.ts    enums that come from the backend and are used across features
```

## Rules

### api.interface.ts

- Change it only when the backend response changes. It is not a scratch file.
- Keep structures shared by several endpoints at the root of the file.

### general.enum.ts

- Extend it only when the backend introduces a new enum.

### Naming

- A component's props type is named `Props`.
- A form's field type is `{Feature}Fillable` - `ContactFillable`, `InvoiceFillable`.

### Data Shape

- A section holds only the data it actually uses. Map an API response to what the section needs
  instead of passing the raw payload down.
