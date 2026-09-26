# resources/js/components/specific - Domain Components

- Domain-aware components used by more than one module: `team-members-list.tsx`.
- May use domain types from `types/`.
- Never import from a single module's folder. If it needs one module's internals, it belongs in
  that module's `widgets/`.
- Still takes its data through props. Fetching stays in the page or section.
