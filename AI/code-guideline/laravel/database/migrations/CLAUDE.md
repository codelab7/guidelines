# database/migrations - Migrations

Schema mechanics only. The design rules are in the parent `CLAUDE.md`.

- Write the `up()` method only. Never add a `down()` method.
- One logical schema change per migration. Don't bundle unrelated tables.
- Foreign keys use `foreignId(...)->constrained()`. No `onDelete` or `onUpdate` clauses.
- Add `$table->softDeletes()` to any table holding records the app can delete.
- Add `$table->index(...)` for foreign keys and frequently filtered columns.
- Never set `->default(...)` on a column.
- Never use `$table->enum(...)`.
