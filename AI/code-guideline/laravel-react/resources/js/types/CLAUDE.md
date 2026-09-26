# resources/js/types - Shared Types

## api.interface.ts

- The contract for everything the Laravel backend returns.
- Change it only when the backend response changes. It is not a scratch file.
- Keep structures shared by several endpoints at the root of the file.

## general.enum.ts

- Enums that come from the backend and are used across features.
- Extend it only when the backend introduces a new enum.

## Naming

- A component's props type is named `Props`.
- A form's field type is `{Module}Fillable` - `ContactFillable`, `InvoiceFillable`.

## Data Shape

- A page receives only the data it actually uses. Map it in the Laravel resource; don't ship the
  whole model and pick fields in the component.
