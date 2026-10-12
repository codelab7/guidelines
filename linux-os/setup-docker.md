# Setting up Docker

A step-by-step guide to install Docker and Docker Compose on Ubuntu or Debian, using Docker's official repository.

---

## 1. Remove old packages

Older Docker packages from the Ubuntu repository conflict with the official ones. Remove them first.

```bash
sudo apt remove -y docker docker-engine docker.io containerd runc
```

It is fine if this says some packages are not installed.

---

## 2. Add Docker's official repository

Install the tools needed to add the repository:

```bash
sudo apt install -y ca-certificates curl gnupg
```

Add Docker's signing key:

```bash
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Add the repository:

```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" \
| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

If you are on an Ubuntu-based system like Linux Mint or Pop!_OS, `lsb_release -cs` returns the wrong name and the install will fail. Use the Ubuntu codename it is built on instead:

```bash
. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}"
```

---

## 3. Install Docker

```bash
sudo apt update
sudo apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

What these give you:

- **docker-ce** - the Docker engine
- **docker-ce-cli** - the `docker` command
- **containerd.io** - the container runtime
- **docker-buildx-plugin** - modern image builds
- **docker-compose-plugin** - the `docker compose` command

---

## 4. Run Docker without sudo

By default every Docker command needs `sudo`. Add yourself to the `docker` group to avoid this:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

`newgrp docker` applies the group to your current terminal. Log out and log back in so it applies everywhere.

**Note:** members of the `docker` group can get full root access on the machine. Only add users you trust as administrators.

---

## 5. Verify the install

```bash
docker version
docker compose version
```

Run a test container:

```bash
docker run hello-world
```

If it prints a welcome message, Docker is working.

---

## 6. Start Docker on boot

On most installs this is already enabled. To be sure:

```bash
sudo systemctl enable --now docker
```

Check that it is running:

```bash
sudo systemctl status docker
```

---

## 7. Common commands

Containers:

```bash
docker ps                 # running containers
docker ps -a              # all containers
docker logs -f <name>     # follow the logs
docker exec -it <name> sh # open a shell inside a container
docker stop <name>
docker rm <name>
```

Compose, run from the folder holding `compose.yaml`:

```bash
docker compose up -d      # start in the background
docker compose down       # stop and remove
docker compose build      # rebuild images
docker compose logs -f    # follow the logs
docker compose ps         # what is running
```

Clean up disk space. Docker keeps old images and volumes and they add up:

```bash
docker system df          # see what is using space
docker system prune       # remove stopped containers and unused images
```

`docker system prune -a --volumes` also deletes unused volumes. That removes database data that is not attached to a running container, so check `docker system df` first.

Short aliases for these commands are in [setup-zsh.md](setup-zsh.md).

---

## What you have now

- Docker engine and CLI from the official repository
- Docker Compose as a built-in `docker compose` command
- Docker running without `sudo`
- Docker starting automatically on boot

Next, follow [setup-node.md](setup-node.md) to install Node.js and pnpm.
