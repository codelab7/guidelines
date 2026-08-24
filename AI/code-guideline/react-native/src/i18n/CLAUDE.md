# src/i18n - Translations

- This folder is only used when the project supports translations.
- Never introduce i18n on your own initiative. If a string needs translating and there is no setup
  yet, ask the user first.
- When a setup exists, follow it. Don't add a second translation mechanism alongside it.
- Every user-facing string goes through the translation function. No literal text in a screen.
- Keys are grouped by module and named for meaning, not for the English text.
- A new key lands in the default language first, then in every other language. A test that fails
  on a missing key is worth having - without one, a whole namespace can go missing quietly.

## Translations Break Layouts

Translated text is the most common cause of a broken mobile layout. A word that is short in
English is often a long phrase in another language.

- A heading next to an action needs to shrink, and the action needs to keep its size.
- Anything limited to one line must still make sense when it is cut off.
- Check a screen in the longest language the project supports before calling it done.
