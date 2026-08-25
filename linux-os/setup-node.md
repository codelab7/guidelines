# Setting up Node.js

A step-by-step guide to install Node.js (LTS) and pnpm on Ubuntu or Debian.

LTS means Long Term Support. Use it for real projects, as it gets fixes for longer than the latest release.

---

## 1. Install Node.js LTS

Ubuntu's own Node.js package is usually old. Install from NodeSource instead:

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

This installs `node` and `npm` together.

---

## 2. Verify the install

```bash
node -v
npm -v
```

If both print versions, you are good.

---

## 3. Install pnpm

pnpm is faster than npm and saves disk space by sharing packages between projects.

Node.js ships with Corepack, which is the recommended way to install pnpm:

```bash
corepack enable
corepack prepare pnpm@latest --activate
```

Verify:

```bash
pnpm -v
```

---

## 4. Common commands

```bash
pnpm install              # install dependencies
pnpm add <package>        # add a dependency
pnpm add -D <package>     # add a dev dependency
pnpm remove <package>     # remove a dependency
pnpm dev                  # run the dev script
pnpm build                # run the build script
```

If a project has a `package-lock.json` it was set up with npm. Keep using npm for that project, or delete the lock file and run `pnpm install` once to switch. Do not use both in the same project, or the dependency versions will drift apart.

---

## What you have now

- Node.js LTS with npm
- pnpm through Corepack

Next, follow [connect-server-ssh.md](connect-server-ssh.md) when you need to deploy to a server.
