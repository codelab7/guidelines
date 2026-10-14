# src/components/features - Feature Folders

One folder per feature. A feature is one business area of the app, such as sales or contacts. Everything the feature is built from lives here. Its screen in `app/` only places the sections.

## Structure

```text
components/features/sales/
  sale-summary.tsx        a section: the feature's logic, state, and data
  sale-lines.tsx          another section
  sale-utils.ts           helpers used only by this feature
  sale-constants.ts       constants used only by this feature
  use-sale-*.ts           hooks used only by this feature
  forms/sale-form.tsx     forms. Every form is a section.
  widgets/                small pieces used only by this feature
```

- "Feature" is the one word for this in the whole tree. `api/` uses "resource" only for a group of backend endpoints.
- Folder names are plural and `kebab-case`: `sales/`, `contacts/`. The files inside use the singular prefix: `sale-summary.tsx`. The feature's folder in `app/` uses the same name.
- No subfolders other than `forms/` and `widgets/`, and both stay flat. Helpers and hooks sit at the feature root.
- **Section** - any component at the feature root or in `forms/`.
- **Widget** - any component in `widgets/`. The folder is what marks a component as a widget.
- The router owns `app/`, so the sections can't sit beside their screen. That is why they live here and not in `app/`.

## Rules

### Sections

- A section holds the feature's logic, state, and data handling.
- Sections own the data calls, through the query hooks in `api/`. When two sections need the same data, each calls the same query hook - the cache sends one request. Never fetch in a parent only to pass the data down.
- A section may call other sections to break up a large flow.
- A section that shows a list owns its `FlatList`, its pull-to-refresh, and its loading, empty, and error states.

### Widgets

- Props in, callbacks out. A widget renders and handles small local state.
- A widget holds display logic only, never a business rule. A business rule is a decision about the domain: a price calculation, a permission check, an allowed status change, validation. Display logic is formatting, toggling, or sorting what was passed in.
- Every widget goes in `widgets/`.
- Once a different feature uses a widget, move it to `src/components/shared/`. The steps are in `components/CLAUDE.md`.

### Forms

- Every form lives in `forms/` with a `-form.tsx` suffix.
- One form serves both create and edit. It takes initial values. Never build a separate create form and edit form.
- Use the UI kit's form package when it has one. Otherwise use React Hook Form with Zod.
- With Zod, the form's schema lives in `src/schemas/`. Read `src/schemas/CLAUDE.md` before you write or change one.
- Validate on blur, then on every change once a field has shown an error. Show the failure next to the field.
- Map the server's field errors (`ApiError.fieldErrors`) to the matching fields.
- Disable the submit button while the request is pending.
- Keep every field visible above the keyboard. Wrap the form in the project's keyboard-avoiding container, and make a long form scroll.
- The keyboard's return key moves to the next field, and on the last field it submits. Set `returnKeyType` and focus the next field on submit.
- Dismiss the keyboard before navigating away or showing a result.

## Boundaries

- Follow the Sections and Widgets rows in the import table in `src/CLAUDE.md`.
- Never import from another feature's folder, with one exception: a feature may import another feature's *section* when it must embed that feature's whole flow - for example, a sale screen that shows the contact form - and the section cannot sensibly move to `shared/`. Import the section only, never its widgets, hooks, or helpers. Tell the user when you do it.
- Not here: shell parts such as the tab bar and header are not a feature. They live in `components/layouts/`.
- Not here: route files live in `app/`. A hook or helper used by more than one feature lives in `src/hooks/` or `src/utils/`. A shared or backend type lives in `src/types/`. A Zod schema lives in `src/schemas/`. A native API wrapper lives in `src/device/`.

## Existing Features

Read this list before opening feature folders. When you add, rename, or remove a feature folder, or change what it covers, update this list in the same change.

| Folder | Covers | Screens |
|--------|--------|---------|
