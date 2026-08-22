# Setting up zsh

## 0️⃣ Update system (always first)

```bash
sudo apt update && sudo apt upgrade -y
```

* * *
## 1️⃣ Install **mandatory base tools** 🔧
These are required for almost everything else.

```bash
sudo apt install -y \
  curl \
  wget \
  git \
  ca-certificates \
  gnupg \
  lsb-release \
  software-properties-common \
  unzip \
  zip \
  build-essential
```

#### What these give you
*   **curl / wget** → download installers & scripts
*   **git** → version control
*   **ca-certificates** → HTTPS downloads won’t fail
*   **gnupg** → verify packages
*   **lsb-release** → OS detection
*   **build-essential** → compile native modules
*   **zip/unzip** → archives
* * *
#### 2️⃣ Verify installations (quick check)

```haskell
curl --version
git --version
wget --version
```

If these print versions, you’re good ✅
* * *
## 3️⃣ Install Zsh (shell)

```plain
sudo apt install zsh -y
```

Verify:

```haskell
zsh --version
```

Make it default:

```bash
chsh -s $(which zsh)
```

➡️ Log out & log back in.
* * *
### 4️⃣ Prevent Zsh welcome screen (important)

```plain
touch ~/.zshrc
```

This avoids the new-user prompt you saw earlier.
* * *
## 5️⃣ Install Oh My Zsh 🚀
Now that `curl` exists:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Terminal will restart automatically.
* * *
#### 6️⃣ Recommended fonts (avoid broken theme symbols)

```plain
sudo apt install fonts-powerline -y
```

Then:
**Terminal → Preferences → Text → Font**
Choose a Powerline font.
### 1️⃣ Powerlevel10k (the best Zsh prompt)
Install theme

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k
```

Enable it

```plain
nano ~/.zshrc
```

Change:

```bash
ZSH_THEME="robbyrussell"
```

To:

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

Apply:

```bash
source ~/.zshrc
```

👉 You’ll see a **configuration wizard**.
Recommended answers for devs:
*   Prompt style: **Lean**
*   Icons: **Yes**
*   Show time: **No**
*   Git status: **Yes**
*   Transient prompt: **Yes**
If icons look broken:

```plain
sudo apt install fonts-powerline -y
```

Then change terminal font to a Powerline font.
Re-run wizard anytime:

```plain
p10k configure
```

* * *
## 7️⃣ (Optional) but highly recommended dev tools 🧠
Install these when ready:

```bash
sudo apt install -y \
  htop \
  tree \
  neovim \
  net-tools \
  jq \
  ripgrep
```

### What you have now 🧰
✔ Secure downloads
✔ Git ready
✔ Zsh + Oh My Zsh
✔ Fonts fixed
✔ Developer-friendly CLI
Your terminal is no longer bare metal. It’s a tuned engine ⚙️
After Installing zsh

```bash
nano ~/.zshrc
```

& Add **this entire block at the bottom**:

```bash
# =========================
# Laravel aliases
# =========================
alias a="php artisan"
alias serve="php artisan serve"
alias migrate="php artisan migrate"
alias fresh="php artisan migrate:fresh --seed"
alias seed="php artisan db:seed"
alias tinker="php artisan tinker"
alias route:list="php artisan route:list"
alias cache:clear="php artisan optimize:clear"

# =========================
# Docker aliases
# =========================
alias d="docker"
alias dc="docker compose"
alias dcu="docker compose up -d"
alias dcd="docker compose down"
alias dcb="docker compose build"
alias dcl="docker compose logs -f"
alias dps="docker ps"
alias dex="docker exec -it"
```

### Zsh (Oh my zash) plugins
*   `git` — aliases and completions for git
*   `z` — jump to frequently used directories
*   `autosuggestions` — suggests commands as you type (needs separate install)
*   `syntax-highlighting` — colorizes valid/invalid commands (needs separate install)

### Autosuggestions + syntax highlighting

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Enable plugins:

```plain
plugins=(
  git
  z
  docker
  docker-compose
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```

Reload:

```bash
source ~/.zshrc
```