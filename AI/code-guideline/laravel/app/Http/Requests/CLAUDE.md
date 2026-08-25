# app/Http/Requests - Form Requests

- One form request per intent: `StoreContactRequest`, `UpdateContactRequest`. Don't share one class
  between store and update.
- A form request holds three things: validation rules, validation messages, and a simple
  `authorize()` check.
- Write rules in array notation so a custom rule class drops in cleanly:

  ```php
  public function rules(): array
  {
      return [
          'email' => ['required', 'email'],
      ];
  }
  ```

- Name custom validation rules in snake_case: `organisation_type`.
- No persistence, no domain decisions, no calls into services.
