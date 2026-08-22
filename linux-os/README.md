# Linux OS Setup

Step-by-step guides for setting up a Linux development machine. Written for Ubuntu and Debian-based systems (they use `apt`).

## Guides

| Guide | What it covers |
|-------|----------------|
| [setup-zsh.md](setup-zsh.md) | Base tools (curl, wget, git, build-essential), Zsh, Oh My Zsh, the Powerlevel10k theme, plugins, and shell aliases. |
| [setup-git.md](setup-git.md) | Git install and identity, recommended defaults, SSH keys for GitHub, and the GitHub CLI (`gh`). |

## Order

Follow **setup-zsh.md** first. It installs the base tools that everything else needs, including `curl` and `git`.

Then follow **setup-git.md** to configure your Git identity and connect to GitHub.

## Before You Start

- You need `sudo` access.
- Some steps ask you to log out and log back in. Do this when the guide says so, or the change will not apply.
- Run the update command first: `sudo apt update && sudo apt upgrade -y`.
