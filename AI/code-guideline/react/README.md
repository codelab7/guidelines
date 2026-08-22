# React Template

`CLAUDE.md` files for a standalone React app, for example one built with Vite. Copy them into your project, keeping the same folder paths, so each folder carries its own rules.

The full rules live in [REACT_GUIDELINE.md](../REACT_GUIDELINE.md) and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md). These files hold only what is specific to a folder.

Use [laravel-react/](../laravel-react/) instead if the React code lives inside a Laravel project.

## Files

All of these are blank so far. Fill them in as conventions settle.

| File | Covers |
|------|--------|
| `src/CLAUDE.md` | Rules for all frontend code: TypeScript only, functional components, hooks. |
| `src/api/CLAUDE.md` | Calls to the backend, grouped by domain. |
| `src/components/CLAUDE.md` | Reusable components. Split into `ui/` for library primitives, `shared/` for general project components, and `specific/` for domain components used in more than one place. |
| `src/hooks/CLAUDE.md` | Custom hooks reusable across the app, for example `use-debounce.ts`. |
| `src/i18n/CLAUDE.md` | Translation files. Only used if the project supports translations. |
| `src/layouts/CLAUDE.md` | Page shells, plus `sections/` and `widgets/` used inside them. |
| `src/pages/CLAUDE.md` | One folder per module, each with its own `sections/` and `widgets/`. |
| `src/stores/CLAUDE.md` | Global client state. |
| `src/styles/CLAUDE.md` | Global stylesheets and Tailwind setup. |
| `src/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `src/utils/CLAUDE.md` | Shared helper functions. Check here before writing a new helper. |

## Naming

- Files: `kebab-case`, for example `contact-list.tsx`
- Components: `PascalCase`, for example `ContactList`
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
