# src/i18n - Translations

Translation files for react-i18next. This folder is only used when the project already supports translations.

## Structure

```text
i18n/
  en/
    common.json   shared strings: Save, Cancel, Delete
    sales.json    one file per feature, named like the feature folder
```

- One folder per language. Inside it, one JSON file (namespace) per feature, plus `common.json`.

## Rules

- Never introduce i18n on your own initiative. If a string needs translating and there is no setup yet, ask the user first.
- Once the project has i18n, never hardcode user-facing text. Add a key.
- Keys are `section.meaning` inside the feature file: `summary.totalLabel`. Name them for their meaning, not for the English text.
- Strings used by many features go in `common.json`. Don't repeat them per feature.
- Use the library's interpolation and plural support. Never build a sentence by joining strings.
