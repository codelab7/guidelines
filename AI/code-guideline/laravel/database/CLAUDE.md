# database/ - Database Design

Rules for the database layer as a whole. Migration mechanics live in `migrations/CLAUDE.md`.

- No database enum columns. Store a string or integer and cast a PHP enum from `app/Enums/` on the
  model.
- No column defaults in the schema. Defaults belong on the model.
- No cascades, triggers, or complex database constraints. Model that behaviour in Laravel with
  relationships, events, observers, or services.
- Index what you query: every foreign key, and any column used often in a `where` or `order by`.
- Soft deletes are the default deletion strategy.
- Table names are plural snake_case. Column names are snake_case.
