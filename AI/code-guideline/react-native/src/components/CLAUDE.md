# src/components/ — Rules

## What this is

Everything that renders UI below the route level: app-wide primitives in `ui/`, and one feature-scoped folder per domain holding the components only that feature uses. Ported components follow this app's native-first idioms (root `CLAUDE.md` → "Native-first UI"), not the web's.

## Rules

- **Folder split:** a feature folder splits into `sections/` (larger composed blocks), `widgets/` (small reusable pieces), and sometimes `forms/` — the same split `src/layouts/` uses. Add a subfolder only once more than one file belongs in it.
- **`ui/` purity:** `ui/` holds primitives with no feature knowledge (a button doesn't know about chat or wallet) — a component that reads a specific domain's API/hooks belongs in that feature's folder. `ui/icons/` and `ui/motion/` are barrel-backed subfolders; import through their `index.ts`.
- **Ported components:** the top-of-file counterpart comment (root rule) also calls out deliberate native-vs-web UX deviations — never silently diverge from the web component.
- **`profile/` vs `profiles/`:** deliberately separate — the signed-in user's own account/settings vs saved family-and-friend subject profiles. Don't merge them.
- **New feature folders:** before adding one, check the component doesn't belong in an existing folder — most new screens extend `dashboard/`, `chart/`, `chat/`, `wallet/`, etc.

## Structure

`ui/` — app-wide primitives (button, avatar, bottom-sheet, text-field, snackbar, …) plus the `icons/` and `motion/` barrel subfolders. One feature folder per domain (`auth/`, `chart/`, `chat/`, `dashboard/`, `match/`, `onboarding/`, `panchang/`, `paywall/`, `profile/`, `profiles/`, `reports/`, `wallet/`, …) — check the folder listing for the current set. `reports/` holds the shared report scaffolding (`coming-soon.tsx`, `report-glyph.tsx`, `widgets/`) plus one subfolder per shipped report (`mangal-dosha/`).
