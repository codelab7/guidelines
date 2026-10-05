# src/components/ui - Library Primitives

- Library primitives and thin wrappers only.
- Keep local edits minimal so an upstream update can still be applied.
- No domain knowledge, no data fetching, no business rules.
- A component that needs project context belongs in `shared/`, not here.
