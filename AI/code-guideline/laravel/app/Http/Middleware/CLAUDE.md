# app/Http/Middleware - Middleware

- Middleware handles cross-cutting request concerns only: decoding hashed IDs, sharing Inertia
  props, small request pre- or post-processing.
- Keep it stateless and fast. It runs on every matching request.
- No business logic and no domain branching.
- No side effects that outlive the request, such as writes unrelated to the pipeline.
- When middleware starts needing a domain rule, move that rule into a service and call it.
