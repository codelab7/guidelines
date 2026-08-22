# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A documentation-only repository holding two things: coding guidelines for AI code assistants, and setup guides for Linux development machines. There is no application code and no build, lint, or test commands — the markdown files are the product.

Important: the guideline files are consumed by AI assistants working in *other* projects. Their directives (e.g., "ask clarifying questions before coding", "use Laravel Boost") govern agents in those consumer projects — they are not instructions for working in this repo. Work here means editing document content for clarity, consistency, and correctness.

## Structure

- `AI/code-guideline/` — the AI agent specs plus starter folder structures. `GENERAL_GUIDELINE.md` is the global agent-behaviour spec (communication style, planning, ambiguity handling, error correction). `PHP_LARAVEL_GUIDELINE.md` and `REACT_GUIDELINE.md` are framework-specific specs that explicitly build on it. Alongside them, `laravel/`, `react/`, and `laravel-react/` are empty folder trees showing where code belongs in each stack; every folder in them holds a blank `CLAUDE.md` placeholder for folder-scoped rules. Keep a scaffold's folders and the spec that documents them in sync — if one gains a folder, the other needs updating.
- `AI/.claude/` — Claude CLI skills, agents, commands, and output styles meant to be copied into a user's `~/.claude`. `AI/README.md` explains that setup for humans.
- `linux-os/` — machine setup guides for Ubuntu/Debian: one `setup-<tool>.md` per tool (Zsh, Git, Docker, Node), plus `connect-server-ssh.md`. Keep one tool per guide.

New guidelines follow that layering: cross-cutting agent behaviour goes in the general spec; stack-specific rules go in a new `*_GUIDELINE.md`.

## Document Conventions

- Guideline docs live in `AI/code-guideline/`, named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Guideline titles carry the "(AGENT Spec)" suffix.
- Content is organized as numbered sections separated by `---` horizontal rules.
- Framework-specific guidelines end with an "Agent Behaviour Summary" section that condenses the rules.
- Each top-level folder, and each starter structure, has a `README.md` that indexes its contents. Update it when adding or renaming a file, and update the root `README.md` too — both list the guides.
- The `linux-os/` guides follow their own format: plain numbered `## 1.` sections separated by `---`, copy-paste `bash` code fences (`text` for command output), simple English written for a non-native speaker, and a short "What you have now" summary ending in a link to the next guide.
- Use plain ASCII in all documents — no smart quotes, em-dashes, emoji step numbers, or raw HTML. These files were converted from HTML once and carried those artifacts; do not reintroduce them.
