# app/Models - Eloquent Models

- Define default attribute values on the model with `$attributes` or an accessor. Never set a
  default in the migration.
- Use soft deletes unless the project forbids them.
- Cast every attribute that isn't a plain string: JSON to array, backed enums, dates and datetimes,
  booleans, decimals.

  ```php
  protected $casts = [
      'status' => TransactionStatusEnum::class,
      'meta' => 'array',
      'settled_at' => 'datetime',
      'amount' => 'decimal:2',
  ];
  ```

## Belongs in a Model

- Relationships (`hasOne`, `hasMany`, `belongsTo`, and the rest).
- Casts.
- Query scopes: `scopeActive`, `scopeForUser`.
- Small persistence helpers and computed attributes.

## Doesn't Belong in a Model

- Domain workflows or multi-step processes. Those are services.
- Orchestration across other domains.
- Controller work: reading the request, building responses.
