# src/components/ui - Library Primitives

- Library primitives and thin wrappers only.
- Keep local edits minimal so an upstream update can still be applied.
- No domain knowledge, no data fetching, no business rules. A button does not know what a sale is.
- A component that needs project context belongs in `shared/`, not here.
- This is where cross-cutting behaviour is enforced once: haptics on press, the minimum 44pt touch
  target, the disabled and loading states. A screen should never re-implement them.
