# app/Helpers - Helpers

- A helper is a pure function: same input, same output, no side effects.
- No database access, no facades, no reading the request or config.
- Anything with domain meaning is a service, not a helper.
- Group helpers by topic and name them for what they return.
