# Git

## 1️⃣ Install Git (engine room)
Most Ubuntu installs already have it, but let’s be sure.

```sql
sudo apt update
sudo apt install git -y
```

Verify:

```haskell
git --version
```

* * *
## 2️⃣ Configure Git identity (mandatory)
This name + email go into every commit.

```verilog
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Check:

```verilog
git config --global --list
```

* * *
## 3️⃣ Set better Git defaults (recommended)

```verilog
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor nano
git config --global color.ui auto
```

* * *
## 4️⃣ Generate SSH key (secure GitHub access 🔐)
### Create key

```perl
ssh-keygen -t ed25519 -C "your@email.com"
```

Just press **Enter** for all questions.
* * *
### Start SSH agent

```javascript
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

* * *
### Copy public key

```javascript
cat ~/.ssh/id_ed25519.pub
```

Copy the full output.
* * *
## 5️⃣ Add SSH key to GitHub
1. Go to **GitHub → Settings**
2. **SSH and GPG keys**
3. **New SSH key**
4. Paste the key
5. Save
* * *
### Test connection

```css
ssh -T git@github.com
```

Expected:

```erlang
Hi username! You've successfully authenticated.
```

* * *
## 6️⃣ Install GitHub CLI (`gh`) 🧠
This makes GitHub feel local.

```plain
sudo apt install gh -y
```

Verify:

```haskell
gh --version
```

* * *
## 7️⃣ Login GitHub via CLI (very important)

```plain
gh auth login
```

Choose:
*   [GitHub.com](http://GitHub.com)
*   HTTPS or SSH → **SSH**
*   Authenticate via browser → **Yes**
Once done:

```plain
gh auth status
```

* * *
## 8️⃣ Integrate Git + GitHub (real workflow)
### Clone repo

```bash
gh repo clone owner/repo
```

### Create repo from local folder

```perl
gh repo create my-project --private --source=. --push
```

### Create branch

```css
git checkout -b feature/login
```

### Commit

```sql
git add .
git commit -m "Add login UI"
```

### Push

```perl
git push -u origin feature/login
```

### Create PR (no browser needed 😎)

```sql
gh pr create
```

* * *
## 9️⃣ Add productivity aliases (GitHub-aware)
Add to `~/.zshrc`:

```verilog
# GitHub CLIalias pr="gh pr create"alias prs="gh pr list"alias prc="gh pr checkout"alias issue="gh issue create"alias issues="gh issue list"
```

Reload:

```bash
source ~/.zshrc
```