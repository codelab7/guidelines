# src/pages - Pages

One folder per feature, holding one page file per route. A page is layout and core structure
only. Everything it is built from lives in `components/features/{feature}/`.

```
pages/sale/index.tsx          the page the router renders
```

## The Page

- Reads the route params, picks the layout, and places the feature's sections.

## Not Allowed Here

- No state, no data fetching, no business logic, and no forms. Those belong in the sections.
- No sections, widgets, helpers, or hooks inside `pages/{feature}/`. They live in
  `components/features/{feature}/`.

## Example

```tsx
export default function SalePage() {
    const { saleId } = useParams();

    return (
        <UserLayout>
            <SaleSummary saleId={saleId} />
            <SaleLines saleId={saleId} />
        </UserLayout>
    );
}
```
