# Code Guidelines

Coding guidelines for AI code assistants, plus ready-to-copy `CLAUDE.md` templates for the stacks we use.

## Guideline Specs

The full rules. These are written for AI assistants to follow, not as a tutorial.

| Document | Purpose |
|----------|---------|
| [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md) | Global agent behaviour: communication style, planning, handling ambiguity, error correction. |
| [PHP_LARAVEL_GUIDELINE.md](PHP_LARAVEL_GUIDELINE.md) | Laravel + PHP: the layer responsibilities, plus an index of which `laravel/` folder file owns each rule. |
| [REACT_GUIDELINE.md](REACT_GUIDELINE.md) | React + TypeScript: the component roles, plus an index of which `react/` and `laravel-react/` folder file owns each rule. |
| [REACT_NATIVE_GUIDELINE.md](REACT_NATIVE_GUIDELINE.md) | React Native on Expo: the screen/section/widget roles, what mobile adds, plus an index of which `react-native/` folder file owns each rule. |

The general guideline is the base spec. The framework guidelines build on it, so an agent always follows the general one plus the framework one matching the code it is editing.

## Project Templates

Folder trees of `CLAUDE.md` files to copy into a new project. Each stack has its own.

| Template | Use it for |
|----------|------------|
| [laravel/](laravel/) | A Laravel API or server-rendered app |
| [react/](react/) | A standalone React app (Vite, CRA, or similar) |
| [laravel-react/](laravel-react/) | Laravel with Inertia and React in one project |
| [react-native/](react-native/) | A React Native app on Expo with `expo-router` |

Each one has its own `README.md` describing what each file covers.

## How the CLAUDE.md Files Work

Claude Code reads the `CLAUDE.md` in a folder when it works on files inside that folder. That lets rules live next to the code they apply to:

- The **root** `CLAUDE.md` holds project-wide rules: communication style, planning, how to handle ambiguity.
- A **folder** `CLAUDE.md` holds rules for that folder only, for example how to write a service.

A folder file should not repeat the root file. Write only what is specific to that folder, and let the root file and the guideline specs cover the rest.

To pull a shared document into a file, use an import line instead of copying the text:

```text
@docs/PROJECT_GUIDELINES.md
```

## Status

All four templates are complete: every folder file is written, and the three framework specs
(`PHP_LARAVEL_GUIDELINE.md`, `REACT_GUIDELINE.md`, `REACT_NATIVE_GUIDELINE.md`) are indexes
pointing at them.

Open questions are tracked as a checklist at the bottom of each template's `README.md`:
[laravel/](laravel/README.md), [react/](react/README.md),
[laravel-react/](laravel-react/README.md), and [react-native/](react-native/README.md).
