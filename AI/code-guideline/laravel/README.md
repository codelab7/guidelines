# Laravel Template

`CLAUDE.md` files for a Laravel project. Copy them into your project, keeping the same folder
paths, so each folder carries its own rules. Claude Code reads the `CLAUDE.md` of the folder it is
working in, so the rules for a layer load only while you are in that layer.

These files are the rules. [PHP_LARAVEL_GUIDELINE.md](../PHP_LARAVEL_GUIDELINE.md) is now an index
that points at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour
that isn't Laravel-specific.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: communication, planning, code output, debugging, MCP servers. |
| `app/CLAUDE.md` | PHP style, control flow, Laravel basics, and the layer map. |
| `app/Http/CLAUDE.md` | Shared HTTP layer rules and the delegation order. |
| `app/Http/Controllers/CLAUDE.md` | Controller naming, the CRUD method set, what must never live in a controller. |
| `app/Http/Requests/CLAUDE.md` | One form request per intent. Rules, messages, and `authorize()` only. |
| `app/Http/Middleware/CLAUDE.md` | Stateless cross-cutting concerns. No domain logic. |
| `app/Services/CLAUDE.md` | How to write a service: one domain per service, fluent calls, typed results. |
| `app/Models/CLAUDE.md` | Casts, soft deletes, model-level defaults, scopes. |
| `app/Enums/CLAUDE.md` | Backed PHP enums instead of database enum columns. |
| `app/Traits/CLAUDE.md` | Small shared behaviours. No god traits. |
| `app/Helpers/CLAUDE.md` | Pure helper functions with no framework access. |
| `database/CLAUDE.md` | Database design: no DB enums, no cascades, index what you query. |
| `database/migrations/CLAUDE.md` | Schema mechanics. `up()` only, no defaults, no `enum()`. |
| `database/factories/CLAUDE.md` | One factory per model, states for variations. |
| `database/seeders/CLAUDE.md` | Idempotent seeders built from factories. |
| `routes/CLAUDE.md` | URLs in kebab-case, route names in camelCase, tuple notation. |
| `tests/CLAUDE.md` | Pest, feature tests first, factories for data. |

This is not the whole Laravel tree. It only covers folders that need their own rules; everything
else keeps the default Laravel layout.

## Layer Responsibilities

Move logic downwards to keep controllers thin:

1. **Controller** - receives the request, delegates, returns a response.
2. **Form request** - validation and simple authorization.
3. **Service** - business logic and multi-step workflows.
4. **Model** - persistence, relationships, casts, and scopes.

See section 2 of the [Laravel guideline](../PHP_LARAVEL_GUIDELINE.md) for the detail on each layer.

## Before You Copy

The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`.
Those paths are relative to the project you copy into, not to this repository. Create that `docs/`
folder, or edit the paths, or the links will not resolve.

## Checklist - Rules Still Missing

Decisions we haven't settled yet. Work through these and add the answer to the matching
`CLAUDE.md`, or create the file if there isn't one.

- [ ] `single` vs `show` for the controller method that renders one resource. Our spec says
      `single`; Laravel convention is `show`. Pick one and make `app/Http/Controllers/CLAUDE.md`
      match.
- [ ] Helpers: global functions or static classes, how they are autoloaded, and when a helper is
      allowed instead of a service.
- [ ] Factories and seeders: confirm the starting rules match how we actually seed, especially
      whether demo data ships outside local, and how it is gated per environment.
- [ ] Routes: splitting `web.php` and `api.php`, route model binding, how hashed IDs interact with
      binding, and how middleware groups are organised.
- [ ] Authorization: policy naming, where gates are defined, and whether `app/Policies/` needs its
      own `CLAUDE.md`.
- [ ] API responses: when to use an API Resource, the JSON envelope shape, the error format, and
      pagination.
- [ ] Where service Result objects and DTOs live, and how they are named.
- [ ] Jobs and queues, console commands, events, listeners, observers, notifications, and
      mailables: decide which of these folders need their own `CLAUDE.md`.
- [ ] Exception handling: custom exception classes and which layer catches them.
- [ ] Static analysis: whether Larastan or a specific Pint preset is required, and at what level.
- [ ] `config/` conventions: kebab-case file names, snake_case keys, and where service credentials
      go.
