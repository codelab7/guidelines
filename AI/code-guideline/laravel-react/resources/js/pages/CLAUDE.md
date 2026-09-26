# resources/js/pages - Module Pages

One folder per domain module. Laravel controllers render these through Inertia.

```
pages/sale/index.tsx          the page a controller renders
pages/sale/sections/          the module's logic
pages/sale/widgets/           small pieces used only by this module
pages/sale/sale-utils.ts      helpers used only by this module
```

## The Three Roles

1. **Page** - `pages/{module}/index.tsx`. Provides the page structure, wires sections together,
   and receives the Inertia props. Keep logic to a minimum.
2. **Section** - `pages/{module}/sections/`. Holds most of the module's logic, state, and data
   handling. A section may call other sections to break up a large flow.
3. **Widget** - `pages/{module}/widgets/`. Props in, callbacks out. Renders and handles small
   local state. No business rules.

## Placement

- Module-only helpers go in `{module}-utils.ts` inside the module, not in `utils/`.
- A widget that a second module needs moves to `components/shared/` or `components/specific/`.
- A hook used by more than one module moves to `hooks/`.

## Forms

- Always destructure `useForm`:

  ```tsx
  const { data, setData, errors, setError, processing, reset } = useForm<ContactFillable>(...);
  ```

- A field that only sets data gets an inline lambda.
- A field that does anything more gets its own named handler - `handleEmailInput` - which sets the
  data, validates, and calls `setError` on failure. Never write one generic handler that branches
  over field names.
- Validate inline at field level and show the failure through `setError`.
- Submit from a button click handler, not a bare HTML form submit. The handler checks for errors
  and stops if any exist.
- A repeated field group, like an invoice line item, becomes a subcomponent that holds its own
  form state and calls the parent's `onChange` with the updated row. The parent replaces that row
  in its array.
