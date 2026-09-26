# app/Http - HTTP Layer

Shared rules for the HTTP layer. Controllers, form requests, and middleware each have their own
`CLAUDE.md` with the detail.

- Delegate in a fixed order: validation to a `FormRequest`, authorization to a policy or gate,
  business logic to a service, persistence to Eloquent.
- Nothing here decides a domain rule. If the rule would be the same when triggered from a console
  command or a job, it belongs in a service.
- Type-hint what you receive. Resolve dependencies through the container, never with `new`.
- Keep query building out of this layer beyond simple CRUD lookups.
