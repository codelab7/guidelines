# Laravel Template

`CLAUDE.md` files for a Laravel project. Copy them into your project, keeping the same folder paths, so each folder carries its own rules.

The full rules live in [PHP_LARAVEL_GUIDELINE.md](../PHP_LARAVEL_GUIDELINE.md) and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md). These files hold only what is specific to a folder.

## Files

| File | Covers | Status |
|------|--------|--------|
| `CLAUDE.md` | Project-wide agent rules: communication, planning, code output, debugging, MCP servers. | Written |
| `app/CLAUDE.md` | Applies the PHP/Laravel spec to everything under `app/`. | Written |
| `app/Http/CLAUDE.md` | Controllers, form requests, and middleware. | Blank |
| `app/Services/CLAUDE.md` | How to write a service: one domain per service, fluent calls, typed results. | Written |
| `app/Helpers/CLAUDE.md` | Shared helper functions. | Blank |
| `database/CLAUDE.md` | Database layer as a whole. | Blank |
| `database/migrations/CLAUDE.md` | Schema changes. No database enums, no cascades, no column defaults. | Blank |
| `routes/CLAUDE.md` | Route files. URLs in kebab-case, route names in camelCase. | Blank |
| `tests/CLAUDE.md` | Feature and unit tests. | Blank |

This is not the whole Laravel tree. It only covers folders that need their own rules; everything else keeps the default Laravel layout.

## Layer Responsibilities

Move logic downwards to keep controllers thin:

1. **Controller** - receives the request, delegates, returns a response.
2. **Form request** - validation and simple authorization.
3. **Service** - business logic and multi-step workflows.
4. **Model** - persistence, relationships, casts, and scopes.

See section 3 of the Laravel guideline for the detail on each layer.

## Before You Copy

`CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`, and `app/CLAUDE.md` imports a spec from `docs/`. Those paths are relative to the project you copy into, not to this repository. Create that `docs/` folder, or edit the paths, or the imports will not resolve.
