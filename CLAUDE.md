# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A documentation-only repository holding two things: coding guidelines for AI code assistants, and setup guides for Linux development machines. There is no application code and no build, lint, or test commands — the markdown files are the product.

Important: the guideline files are consumed by AI assistants working in *other* projects. Their directives (e.g., "ask clarifying questions before coding", "use Laravel Boost") govern agents in those consumer projects — they are not instructions for working in this repo. Work here means editing document content for clarity, consistency, and correctness.

## Structure

- `AI/code-guideline/` — the AI agent specs. `GENERAL_GUIDELINE.md` is the global agent-behaviour spec (communication style, planning, ambiguity handling, error correction). `PHP_LARAVEL_GUIDELINE.md` and `REACT_GUIDELINE.md` are framework-specific specs that explicitly build on it; together they describe the two halves of one assumed stack — a Laravel backend with Inertia and React under `resources/js`.
- `AI/.claude/` — Claude CLI skills, agents, commands, and output styles meant to be copied into a user's `~/.claude`. `AI/README.md` explains that setup for humans.
- `linux-os/` — machine setup guides (`setup-zsh.md`, `setup-git.md`) for Ubuntu/Debian.

New guidelines follow that layering: cross-cutting agent behaviour goes in the general spec; stack-specific rules go in a new `*_GUIDELINE.md`.

## Document Conventions

- Guideline docs live in `AI/code-guideline/`, named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Guideline titles carry the "(AGENT Spec)" suffix.
- Content is organized as numbered sections separated by `---` horizontal rules.
- Framework-specific guidelines end with an "Agent Behaviour Summary" section that condenses the rules.
- Each top-level folder has a `README.md` that indexes its contents.
- The `linux-os/` guides use a different, informal style (emoji step numbers, copy-paste command blocks). Keep that style when editing them.
