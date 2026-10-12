# database/factories - Factories

- One factory per model, named `{Model}Factory`.
- `definition()` returns a valid, minimal record. Every required column gets a realistic fake value.
- Put variations in named states (`unpaid()`, `withLineItems()`), not in extra factory classes.
- Use enum cases for enum columns, never the raw backing string.
- Set relationships with the related factory so a factory call works on its own.
- Don't randomise a column a test asserts on. The test passes that value explicitly.
