# routes/ - Route Files

- URLs are kebab-case and use plural resource names: `/error-occurrences`, `/open-source`.
- Route names are camelCase: `->name('openSource')`, `->name('errorOccurrences.index')`.
- Route parameters are camelCase: `{userId}`, `{errorOccurrence}`.
- Point a route at a controller with tuple notation:

  ```php
  Route::get('/error-occurrences', [ErrorOccurrencesController::class, 'index'])
      ->name('errorOccurrences.index');
  ```

- Keep nesting shallow. Prefer `/error-occurrences/1` and `/errors/1/occurrences` over anything
  deeper.
- No closures in route files. Every route resolves to a controller method.
- No logic in a route file beyond grouping by prefix, middleware, or name.
