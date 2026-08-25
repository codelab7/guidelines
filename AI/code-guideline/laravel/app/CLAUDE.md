# app/ - PHP and Laravel Rules

Rules for all PHP code under `app/`. Each subfolder has its own `CLAUDE.md` with the rules for
that layer. Don't restate the root `CLAUDE.md` here.

## PHP Style

- Follow PSR-12. Run `./vendor/bin/pint` before finishing a change.
- Keep classes small, focused, and single-responsibility.
- Use typed properties and parameter types. Always declare a return type, including `void`.
- Short nullable notation: `?string`, never `string|null`.
- Use constructor property promotion when every property can be promoted.
- One trait per line in a `use` statement.
- Skip docblocks on fully type-hinted methods. Add one only for a description or a generic, and
  import the class names instead of writing them fully qualified:

  ```php
  /** @return Collection<int, User> */
  public function getUsers(): Collection
  ```

- Names must state intent. No abbreviations, no cryptic short names.

## Control Flow

- Happy path last. Handle the failure cases first and return early.
- Avoid `else`. Use early returns instead of nesting.
- Prefer several small `if` statements over one compound condition.
- Always use curly braces, even for a single statement.
- String interpolation over concatenation: `"Hello {$name}"`.
- Let the code breathe. Blank lines between statements, none directly inside `{}`.

## Laravel

- Prefer Laravel's standard APIs over custom helpers unless the project already defines them.
- Prefer Eloquent over raw database queries. Justify any raw query.
- Read configuration with `config()`. Never call `env()` outside `config/`.
- Don't add localization or i18n unless the project already uses it or the user asks for it.
- Keep methods short. Support a public method with small private methods that each do one thing.

## Comments

- Names carry the meaning. A comment is the last resort, not the first move.
- Comment only *why* something non-obvious is done, never *what* the code does.

## Layer Map

Push logic downwards so controllers stay thin:

1. `Http/Controllers` - receive the request, delegate, return a response.
2. `Http/Requests` - validation and simple authorization.
3. `Services` - business logic and multi-step workflows.
4. `Models` - persistence: relationships, casts, scopes.

When logic could sit in two layers, put it in the lower one.
