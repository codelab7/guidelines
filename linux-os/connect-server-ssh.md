# Connecting to a Server over SSH

How to connect to a remote Linux server from your machine. There are two ways to log in: with a **password** or with an **SSH key**.

Use the key method. It is safer and you do not have to type a password every time.

---

## 1. What you need

Before you start, get these details from your server provider:

- **Server address** - an IP like `203.0.113.10` or a domain like `server.example.com`
- **Username** - often `root`, `ubuntu`, or `deploy`
- **Port** - `22` unless someone changed it
- **Password** or a **key file** for the first login

The examples below use `deploy@203.0.113.10`. Replace it with your own details.

---

## 2. Connect with a password

The basic command:

```bash
ssh deploy@203.0.113.10
```

If the server uses a different port, pass it with `-p`:

```bash
ssh -p 2222 deploy@203.0.113.10
```

The first time you connect, you will see a message like this:

```text
The authenticity of host '203.0.113.10' can't be established.
ED25519 key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type `yes` and press Enter. This happens only once per server. Your machine saves the server fingerprint in `~/.ssh/known_hosts` so it can warn you later if the server identity changes.

Then type your password. Nothing shows on screen while you type. That is normal.

To log out:

```bash
exit
```

---

## 3. Connect with an SSH key

This is the recommended way.

### 3.1 Create a key

Skip this if you already made a key while setting up Git. Check first:

```bash
ls ~/.ssh/id_ed25519
```

If the file does not exist, create it:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```

Press **Enter** for every question to accept the defaults.

This creates two files:

- `~/.ssh/id_ed25519` - the **private** key. Never share this or copy it to a server.
- `~/.ssh/id_ed25519.pub` - the **public** key. This is the one you put on servers.

### 3.2 Copy the public key to the server

The easy way, using the password login one last time:

```bash
ssh-copy-id deploy@203.0.113.10
```

With a custom port:

```bash
ssh-copy-id -p 2222 deploy@203.0.113.10
```

If `ssh-copy-id` is not available, do it manually:

```bash
cat ~/.ssh/id_ed25519.pub | ssh deploy@203.0.113.10 \
  "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

### 3.3 Connect

```bash
ssh deploy@203.0.113.10
```

It should log in without asking for a password.

If you have more than one key, pick the right one with `-i`:

```bash
ssh -i ~/.ssh/id_ed25519 deploy@203.0.113.10
```

---

## 4. Save servers in a config file

Typing the address, user, port, and key every time is slow. Put them in `~/.ssh/config` instead.

Open the file:

```bash
nano ~/.ssh/config
```

Add a block for each server:

```bash
Host myserver
    HostName 203.0.113.10
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60

Host staging
    HostName staging.example.com
    User ubuntu
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

Fix the file permissions:

```bash
chmod 600 ~/.ssh/config
```

Now connect with the short name:

```bash
ssh myserver
```

`ServerAliveInterval 60` sends a signal every 60 seconds so the connection does not drop when you stop typing.

---

## 5. Fix key permissions

SSH refuses to use key files that other users can read. This is the most common reason a key login fails.

On your machine:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

On the server:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

## 6. Use the SSH agent

If you set a passphrase on your key, the agent remembers it for the session so you type it only once.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Check which keys are loaded:

```bash
ssh-add -l
```

---

## 7. Turn off password login

Once key login works, turn off passwords so nobody can guess their way in.

**Warning:** if you do this before your key works, you will lock yourself out of the server. Test the key login first, and keep your current session open while you make the change.

Open the SSH server config on the **server**:

```bash
sudo nano /etc/ssh/sshd_config
```

Set these values:

```bash
PasswordAuthentication no
PubkeyAuthentication yes
PermitRootLogin no
```

Check the file for mistakes before applying it:

```bash
sudo sshd -t
```

If that prints nothing, the file is valid. Restart the service:

```bash
sudo systemctl restart ssh
```

Now open a **second terminal** and connect again. If it works, you are safe to close the first one.

---

## 8. Copy files to and from the server

Copy a file to the server:

```bash
scp report.pdf deploy@203.0.113.10:~/
```

Copy a folder:

```bash
scp -r ./build deploy@203.0.113.10:/var/www/
```

Copy a file from the server to your machine:

```bash
scp deploy@203.0.113.10:/var/log/app.log ./
```

With a custom port, note the capital `P`:

```bash
scp -P 2222 report.pdf deploy@203.0.113.10:~/
```

If you saved the server in `~/.ssh/config`, use the short name:

```bash
scp report.pdf myserver:~/
```

For large folders use `rsync`. It only sends what changed:

```bash
rsync -avz ./build/ myserver:/var/www/build/
```

---

## 9. Run a command without logging in

Useful for quick checks and scripts:

```bash
ssh myserver "df -h"
ssh myserver "sudo systemctl status nginx"
```

---

## 10. Troubleshooting

Add `-v` to any `ssh` command to see what is happening:

```bash
ssh -v myserver
```

Common errors:

| Error | Likely cause | Fix |
|-------|--------------|-----|
| `Permission denied (publickey)` | The key is not on the server, or file permissions are wrong | Re-run `ssh-copy-id`, then check step 5 |
| `Connection refused` | SSH is not running, or the port is wrong | Confirm the port, check that the server is up |
| `Connection timed out` | A firewall is blocking you, or the address is wrong | Check the IP and the firewall rules |
| `Host key verification failed` | The server was rebuilt and its identity changed | Remove the old entry: `ssh-keygen -R 203.0.113.10` |
| `Too many authentication failures` | SSH is offering too many keys before the right one | Add `IdentitiesOnly yes` to the host block in `~/.ssh/config` |

**Careful with `Host key verification failed`.** It means the server is not the one you saved before. That is normal after a rebuild, but it can also mean someone is intercepting the connection. Only clear the old entry if you know why the server changed.
