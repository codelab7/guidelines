# src/components/shared - Shared Project UI

- General-purpose UI that any module can use: `delete-confirmation.tsx`, `phone-input.tsx`.
- Built from `ui/` primitives.
- No domain vocabulary and no imports from `pages/`. A component that knows about invoices or
  contacts belongs in `specific/`.
- Controlled by props and callbacks. No data fetching here.
