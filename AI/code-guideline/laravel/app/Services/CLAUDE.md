# app/Services — Writing Services

Service-specific rules only. These sit on top of the project's general PHP/Laravel conventions
and the root `CLAUDE.md` — don't restate those here.

- One service = one domain's purpose. No domain overlap; logic for another domain goes behind
  that domain's service.
- Serve a domain, not a controller. Never couple a service to one controller; thinning
  controllers is a side effect, not the goal. The same service must work from a controller,
  command, job, or another service unchanged.
- Prefer chain (fluent) calling: static named constructors (`for()`, `forProduct()`,
  `fromRap()`) and `with*()` setters return `self`, closed by a terminal method.

  ```php
  DiamondPriceService::for($shape, $clarity, $color, $weight)
      ->withFinalPrice($finalPrice)
      ->withDiscount($discount)
      ->estimatedFormat();
  ```

- Layout: `app/Services/{Domain}/`, namespace `App\Services\{Domain}`, class `{Domain}{Role}Service`.
- Return a typed `final readonly` Result object, never an untyped array. Share sibling logic via
  a small abstract base, not a god-trait.
- Two-tier errors: `throw \RuntimeException` for whole-operation failures; collect per-row
  failures into the Result and keep going.
- Multi-model writes go through `DB::transaction()`.
- No `request()` inside services — pass plain values in. Inject via the container; don't `new`.
