# src/components/features - Feature Folders

One folder per feature. Everything the feature is built from lives here. Its page in `pages/`
only places the sections.

## Structure

```text
components/features/sale/
  sale-summary.tsx    a section: the feature's logic, state, data, forms
  sale-lines.tsx      another section
  sale-form.tsx       a form, which is also a section
  sale-utils.ts       helpers used only by this feature
  use-sale-*.ts       hooks used only by this feature
  widgets/            small pieces used only by this feature
```

1. **Section** - any component at the feature root. Sections sit directly in the feature folder.
2. **Widget** - any component in `widgets/`. The folder is what marks a component as a widget.

## Rules

### Sections

- A section holds the feature's logic, state, data handling, and forms.
- Sections own the data calls, made through `api/`.
- A section may call other sections to break up a large flow.

### Widgets

- Props in, callbacks out. A widget renders and handles small local state. No business rules.
- Every widget goes in `widgets/`.
- Once a second feature uses a widget, move it to `src/components/shared/`.

### Forms

- Every form is a section. It sits at the feature root with a `-form.tsx` suffix.
- Validate inline at field level and show the failure next to the field.

## Boundaries

- Import from `shared/`, `ui/`, and this feature's own files. Never from another feature's
  folder.
- Not here: shell parts such as the sidebar and header are not a feature. They live in
  `components/layouts/`.
- Not here: route files live in `pages/`. A hook or helper used by more than one feature lives in
  `src/hooks/` or `src/utils/`.

## Existing Features

Read this list before opening feature folders. When you add, rename, or remove a feature folder,
or change what it covers, update this list in the same change.

| Folder | Covers | Page |
|--------|--------|------|
