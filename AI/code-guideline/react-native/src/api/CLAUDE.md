# src/api/ — Rules

## What this is

The only layer in the app allowed to call `fetch` against **kgpt-api**. Every backend resource gets one file exporting typed functions that hooks and screens call — no component or hook talks to `fetch` directly. Ported from `kgpt-app-ui/src/api/` where sensible; keep shapes and error handling in sync with it.

## Rules

- **Always go through `client.ts`:** call `request()`/`apiFetch()` from `./client` — never `fetch()` directly. `apiFetch` builds the URL from `API_URL` (`@/lib/app-config`), sends `credentials: 'omit'` (deliberate: a manually-set auth header and automatic cookie credentials would fight each other), and injects auth headers via `getAuthHeaders()`/`setAuthHeadersProvider()`. Only the chat streaming transport (which builds its own `fetch` for SSE) reads `getAuthHeaders()` directly instead of going through `request`.
- **Error handling:** on a non-OK response, `request`/`requestText` funnel through `handleApiError()` in `./errors` — it inspects the status (401/402/403/409) and throws a typed error (`InsufficientCoinsError`, `SubscriptionRequiredError`, `ProfileLimitError`, `ChatFullError`, …), opening the relevant paywall sheet via `@/lib/paywall-channel` for 402s along the way. Never hand-roll status-code branching in an API file — extend `errors.ts` instead, and keep it a faithful port of `kgpt-app-ui/src/api/errors.ts` (same classes, same server-body parsing) so both clients interpret kgpt-api failures identically.
- **No business logic:** a file here shapes a request, calls `request`, and returns the typed response — state, caching, and side effects belong in `src/hooks/` (TanStack Query) or `src/lib/`.
- **Types:** response/payload shapes live in `src/types/api.ts`, mirrored from the kgpt-api *source code* (not its docs) — import them, never redeclare inline.

## Structure

`client.ts` (the shared `apiFetch`/`request` wrapper + auth-header injection point), `errors.ts` (error taxonomy + `handleApiError`), plus one file per backend resource (`chat.ts`, `coins.ts`, `reports.ts`, …) — check the folder listing for the current set.
