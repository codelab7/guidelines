# src/components/features - Feature Folders

One folder per feature. Everything the feature is built from lives here. Its page in `pages/`
only places the sections.

```
components/features/sale/sections/          the feature's logic, state, data, and forms
components/features/sale/widgets/           small pieces used only by this feature
components/features/sale/sale-utils.ts      helpers used only by this feature
components/features/sale/use-sale-*.ts      hooks used only by this feature
```

- Add a subfolder only once more than one file belongs in it. A feature with two files keeps them
  flat.
- Feature-only helpers go in `{feature}-utils.ts` inside the feature, not in `utils/`.

## The Two Roles

1. **Section** - `sections/`. Holds the feature's logic, state, data handling, and forms. Sections
   own the data calls, made through `api/`. A section may call other sections to break up a large
   flow.
2. **Widget** - `widgets/`. Props in, callbacks out. Renders and handles small local state. No
   business rules.

## Forms

- Destructure the form state you use. Don't pass a single form object around.
- A field that only sets a value gets an inline lambda.
- A field that does anything more gets its own named handler - `handleEmailInput` - which sets the
  value, validates, and records the error. Never write one generic handler that branches over
  field names.
- Validate inline at field level and show the failure next to the field.
- Submit from a button click handler, not a bare HTML form submit. The handler checks for errors
  and stops if any exist.
- A repeated field group, like an invoice line item, becomes a subcomponent that holds its own
  form state and calls the parent's `onChange` with the updated row. The parent replaces that row
  in its array.
