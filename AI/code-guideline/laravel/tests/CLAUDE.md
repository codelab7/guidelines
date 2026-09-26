# tests/ - Tests

- Write tests with Pest.
- Prefer a feature test that goes through the route. Add a unit test only for logic that is hard to
  reach over HTTP, such as a calculation inside a service.
- Build data with factories. Never handwrite an array of attributes.
- Follow arrange, act, assert, with a blank line between the three parts.
- The test name is a sentence describing the behaviour:
  `it('rejects a transaction with no line items')`.
- Never put a comment in a test. If a test needs explaining, rename it or split it.
- Assert both sides: the response (status, redirect, flash, payload) and the database effect
  (`assertDatabaseHas`, `assertSoftDeleted`).
- Use `RefreshDatabase` so every test starts clean.
- One behaviour per test. A test asserting two unrelated things is two tests.
