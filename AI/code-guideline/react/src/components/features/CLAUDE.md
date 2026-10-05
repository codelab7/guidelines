# src/components/features - Feature Folders

## Rules
- One folder per feature. Everything the feature is built from lives here. Its page in `pages/` only places the sections.
- Sections sit directly in the feature folder.
- Shell parts, such as the sidebar and header, are not a feature. They live in `components/layouts/`.

```
components/features/sale/sale-summary.tsx     a section: the feature's logic, state, data, forms
components/features/sale/sale-lines.tsx       another section
components/features/sale/widgets/             small pieces used only by this feature
components/features/sale/sale-utils.ts        helpers used only by this feature
components/features/sale/use-sale-*.ts        hooks used only by this feature
```

1. **Section** - a component at the feature root. Holds the feature's logic, state, data handling, and forms. Sections own the data calls, made through `api/`. A section may call other sections to break up a large flow.
	- any component at the feature root is a section.
	- All Forms should be considered as section and goes into features folder at root level with `-form.tsx` postfix.
2. **Widget** - `widgets/`. Props in, callbacks out. Renders and handles small local state. No business rules.
	- Every widget goes in `widgets/`. The folder is what marks a component as a widget.
	- Widgets that have used by more than one features, goes to `src/components/shared/` folder.

### Forms
- Validate inline at field level and show the failure next to the field.