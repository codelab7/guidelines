# src/components/features - Feature Folders

One folder per feature. Everything the feature is built from lives here. Its page in `pages/`
only places the sections. The one exception is `app-shell/`, the sidebar, header, and other shell
parts, whose sections are placed by a layout in `layouts/` instead.

```
components/features/sale/sale-summary.tsx     a section: the feature's logic, state, data, forms
components/features/sale/sale-lines.tsx       another section
components/features/sale/widgets/             small pieces used only by this feature
components/features/sale/sale-utils.ts        helpers used only by this feature
components/features/sale/use-sale-*.ts        hooks used only by this feature
```

- Sections sit directly in the feature folder. There is no `sections/` subfolder.
- Every widget goes in `widgets/`, even when there is only one. The folder is what marks a
  component as a widget, so any component at the feature root is a section.
- Feature-only helpers go in `{feature}-utils.ts` inside the feature, not in `utils/`.

## The Two Roles

1. **Section** - a component at the feature root. Holds the feature's logic, state, data
   handling, and forms. Sections own the data calls, made through `api/`. A section may call other
   sections to break up a large flow.
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
