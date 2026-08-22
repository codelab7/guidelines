# app/Enums - Enums

- Every enum is a PHP backed enum in `app/Enums/`. Nest by domain when it helps:
  `app/Enums/Accounting/AccountTypeEnum.php`, namespace `App\Enums\Accounting`.
- Create an enum for a value that is stored in the database, compared often, or rendered in the UI:
  status, type, segment, currency.
- Case names use PascalCase. The backing value is what the database stores.

  ```php
  enum AccountTypeEnum: string
  {
      case Asset = 'asset';
      case Liability = 'liability';
  }
  ```

- Cast the enum on the model. Never use a database `enum` column.
- Display helpers such as `label()` may live on the enum. Domain workflows may not.
