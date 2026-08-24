# src/components - Components

Everything that renders UI below the route level. A screen lives in `app/`; everything it is built
from lives here.

## Where a Component Goes

- `ui/` - library primitives and thin wrappers around them.
- `shared/` - generic project UI with no domain knowledge.
- `specific/` - domain-aware components used by more than one feature.
- `{feature}/` - anything used by a single feature. This is where most components start.

Promote a component out of its feature folder on its *second* use, not in anticipation of one.

## Inside a Feature Folder

```
components/sale/sections/    the feature's logic
components/sale/widgets/     small pieces used only by this feature
components/sale/forms/       the feature's forms, when it has more than one
```

- **Section** - holds most of the feature's logic, state, and data handling. A section may call
  other sections to break up a large flow.
- **Widget** - props in, callbacks out. Renders and handles small local state. No business rules.
- Add a subfolder only once more than one file belongs in it. A feature with two files keeps them
  flat.
- Push logic upwards into sections and data downwards as props. A widget never reaches for global
  state on its own.

## Design

- Minimum props, maximum flexibility. Expose only what the caller must control.
- Prefer composition - children, nested components, callback props - over adding another prop.
- Never pass a whole object or global state when a single field is enough.
- Never bind a reusable component to one screen's logic.

## Native UI

Build for the platform, not for the web. This is the rule most often broken when porting a web
component.

- Use a native sheet or a platform alert. Never a centered web-style modal.
- An action is a button with a real hit area. Never link-styled text.
- Use the platform date and time pickers, not a hand-built calendar.
- Use pull-to-refresh and swipe actions where the platform expects them.
- When porting from a web app, port the *logic*. Leave its web UI patterns behind.

## Changing a Component

- Update every place it is used, not just the file in front of you.
- Check all usage points before editing a form or a shared component. If a form is shared between
  create and edit, a new field goes into both flows unless the user says otherwise.
- A component full of `if (isEdit)` branches is two components. Split it and pick the right one a
  level up.
