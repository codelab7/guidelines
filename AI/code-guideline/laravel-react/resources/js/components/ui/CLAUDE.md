# resources/js/components/ui - Library Primitives

- Library primitives and thin wrappers only. This is where shadcn/ui components land.
- Generate them with the shadcn CLI or the Shadcn MCP. Don't hand-write a primitive that the
  library already ships.
- Keep local edits minimal so an upstream update can still be applied.
- No domain knowledge, no data fetching, no business rules, no Inertia props.
- A component that needs project context belongs in `shared/`, not here.
