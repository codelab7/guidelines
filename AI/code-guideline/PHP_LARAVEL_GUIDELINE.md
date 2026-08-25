# Laravel Implementation Guidelines (AGENT Spec)

Framework-specific rules for how the AI coding agent must structure and write Laravel + PHP code.
These build on [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md) and the Spatie PHP & Laravel AI Guidelines.

---

## 1. Where the Rules Live

The rules are not in this file. They sit next to the code they govern, in the `CLAUDE.md` of each
folder of the [laravel/](laravel/) template. Claude Code reads the `CLAUDE.md` of the folder it is
working in, so the migration rules load while a migration is open and stay out of the way the rest
of the time.

Copy the [laravel/](laravel/) tree into a project, keeping the folder paths, and the rules apply
themselves. This table is for humans looking for a rule.

| Rule area | File |
|-----------|------|
| Agent behaviour across the project | [laravel/CLAUDE.md](laravel/CLAUDE.md) |
| PHP style, control flow, Laravel basics | [laravel/app/CLAUDE.md](laravel/app/CLAUDE.md) |
| HTTP layer, delegation order | [laravel/app/Http/CLAUDE.md](laravel/app/Http/CLAUDE.md) |
| Controllers | [laravel/app/Http/Controllers/CLAUDE.md](laravel/app/Http/Controllers/CLAUDE.md) |
| Form requests | [laravel/app/Http/Requests/CLAUDE.md](laravel/app/Http/Requests/CLAUDE.md) |
| Middleware | [laravel/app/Http/Middleware/CLAUDE.md](laravel/app/Http/Middleware/CLAUDE.md) |
| Services | [laravel/app/Services/CLAUDE.md](laravel/app/Services/CLAUDE.md) |
| Models | [laravel/app/Models/CLAUDE.md](laravel/app/Models/CLAUDE.md) |
| Enums | [laravel/app/Enums/CLAUDE.md](laravel/app/Enums/CLAUDE.md) |
| Traits | [laravel/app/Traits/CLAUDE.md](laravel/app/Traits/CLAUDE.md) |
| Helpers | [laravel/app/Helpers/CLAUDE.md](laravel/app/Helpers/CLAUDE.md) |
| Database design | [laravel/database/CLAUDE.md](laravel/database/CLAUDE.md) |
| Migrations | [laravel/database/migrations/CLAUDE.md](laravel/database/migrations/CLAUDE.md) |
| Factories | [laravel/database/factories/CLAUDE.md](laravel/database/factories/CLAUDE.md) |
| Seeders | [laravel/database/seeders/CLAUDE.md](laravel/database/seeders/CLAUDE.md) |
| Routes | [laravel/routes/CLAUDE.md](laravel/routes/CLAUDE.md) |
| Tests | [laravel/tests/CLAUDE.md](laravel/tests/CLAUDE.md) |

A rule belongs in exactly one of those files. When a rule changes, change it there, not here.

---

## 2. Layer Responsibilities

This is the one rule with no single owning folder, so it stays in this document. Move logic
downwards until it sits in the lowest layer that can hold it.

1. **Controller** - receives the HTTP request, delegates, returns a response. Nothing else.
2. **Form request** - validation rules, messages, and simple authorization.
3. **Service** - business logic, domain rules, and multi-step workflows. Usable from a controller,
   a console command, or a job without change.
4. **Model** - persistence: relationships, casts, scopes, small query helpers.
5. **Middleware** - stateless cross-cutting concerns on the request pipeline.

If a piece of logic would be identical when triggered from a console command, it does not belong
in the HTTP layer.

---

## 3. Agent Behaviour Summary for Laravel

When working on Laravel code, the AI coding agent must:

1. Read the `CLAUDE.md` of the folder it is editing before writing code in that folder.
2. Respect the layer responsibilities in section 2.
3. Prefer Eloquent and Laravel conventions over custom patterns unless the project clearly defines
   otherwise.
4. Use PHP enums, soft deletes, casts, and model-level defaults instead of database enums,
   cascades, and column defaults.
5. Keep code small, readable, and consistent across every module.
