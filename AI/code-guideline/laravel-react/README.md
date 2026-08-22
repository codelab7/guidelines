# Laravel + React Template

`CLAUDE.md` files for the frontend of a Laravel project that uses Inertia and React. Copy them into your project, keeping the same folder paths, so each folder carries its own rules.

The full rules live in [REACT_GUIDELINE.md](../REACT_GUIDELINE.md) and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md). These files hold only what is specific to a folder.

For the backend files, use [laravel/](../laravel/). Use [react/](../react/) instead if the React app is standalone.

## Files

All of these are blank so far. Fill them in as conventions settle.

| File | Covers |
|------|--------|
| `resources/js/CLAUDE.md` | Rules for all frontend code: TypeScript only, functional components, hooks. |
| `resources/js/api/CLAUDE.md` | Calls to backend endpoints that are not Inertia pages. |
| `resources/js/components/CLAUDE.md` | Reusable components. Split into `ui/` for library primitives, `shared/` for general project components, and `specific/` for domain components used in more than one place. |
| `resources/js/hooks/CLAUDE.md` | Custom hooks reusable across the project. |
| `resources/js/layouts/CLAUDE.md` | Page shells, plus `sections/` and `widgets/` used inside them. |
| `resources/js/pages/CLAUDE.md` | One folder per module, each with its own `sections/` and `widgets/`. Laravel controllers render these through Inertia. |
| `resources/js/store/CLAUDE.md` | Global client state. |
| `resources/js/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `resources/js/utils/CLAUDE.md` | Shared helper functions. Check here before writing a new helper. |

## Working with Inertia

- Controllers return Inertia responses, not JSON. Use JSON only for real API endpoints.
- Page components sit in `pages/{module}/` and stay thin. Most logic goes in `sections/`.
- Read `auth`, `flash`, and `permissions` from the shared props set by `HandleInertiaRequests`.
- Generate URLs with Ziggy or WayFinder. Do not hardcode paths.
