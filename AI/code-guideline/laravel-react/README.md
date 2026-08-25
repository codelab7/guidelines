# Laravel + React Template

`CLAUDE.md` files for the frontend of a Laravel project that uses Inertia and React. Copy
`resources/` into your project, keeping the same folder paths, so each folder carries its own
rules. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the rules for a layer
load only while you are in that layer.

These files are the rules. [REACT_GUIDELINE.md](../REACT_GUIDELINE.md) is now an index that points
at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour that isn't
React-specific.

For the backend files and the project root `CLAUDE.md`, use [laravel/](../laravel/). This template
covers the frontend only. Use [react/](../react/) instead if the React app is standalone.

## Files

| File | Covers |
|------|--------|
| `resources/js/CLAUDE.md` | Rules for all frontend code: TypeScript, naming, Tailwind, responsiveness, Inertia, libraries. |
| `resources/js/api/CLAUDE.md` | Direct backend calls, for the few cases that are not Inertia page loads. |
| `resources/js/components/CLAUDE.md` | Where a component goes, minimum props, composition, updating every usage. |
| `resources/js/components/ui/CLAUDE.md` | Library primitives and shadcn/ui wrappers. |
| `resources/js/components/shared/CLAUDE.md` | Generic project UI with no domain knowledge. |
| `resources/js/components/specific/CLAUDE.md` | Domain components used by more than one module. |
| `resources/js/hooks/CLAUDE.md` | Custom hooks reusable across modules. |
| `resources/js/layouts/CLAUDE.md` | Page shells. |
| `resources/js/layouts/sections/CLAUDE.md` | Large parts of a shell, such as the sidebar and header. |
| `resources/js/layouts/widgets/CLAUDE.md` | Small pieces inside a shell. |
| `resources/js/pages/CLAUDE.md` | One folder per module, the page/section/widget roles, and form rules. |
| `resources/js/stores/CLAUDE.md` | Client state with Zustand. |
| `resources/js/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `resources/js/utils/CLAUDE.md` | Shared helper functions. Check here before writing a new helper. |

This is not the whole frontend tree. It only covers folders that need their own rules. A module's
own `sections/` and `widgets/` folders are created per module under `pages/{module}/`, and their
rules live in `pages/CLAUDE.md`.

## Working with Inertia

- Controllers return Inertia responses, not JSON. Use JSON only for real API endpoints.
- Page components sit in `pages/{module}/` and stay thin. Most logic goes in `sections/`.
- Read `auth`, `flash`, and `permissions` from the shared props set by `HandleInertiaRequests`.
- Generate URLs with Ziggy or WayFinder. Do not hardcode paths.

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
- [ ] `api/`: the error shape, loading state, and retry policy for a call that is not a page load.
- [ ] `stores/`: whether an Inertia project uses a client store at all, and what is allowed in it.
- [ ] Permissions: how the `permissions` shared prop gates UI, and whether a shared `<Can>`
      component exists.
- [ ] Shared patterns with no home yet: toasts, modals, confirm dialogs, data tables, pagination,
      and file upload.
- [ ] Forms: whether Inertia `useForm` is mandatory, or a form library is allowed for complex
      flows.
- [ ] i18n: whether `resources/js/i18n/` is used, and with which library.
- [ ] Styling: whether `resources/css/` needs its own `CLAUDE.md`, plus the Tailwind version and
      where theme tokens live.
- [ ] Confirm the `store/` to `stores/` rename, which was made here to match the standalone
      template.
- [ ] `AI/.claude/agents/code-refactor-docs.md` tells its agent to read `/docs/REACT_GUIDELINES.md`
      (a name that doesn't exist here), to follow Redux Toolkit patterns, and to add JSDoc
      comments. All three now conflict with these rules. Decide whether that agent gets updated.
