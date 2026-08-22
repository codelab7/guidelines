# Guidelines

A central repository of coding guidelines for AI code assistants (Claude Code, GitHub Copilot, Cursor, etc.). The markdown specs in `AI/docs/` define how an AI coding agent should behave and how it should structure code in our projects.

## Contents

| Document | Purpose |
|----------|---------|
| [AI/docs/GENERAL_GUIDELINE.md](AI/docs/GENERAL_GUIDELINE.md) | Global agent behaviour: communication style, planning, handling ambiguity, error correction. |
| [AI/docs/PHP_LARAVEL_GUIDELINE.md](AI/docs/PHP_LARAVEL_GUIDELINE.md) | Laravel + PHP implementation rules: layer responsibilities (controllers, requests, services, models), enums, migrations. |
| [AI/docs/REACT_GUIDELINE.md](AI/docs/REACT_GUIDELINE.md) | React + TypeScript implementation rules: directory layout under `resources/js`, components, forms, Inertia integration. |

The general guideline is the base spec; the Laravel and React guidelines build on it and together cover one stack: a Laravel backend with Inertia and React.

## Usage

Reference these documents from your AI assistant's instruction file in the consumer project (for example, a `CLAUDE.md`, `.cursorrules`, or `AGENTS.md` that points to or includes them). The agent then follows the general guideline for behaviour and the framework guideline matching the code it is working on.

## Adding a Guideline

- Put new documents in `AI/docs/`, named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Cross-cutting agent behaviour belongs in the general guideline; stack-specific rules get their own document.
- Follow the existing format: an "(AGENT Spec)" title, numbered sections separated by `---`, and an "Agent Behaviour Summary" section at the end of framework docs.
