# database/seeders - Seeders

- A seeder inserts data and nothing else. No business rules, no HTTP calls.
- Build records with factories, not handwritten arrays.
- A seeder must be safe to run twice. Use `firstOrCreate` or `updateOrCreate` for reference data.
- Keep reference data (roles, currencies, account types) in its own seeder, separate from demo
  data, and call each from `DatabaseSeeder`.
