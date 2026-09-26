# src/components/shared - Shared Components

- Any component reused by two or more features: `delete-confirmation.tsx`, `phone-input.tsx`,
  `team-members-list.tsx`, `notification-toast.tsx`.
- Built from `ui/` primitives.
- May use domain types from `types/`.
- Data comes in through props, callbacks go out. No data fetching here.
