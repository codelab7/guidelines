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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### FEAT-1. Confusing - Feature, domain, module, resource

The tree uses four words for nearly the same thing: `pages/` groups by "domain", `api/` is one file
per "resource" grouped by "domain", this folder uses "feature", `i18n/` groups keys by "feature",
and the Laravel tree says "module". The agent cannot tell whether `pages/sale/` and
`components/features/sale/` must share a name.

- A: Use "feature" everywhere in this tree. A page folder and its feature folder share the same
  name. `api/` keeps "resource" for a backend endpoint group.
- B: Keep the words, and define each one in `src/CLAUDE.md`.

Recommended: A.

**Decision:**

### FEAT-2. Question - Singular or plural folder names

Examples use `sale`, but nothing fixes it. Agents will create `sales/` and `sale/` side by side.

- A: Singular - `sale/`, matching the file prefix `sale-summary.tsx`.
- B: Plural.

Recommended: A.

**Decision:**

### FEAT-3. Question - Feature-level types

Open in the README checklist: does a feature keep its own types file, or does everything go to
`types/`?

- A: `{feature}-types.ts` at the feature root for types only this feature uses. Move to `types/` on
  the second feature's use, like widgets.
- B: Everything in `types/`.

Recommended: A.

**Decision:**

### FEAT-4. Question - Subfolders in a large feature

A feature with 20 sections has no rule for grouping. Can it have sub-feature folders? Can
`widgets/` have subfolders?

- A: One level of sub-feature folders, each with the same layout as a feature (sections at root,
  own `widgets/`). `widgets/` stays flat.
- B: Always flat.
- C: No rule.

Recommended: A.

**Decision:**

### FEAT-5. Question - Many helpers or hooks in one feature

The structure shows one `sale-utils.ts` and `use-sale-*.ts` hooks at the root. With many hooks the
root gets crowded and the sections become hard to spot.

- A: Keep them at the root.
- B: Once a feature has more than 3 hooks, move them to `hooks/` inside the feature folder. Same
  for `utils/`.

Recommended: B.

**Decision:**

### FEAT-6. Missing - Form rules

The form rules cover only inline validation. Open: form library (README checklist), schema library
(for example zod) and where schemas live, when validation runs (blur, change, submit), how server
errors map to fields, and the submit button state.

- Suggested: React Hook Form + zod. The schema sits in the form file, or `{feature}-schema.ts` when
  shared. Validate on blur, then on change after the first error. Map server field errors to the
  matching fields. Disable submit while pending.

Recommended: Adopt, or name your form library.

**Decision:**

### FEAT-7. Confusing - Two sections that need the same data

Sections own the data calls and may call other sections. When a parent and a child section both
need the same data, which one fetches? The answer depends on API-1.

- A: With TanStack Query: each section fetches what it needs, the cache removes duplicate calls.
- B: With plain calls: the parent fetches and passes the data down as props.

Recommended: Follows API-1.

**Decision:**

### FEAT-8. Decision aid - What counts as a business rule

Widgets hold "no business rules", but the term is not defined, so the agent cannot tell whether
formatting a price or hiding a button is one.

- Suggested: business rule = a decision about the domain (price calculation, permission check,
  allowed status change, validation). Display logic = formatting, toggling, sorting what was passed
  in. Widgets may hold display logic only.

Recommended: Adopt.

**Decision:**
