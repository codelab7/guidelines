# src/types - Shared Types

## api.interface.ts

- The contract for everything the backend returns.
- Change it only when the backend response changes. It is not a scratch file.
- Keep structures shared by several endpoints at the root of the file.
- Mirror the backend's actual response, not its documentation.

## general.enum.ts

- Enums that come from the backend and are used across features.
- Extend it only when the backend introduces a new enum.

## Naming

- A component's props type is named `Props` and stays in the component's own file.
- A form's field type is `{Module}Fillable` - `ContactFillable`, `InvoiceFillable`.

## Data Shape

- A screen holds only the data it actually uses. Map an API response to what the screen needs
  instead of passing the raw payload down.
