# Setting up Git

A step-by-step guide to install Git, connect it to GitHub over SSH, and set up the GitHub CLI on Ubuntu or Debian.

---

## 1. Install Git

Most Ubuntu installs already have Git, but make sure:

```bash
sudo apt update
sudo apt install git -y
```

Verify:

```bash
git --version
```

---

## 2. Configure your Git identity

This is mandatory. The name and email go into every commit.

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Check:

```bash
git config --global --list
```

---

## 3. Set better defaults

Recommended:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor nano
git config --global color.ui auto
```

---

## 4. Generate an SSH key

Create the key:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```

Press **Enter** for every question to accept the defaults.

Start the SSH agent and add the key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Print the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the full output.

---

## 5. Add the SSH key to GitHub

1. Go to **GitHub > Settings**
2. Open **SSH and GPG keys**
3. Click **New SSH key**
4. Paste the key
5. Save

Test the connection:

```bash
ssh -T git@github.com
```

You should see:

```text
Hi username! You've successfully authenticated.
```

---

## 6. Install the GitHub CLI

The `gh` command lets you work with GitHub from the terminal.

```bash
sudo apt install gh -y
```

Verify:

```bash
gh --version
```

---

## 7. Log in to GitHub

```bash
gh auth login
```

Choose:

- GitHub.com
- HTTPS or SSH: **SSH**
- Authenticate via browser: **Yes**

When it finishes, check the status:

```bash
gh auth status
```

---

## 8. Everyday workflow

Clone a repo:

```bash
gh repo clone owner/repo
```

Create a repo from a local folder:

```bash
gh repo create my-project --private --source=. --push
```

Create a branch:

```bash
git checkout -b feature/login
```

Commit:

```bash
git add .
git commit -m "Add login UI"
```

Push:

```bash
git push -u origin feature/login
```

Create a pull request, no browser needed:

```bash
gh pr create
```

---

## 9. Add aliases

Add this block to `~/.zshrc`:

```bash
# =========================
# GitHub CLI aliases
# =========================
alias pr="gh pr create"
alias prs="gh pr list"
alias prc="gh pr checkout"
alias issue="gh issue create"
alias issues="gh issue list"
```

Reload:

```bash
source ~/.zshrc
```

---

## What you have now

- Git installed and configured with your identity
- An SSH key connected to GitHub
- The GitHub CLI, logged in
- Short aliases for pull requests and issues

Next, follow [setup-docker.md](setup-docker.md) to install Docker and Docker Compose.
