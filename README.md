# Guidelines

A central repository for our development guidelines and setup guides. It has two parts: coding guidelines for AI code assistants, and setup guides for a Linux development machine.

## AI Coding Guidelines

Markdown specs in [`AI/code-guideline/`](AI/code-guideline/) that define how an AI coding agent should behave and how it should structure code in our projects.

| Document | Purpose |
|----------|---------|
| [GENERAL_GUIDELINE.md](AI/code-guideline/GENERAL_GUIDELINE.md) | Global agent behaviour: communication style, planning, handling ambiguity, error correction. |
| [PHP_LARAVEL_GUIDELINE.md](AI/code-guideline/PHP_LARAVEL_GUIDELINE.md) | Laravel + PHP rules: layer responsibilities (controllers, requests, services, models), enums, migrations. |
| [REACT_GUIDELINE.md](AI/code-guideline/REACT_GUIDELINE.md) | React + TypeScript rules: directory layout under `resources/js`, components, forms, Inertia integration. |

The general guideline is the base spec. The Laravel and React guidelines build on it and together cover one stack: a Laravel backend with Inertia and React.

To use them, reference these documents from your AI assistant's instruction file in the consumer project (for example a `CLAUDE.md`, `.cursorrules`, or `AGENTS.md` that points to or includes them). The agent then follows the general guideline for behaviour and the framework guideline matching the code it is working on.

See [`AI/README.md`](AI/README.md) for how to set up the Claude CLI skills, agents, and commands in [`AI/.claude/`](AI/.claude/).

## Linux Setup

Step-by-step guides for setting up a Linux development machine, in [`linux-os/`](linux-os/):

| Guide | What it covers |
|-------|----------------|
| [setup-zsh.md](linux-os/setup-zsh.md) | Base tools, Zsh, Oh My Zsh, Powerlevel10k, plugins, and aliases. |
| [setup-git.md](linux-os/setup-git.md) | Git identity, SSH keys for GitHub, and the GitHub CLI. |

## Adding a Guideline

- Put new AI coding guidelines in `AI/code-guideline/`, named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Cross-cutting agent behaviour belongs in the general guideline. Stack-specific rules get their own document.
- Follow the existing format: an "(AGENT Spec)" title, numbered sections separated by `---`, and an "Agent Behaviour Summary" section at the end of framework docs.
