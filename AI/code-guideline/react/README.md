# React Template

`CLAUDE.md` files for a standalone React app, for example one built with Vite. Copy them into your project, keeping the same folder paths, so each folder carries its own rules. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the rules for a layer load only while you are in that layer.

These files are the rules. [REACT_GUIDELINE.md](../REACT_GUIDELINE.md) is now an index that points at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour that isn't React-specific.

Use [laravel-react/](../laravel-react/) instead if the React code lives inside a Laravel project.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: stack, commands, communication, planning, code output, debugging, MCP servers. |
| `src/CLAUDE.md` | Rules for all frontend code: TypeScript, naming, imports, styling, responsiveness, libraries, security, and the import table. |
| `src/api/CLAUDE.md` | Calls to the backend and their TanStack Query hooks, one file per resource. Error shape, auth, cache. |
| `src/components/CLAUDE.md` | Where a component goes, promoting to `shared/`, file layout, props types, composition, updating every usage. |
| `src/components/ui/CLAUDE.md` | Thin wrappers around the UI library's components. |
| `src/components/shared/CLAUDE.md` | Components reused by two or more features, including `<Can>`. |
| `src/components/features/CLAUDE.md` | One folder per feature: section and widget roles, `forms/`, feature-only helpers and hooks, form rules. |
| `src/components/layouts/CLAUDE.md` | The parts a layout is built from, such as the sidebar and header. |
| `src/hooks/CLAUDE.md` | Custom hooks reusable across the app, for example `use-debounce.ts`. |
| `src/i18n/CLAUDE.md` | Translation files. Only used if the project supports translations. |
| `src/layouts/CLAUDE.md` | Layout routes. The shell's parts, such as the sidebar and header, live in `components/layouts/`. |
| `src/pages/CLAUDE.md` | One file per route page, grouped in a feature folder when a feature has more than one. The page role only: route params, title, placing sections. |
| `src/schemas/CLAUDE.md` | Zod form schemas. Only used if the project validates forms with Zod. |
| `src/stores/CLAUDE.md` | Client state with Zustand, and where each kind of state goes. |
| `src/styles/CLAUDE.md` | Global stylesheet and the UI library's theme. |
| `src/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `src/utils/CLAUDE.md` | Shared helper functions. Check here before writing a new helper. |

This is not the whole tree. It only covers folders that need their own rules. A feature's sections and its `forms/` and `widgets/` folders are created per feature under `components/features/{feature}/`, and their rules live in `components/features/CLAUDE.md`.

## Folder File Layout

Every `CLAUDE.md` under `src/` uses the same sections, in this order. Keep new files to it.

1. Intro - what the folder holds, in one or two sentences.
2. `Structure` - how files and subfolders are laid out and what role each one plays.
3. `Rules` - what to follow while working in the folder.
4. `Boundaries` - what the folder may import, and what belongs somewhere else. Skip it when the folder has neither.
5. `Before You Finish` - checks to run before the work is done. Only where needed.
6. `Existing ...` - a table of what the folder already holds, so the agent can check for an existing hook, helper, or component without opening every file. The agent must update it in the same change whenever it adds, renames, or removes a file there. The tables start empty - fill them in when you copy the template into a project.

The root `CLAUDE.md` holds agent behaviour, not folder rules, so it keeps its own layout.

## Naming

- Files and folders: `kebab-case`, for example `contact-list.tsx`
- Feature folders: plural, for example `components/features/sales/`
- Components: `PascalCase`, for example `ContactList`
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## Before You Copy

The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`. Those paths are relative to the project you copy into, not to this repository. Create that `docs/` folder, or edit the paths, or the links will not resolve.

Then fill in the `Stack` and `Commands` sections of the root `CLAUDE.md` for the project. The agent runs those commands before it finishes, so they must be the project's real scripts.

## Checklist - Rules Still Missing

Decisions we haven't settled yet. Work through these and add the answer to the matching `CLAUDE.md`, or create the file if there isn't one.

- [ ] ESLint and Prettier: which preset is enforced, and whether typecheck and lint run in CI.
- [ ] Frontend testing: there are no tests for now, and the agent must not add a test setup. Revisit when a project needs tests.
- [ ] `react-native/` still uses `components/{feature}/` and `components/specific/`. Decide whether to align it with `components/features/{feature}/` and the merged `shared/`.
