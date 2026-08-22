# React Template

`CLAUDE.md` files for a standalone React app, for example one built with Vite. Copy them into your
project, keeping the same folder paths, so each folder carries its own rules. Claude Code reads
the `CLAUDE.md` of the folder it is working in, so the rules for a layer load only while you are
in that layer.

These files are the rules. [REACT_GUIDELINE.md](../REACT_GUIDELINE.md) is now an index that points
at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour that isn't
React-specific.

Use [laravel-react/](../laravel-react/) instead if the React code lives inside a Laravel project.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: communication, planning, code output, debugging, MCP servers. |
| `src/CLAUDE.md` | Rules for all frontend code: TypeScript, naming, Tailwind, responsiveness, libraries. |
| `src/api/CLAUDE.md` | Calls to the backend, grouped by domain. |
| `src/components/CLAUDE.md` | Where a component goes, minimum props, composition, updating every usage. |
| `src/components/ui/CLAUDE.md` | Library primitives and shadcn/ui wrappers. |
| `src/components/shared/CLAUDE.md` | Generic project UI with no domain knowledge. |
| `src/components/specific/CLAUDE.md` | Domain components used by more than one module. |
| `src/hooks/CLAUDE.md` | Custom hooks reusable across the app, for example `use-debounce.ts`. |
| `src/i18n/CLAUDE.md` | Translation files. Only used if the project supports translations. |
| `src/layouts/CLAUDE.md` | Page shells. |
| `src/layouts/sections/CLAUDE.md` | Large parts of a shell, such as the sidebar and header. |
| `src/layouts/widgets/CLAUDE.md` | Small pieces inside a shell. |
| `src/pages/CLAUDE.md` | One folder per module, the page/section/widget roles, and form rules. |
| `src/stores/CLAUDE.md` | Client state with Zustand. |
| `src/styles/CLAUDE.md` | Global stylesheet and Tailwind setup. |
| `src/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `src/utils/CLAUDE.md` | Shared helper functions. Check here before writing a new helper. |

This is not the whole tree. It only covers folders that need their own rules. A module's own
`sections/` and `widgets/` folders are created per module under `pages/{module}/`, and their rules
live in `pages/CLAUDE.md`.

## Naming

- Files: `kebab-case`, for example `contact-list.tsx`
- Components: `PascalCase`, for example `ContactList`
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## Before You Copy

The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`.
Those paths are relative to the project you copy into, not to this repository. Create that `docs/`
folder, or edit the paths, or the links will not resolve.

## Checklist - Rules Still Missing

Decisions we haven't settled yet. Work through these and add the answer to the matching
`CLAUDE.md`, or create the file if there isn't one.

- [ ] Icons: the old spec named `lucide-react` and we settled on Phosphor, following
      `code-decisions/preferred-libraries.md`. Confirm the existing projects match, or record the
      exception.
- [ ] Utils file suffix: formatting helpers are named `number.enums.ts` and `date.enums.ts` while
      validation helpers are `validation.utils.ts`. The `.enums.ts` suffix on a file holding no
      enum looks like a leftover. Pick one suffix and correct `utils/CLAUDE.md`.
- [ ] Frontend testing: there are no rules at all today. Decide on Vitest, Testing Library, or
      Playwright, and what must be covered.
- [ ] ESLint and Prettier: which preset is enforced, and whether typecheck and lint run in CI.
- [ ] Module-level types: whether a module keeps a `{module}-types.ts` or everything lands in
      `types/`.
- [ ] `api/`: the error shape, loading state, and retry policy.
- [ ] `stores/`: what is allowed in a store, and where the line sits against the data cache.
- [ ] Permissions: how the UI is gated, and whether a shared `<Can>` component exists.
- [ ] Shared patterns with no home yet: toasts, modals, confirm dialogs, data tables, pagination,
      and file upload.
- [ ] Router: React Router or TanStack Router, and where the route definitions live.
- [ ] Data fetching: TanStack Query or plain calls in `api/`, and where the cache config lives.
- [ ] Form library, since there is no Inertia `useForm` here.
- [ ] Auth and session handling, plus how env config is read and typed.
