# src/schemas - Form Schemas

Zod schemas for forms. This folder is only used when the project validates forms with Zod.

## Structure

```text
schemas/
  sale-schema.ts      exports saleSchema
  contact-schema.ts   exports contactSchema
```

- One file per form or per entity, flat, named `{name}-schema.ts`. The schema is a named export: `saleSchema`.

## Rules

- Build schemas from the shared pieces in `utils/validation.utils.ts` - phone, email, money. Never redefine one of those rules inside a schema.
- Derive the form's field type from the schema instead of writing it twice: `export type SaleFillable = z.infer<typeof saleSchema>`.
- One schema serves both the create and the edit form.
- Error messages in a schema follow the project's i18n setup when it has one.

## Boundaries

- Follow the `schemas/` row in the import table in `src/CLAUDE.md`.
- Not here: a single reusable rule (phone, email, money) goes in `utils/validation.utils.ts`.

## Existing Schemas

Read this list before writing a schema - the form may already have one. When you add, rename, or remove a schema, or change its fields, update this list in the same change.

| File | Schema | Used by |
|------|--------|---------|
