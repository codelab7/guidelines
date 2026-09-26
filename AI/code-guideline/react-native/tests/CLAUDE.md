# tests - Tests

The test framework is not settled yet. See the checklist in `README.md`. These rules hold
whichever one the project picks.

- Tests live in this top-level folder, not next to the source file.
- One file per subject, named `{subject}.test.ts`.
- Import through the `@/` alias, the same way the app does.
- Fixtures sit beside the test that uses them.
- Test pure logic from `utils/` first. That is where a test is cheap and catches real bugs.
- A test that needs a native module mocked is a sign the logic should be pulled out of the
  integration and into a pure helper.
- Never write a test that only repeats the implementation. Test the behaviour the user depends on.
