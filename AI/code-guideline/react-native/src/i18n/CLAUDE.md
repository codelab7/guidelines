# src/i18n/ — Rules

## What this is

i18next setup and the 15-language string resources — a v1 requirement, not a stretch goal. Resources are statically bundled (Metro has no lazy-chunking equivalent to the web's Vite setup), namespaced `common`/`chat`/`onboarding` for web parity. The every-string-through-`t()` rule is in the root `CLAUDE.md`.

## Rules

- **New keys:** a new key lands in `locales/en/<namespace>.json` first, then all 14 other locales — `tests/locale-parity.test.ts` fails a key missing from any locale, across all three namespaces. A new namespace joins that list the day it is created: the check was `common`-only for a while, and four `onboarding` keys went missing from every non-English bundle without a test failing.
- **Long translations are the layout constraint:** a label that is one short word in English is often a wide phrase in Tamil, Malayalam or Kannada. A heading beside an action needs `flexShrink: 1` (and the action `flexShrink: 0`), and anything given `numberOfLines={1}` must be something that reads when clipped — check a screen in `ta` before calling it done.
- **Language list parity:** `SUPPORTED_LANGUAGES` (in `index.ts`) must stay in sync with `kgpt-app-ui/src/i18n/index.ts` — same codes, same endonyms.
- **RTL:** `ur`/`fa`/`ar` are RTL *scripts* rendered in LTR layout for v1 (matches web) — don't wire up `I18nManager.forceRTL` or mirrored layouts for them.
- **Persistence:** persist the selected language with `storage.ts`'s `'selectedLanguage'` AsyncStorage key — the same key name the web app uses in localStorage — not a new key.
- **Adding a language:** a new `locales/<code>/` folder, its three JSON files wired into the static imports in `resources.ts`, and entries in both `SUPPORTED_LANGUAGES` and `LANGUAGE_ENGLISH_NAMES` in `index.ts`.

## Structure

`index.ts` (i18next init, `SUPPORTED_LANGUAGES`, `LANGUAGE_ENGLISH_NAMES`, `isSupportedLanguage()`), `resources.ts` (static imports assembling all locale JSON), `storage.ts` (AsyncStorage persistence). `locales/` holds one folder per language code (`ar, as, bn, en, fa, gu, hi, kn, ml, mr, or, pa, ta, te, ur`), each with `common.json`/`chat.json`/`onboarding.json`.
