# src/hooks/ — Rules

## What this is

Every shared React hook in the app — generic (`useTheme`, `useDebouncedValue`) and domain-specific alike (`usePanchang`, `useWallet`). If it's a hook and more than one screen could use it, it lives here; `src/lib/` holds no hooks.

## Rules

- **File shape:** one hook per file, kebab-case (`use-debounced-value.ts`).
- **Barrel:** register every hook in `src/hooks/index.ts`; outside consumers import through `@/hooks`, never a per-file path. Inside the folder, hook files import each other relatively (`./use-otp-timers`), never via the barrel.
- **Thin hooks:** hooks are state/effect glue — calculations and API calls live in `src/lib/`/`src/api/`, never inline in the hook body (e.g. `use-panchang.ts` wraps `@/lib/panchang` + `@/lib/geolocation`).
- **Server state (canonical rule):** all server state goes through TanStack Query here (`useQuery`/`useMutation`), invalidating `['wallet']`-style query keys after a spend rather than a custom refresh event. No context-owned server state anywhere in the app.
- **Platform forks:** a hook needing a web-specific implementation ships a `.web.ts` sibling (`use-color-scheme.web.ts`) rather than an inline `Platform.OS === 'web'` branch.

## Structure

Hooks behind the `src/hooks/index.ts` barrel, grouped by area: chat, astrology data, wallet/payments, personalization, profiles, reports, and UI/system (including `use-color-scheme` with its `.web.ts` sibling) — check the folder listing for the current set.
