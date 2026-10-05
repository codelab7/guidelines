# src/i18n - Translations

Translation files. This folder is only used when the project already supports translations.

## Structure

- Follow the file layout of the i18n library the project already uses.
- Keys are grouped by feature.

## Rules

- Never introduce i18n on your own initiative. If a string needs translating and there is no
  setup yet, ask the user first.
- Name keys for their meaning, not for the English text.

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### I18N-1. Question - Library and file layout

"Follow the layout the project already uses" is fine for an existing setup. If the team has a
standard, naming it saves a guess.

- A: react-i18next. One folder per language, one JSON file per feature: `i18n/en/sale.json`.
- B: No standard - follow the project.

Recommended: A, if the team has used it before.

**Decision:**

### I18N-2. Question - Shared strings

Keys are grouped by feature. Where do "Save", "Cancel", "Delete" go?

- A: A `common` file / namespace.
- B: Repeat them per feature.

Recommended: A.

**Decision:**

### I18N-3. Missing - Key format and plurals

No key format, and nothing against building sentences by joining strings.

- Suggested: `section.meaning` keys inside the feature file (`summary.totalLabel`). Use the
  library's interpolation and plural support, never string concatenation.

Recommended: Adopt.

**Decision:**

### I18N-4. Missing - Hardcoded text when i18n exists

Nothing says that, once a project has i18n, every user-facing string must go through it.

- Suggested: "When the project has i18n, never hardcode user-facing text. Add a key."

Recommended: Adopt.

**Decision:**
