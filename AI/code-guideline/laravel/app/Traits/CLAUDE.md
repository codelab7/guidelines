# app/Traits - Traits

- Traits live in `app/Traits/`, namespace `App\Traits`, named after the behaviour they add:
  `FileUploadTrait`, `LocalIdHelperTrait`.
- A trait shares one small, cohesive behaviour. Nothing else.
- No god traits. When a trait mixes unrelated responsibilities, split it.
- Once the behaviour needs its own state, dependencies, or branching, make it a service and inject
  it instead.
- One trait per line in the class that uses it.
