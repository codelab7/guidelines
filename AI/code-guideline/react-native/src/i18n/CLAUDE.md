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
- The starting language comes from the device, through `expo-localization`. The user's own choice, if the app has one, overrides it and is kept in a store.

## Rules

- Never introduce i18n on your own initiative. If a string needs translating and there is no setup yet, ask the user first.
- Once the project has i18n, never hardcode user-facing text. Add a key. This includes accessibility labels and text in `app.json`, such as permission descriptions.
- Keys are `section.meaning` inside the feature file: `summary.totalLabel`. Name them for their meaning, not for the English text.
- Strings used by many features go in `common.json`. Don't repeat them per feature.
- Use the library's interpolation and plural support. Never build a sentence by joining strings.
- A new key lands in the default language first, then in every other language.
- Format dates, numbers, and currency for the active language. Don't hardcode a format.

## Translations Break Layouts

Translated text is the most common cause of a broken mobile layout. A word that is short in English is often a long phrase in another language.

- A heading next to an action needs to shrink, and the action needs to keep its size.
- Anything limited to one line must still make sense when it is cut off.
- Check a screen in the longest language the project supports before calling it done.
- A language written right to left flips the layout. Use `start` and `end` styles, never `left` and `right`, when the project supports one.
