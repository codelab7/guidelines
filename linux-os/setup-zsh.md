# Setting up Zsh

A step-by-step guide to set up Zsh with Oh My Zsh on Ubuntu or Debian.

---

## 1. Update the system

Always do this first.

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Install the base tools

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

What these give you:

- **curl / wget** - download installers and scripts
- **git** - version control
- **ca-certificates** - HTTPS downloads will not fail
- **gnupg** - verify packages
- **lsb-release** - OS detection
- **build-essential** - compile native modules
- **zip / unzip** - archives

---

## 3. Verify the install

```bash
curl --version
git --version
wget --version
```

If these print versions, you are good.

---

## 4. Install Zsh

```bash
sudo apt install zsh -y
```

Verify:

```bash
zsh --version
```

Make it your default shell:

```bash
chsh -s $(which zsh)
```

Now log out and log back in.

---

## 5. Create the Zsh config file

```bash
touch ~/.zshrc
```

This stops the new-user setup prompt from showing.

---

## 6. Install Oh My Zsh

`curl` is already installed, so run:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

The terminal restarts automatically.

---

## 7. Install Powerline fonts

These stop theme symbols from showing as broken boxes.

```bash
sudo apt install fonts-powerline -y
```

Then open **Terminal > Preferences > Text > Font** and choose a Powerline font.

---

## 8. Install the Powerlevel10k theme

Powerlevel10k is the recommended Zsh prompt.

Install it:

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k
```

Open the config file:

```bash
nano ~/.zshrc
```

Change this line:

```bash
ZSH_THEME="robbyrussell"
```

To this:

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

Apply the change:

```bash
source ~/.zshrc
```

A configuration wizard opens. Recommended answers for developers:

- Prompt style: **Lean**
- Icons: **Yes**
- Show time: **No**
- Git status: **Yes**
- Transient prompt: **Yes**

You can run the wizard again at any time:

```bash
p10k configure
```

---

## 9. Install plugins

Install autosuggestions and syntax highlighting:

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Then open `~/.zshrc` and set the plugin list:

```bash
plugins=(
  git
  z
  docker
  docker-compose
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```

What each plugin does:

- **git** - aliases and completions for git
- **z** - jump to folders you use often
- **docker / docker-compose** - completions for Docker commands
- **zsh-autosuggestions** - suggests commands as you type
- **zsh-syntax-highlighting** - colours valid and invalid commands

Reload:

```bash
source ~/.zshrc
```

---

## 10. Add aliases

Open the config file:

```bash
nano ~/.zshrc
```

Add this block at the bottom:

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

Reload:

```bash
source ~/.zshrc
```

---

## 11. Optional developer tools

Install these when you are ready:

```bash
sudo apt install -y \
  htop \
  tree \
  neovim \
  net-tools \
  jq \
  ripgrep
```

---

## What you have now

- Secure downloads
- Git ready
- Zsh with Oh My Zsh
- Working fonts and prompt
- A developer-friendly CLI

Next, follow [setup-git.md](setup-git.md) to configure Git and GitHub.
