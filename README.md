# Guidelines

A central repository for our development guidelines and setup guides. It has two parts: coding guidelines for AI code assistants, and setup guides for a Linux development machine.

## AI Coding Guidelines

Markdown specs in [`AI/code-guideline/`](AI/code-guideline/) that define how an AI coding agent should behave and how it should structure code in our projects.

| Document | Purpose |
|----------|---------|
| [GENERAL_GUIDELINE.md](AI/code-guideline/GENERAL_GUIDELINE.md) | Global agent behaviour: communication style, planning, handling ambiguity, error correction. |
| [PHP_LARAVEL_GUIDELINE.md](AI/code-guideline/PHP_LARAVEL_GUIDELINE.md) | Laravel + PHP: layer responsibilities (controllers, requests, services, models), plus an index of which `laravel/` folder file owns each rule. |
| [REACT_GUIDELINE.md](AI/code-guideline/REACT_GUIDELINE.md) | React + TypeScript: the page/section/widget component roles, plus an index of which folder file owns each rule. |

The general guideline is the base spec. The framework guidelines build on it, so an agent follows the general one plus whichever framework guideline matches the code it is editing.

The same folder holds starter folder structures to copy into a new project, one per stack: [`laravel/`](AI/code-guideline/laravel/), [`react/`](AI/code-guideline/react/), and [`laravel-react/`](AI/code-guideline/laravel-react/). Each folder in them carries a `CLAUDE.md` with the rules for that folder, so an agent picks up the right rules from where it is working. All three trees are filled in, and each one's `README.md` ends with a checklist of rules still to settle. See [`AI/code-guideline/README.md`](AI/code-guideline/README.md) for how they fit together.

To use them, reference these documents from your AI assistant's instruction file in the consumer project (for example a `CLAUDE.md`, `.cursorrules`, or `AGENTS.md` that points to or includes them). The agent then follows the general guideline for behaviour and the framework guideline matching the code it is working on.

See [`AI/README.md`](AI/README.md) for how to set up the Claude CLI skills, agents, and commands in [`AI/.claude/`](AI/.claude/).

## Code Decisions

Choices we have already made, so nobody has to re-argue them per project, in [`code-decisions/`](code-decisions/):

| Document | Purpose |
|----------|---------|
| [preferred-libraries.md](code-decisions/preferred-libraries.md) | Which library to reach for by default, per stack. |

## Linux Setup

Step-by-step guides for setting up a Linux development machine, in [`linux-os/`](linux-os/):

| Guide | What it covers |
|-------|----------------|
| [setup-zsh.md](linux-os/setup-zsh.md) | Base tools, Zsh, Oh My Zsh, Powerlevel10k, plugins, and aliases. |
| [setup-git.md](linux-os/setup-git.md) | Git identity, SSH keys for GitHub, and the GitHub CLI. |
| [setup-docker.md](linux-os/setup-docker.md) | Docker engine and Docker Compose, plus running Docker without `sudo`. |
| [setup-node.md](linux-os/setup-node.md) | Node.js LTS and pnpm. |
| [connect-server-ssh.md](linux-os/connect-server-ssh.md) | Connecting to a remote server by password or SSH key, plus file transfer. |

## Adding a Guideline

- Put new AI coding guidelines in `AI/code-guideline/`, named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Cross-cutting agent behaviour belongs in the general guideline. Stack-specific rules get their own document.
- Follow the existing format: an "(AGENT Spec)" title, numbered sections separated by `---`, and an "Agent Behaviour Summary" section at the end of framework docs.
