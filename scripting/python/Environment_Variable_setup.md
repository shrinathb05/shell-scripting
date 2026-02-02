Storing sensitive data directly in your code is a major security risk, especially if you ever share your script or upload it to a repository like GitHub. Using **Environment Variables** is the industry standard for keeping "secrets" safe and separate from your logic.

---

### 1. How to Create Environment Variables in Linux

On Linux, you can set variables at different levels depending on how long you need them to last.

#### Temporary (Current Session)

If you just want to test a script, you can export the variable in your terminal. It will disappear once you close the window.

```bash
export DB_PASSWORD="supersecretpassword123"
export API_KEY="hx-9988776655"

```

#### Permanent (User Level)

To make these variables stay after a reboot, add them to your shell configuration file (usually `.bashrc` or `.zshrc`).

1. Open the file: `nano ~/.bashrc`
2. Add your exports at the bottom:
```bash
export DB_PASSWORD="supersecretpassword123"
export API_KEY="hx-9988776655"

```


3. Save and reload: `source ~/.bashrc`

#### Permanent (System Level)

For automation scripts run by the system (like Cron), you often put them in `/etc/environment`.

```bash
sudo nano /etc/environment
# Add lines without 'export'
DB_PASSWORD="supersecretpassword123"

```

---

### 2. How to Access Them in Python

Python’s `os` library has a specific method called `os.getenv()` to grab these values.

```python
import os

# 1. Fetching the variable
db_pass = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

# 2. Handling missing variables (Production Safety)
if not db_pass:
    print("Error: DB_PASSWORD environment variable is not set!")
    exit(1)

print(f"Connecting to database with password length: {len(db_pass)}")

```

---

### 3. The "Production" Choice: `.env` Files

Manually setting variables on every server is tedious. In production automation, we use a `.env` file located in the same folder as the script.

**Step 1: Create a `.env` file**

```text
# .env
DB_PASSWORD=my_secure_pass
SLACK_WEBHOOK=https://hooks.slack.com/...

```

**Step 2: Use the `python-dotenv` library**
This is the most popular way to manage secrets.

```bash
pip install python-dotenv

```

**Step 3: The Python Script**

```python
import os
from dotenv import load_dotenv

# This looks for a file named .env and loads the variables
load_dotenv()

db_password = os.getenv("DB_PASSWORD")
webhook = os.getenv("SLACK_WEBHOOK")

print(f"Slack Webhook is loaded: {bool(webhook)}")

```

---

### 4. Why use `os.getenv()` instead of `os.environ[]`?

| Method | Behavior if missing | Best Use Case |
| --- | --- | --- |
| `os.environ["KEY"]` | Raises a **KeyError** (Crashes) | When the variable is 100% required to run. |
| `os.getenv("KEY")` | Returns **None** | When you want to handle the error gracefully. |
| `os.getenv("KEY", "default")` | Returns **"default"** | For optional settings (like a log level). |

---

### Security Checklist:

* **`.gitignore`**: If you use Git, **never** commit your `.env` file. Add `.env` to your `.gitignore` file immediately.
* **Permissions**: Set strict permissions on your `.env` file or your bash config: `chmod 600 .env`. This ensures only you (and the script) can read it.

Would you like me to show you how to set these variables specifically for a **systemd service** or a **Cron job**, since they don't always load your `.bashrc` automatically?


This is a crucial detail because **Cron** and **Systemd** are "non-interactive" shells. They do not load your `.bashrc` or `.profile` files, which means your `export` commands will be ignored, and your script will fail to find its secrets.

Here is how you handle environment variables for those specific production scenarios.

---

### 1. Variables for Cron Jobs

Cron runs in a very minimal environment. There are two ways to provide variables to a Cron job:

#### Option A: Define them inside the Crontab (Simplest)

You can declare variables at the very top of your crontab file.

1. Run `crontab -e`.
2. Add your variables at the top, before the schedule:
```bash
DB_PASSWORD=supersecret123
API_KEY=hx-998877

# Run the script every midnight
0 0 * * * /usr/bin/python3 /home/user/script.py

```



#### Option B: Load them in the command line

You can also pass them directly in the command string:

```bash
0 0 * * * export DB_PASSWORD=secret; /usr/bin/python3 /home/user/script.py

```

---

### 2. Variables for Systemd Services

If you are running your Python script as a background service (like a custom monitoring daemon), Systemd provides a clean way to manage environment variables using a dedicated file.

**Step 1: Create an Environment File**
Create a file at `/etc/default/my_service` (or any path you prefer):

```bash
# /etc/default/my_service
DB_PASSWORD=supersecret123
API_KEY=hx-998877

```

Set permissions so only root can read it: `sudo chmod 600 /etc/default/my_service`.

**Step 2: Update your Systemd Unit File**
In your `.service` file (usually in `/etc/systemd/system/`), use the `EnvironmentFile` directive:

```ini
[Unit]
Description=My Python Automation Service

[Service]
ExecStart=/usr/bin/python3 /home/user/script.py
# Load the variables from your file
EnvironmentFile=/etc/default/my_service
User=myuser

[Install]
WantedBy=multi-user.target

```

---

### 3. The "Python-Native" Approach (Highly Recommended)

Regardless of whether you use Cron, Systemd, or manual execution, the most **portable** way is to use a `.env` file and the `python-dotenv` library. This makes your script "environment-aware" without needing to mess with OS-level configs.

```python
import os
from pathlib import Path
from dotenv import load_dotenv

# Automatically finds .env in the same folder as the script
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

def connect_to_db():
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("CRITICAL: DB_PASSWORD is not set!")
    # Proceed with logic...

```

### Summary Table: Where to store secrets?

| Scenario | Best Method | Why? |
| --- | --- | --- |
| **Development** | `.env` file | Easy to change and keeps code clean. |
| **Simple Cron** | Top of `crontab -e` | Quick and doesn't require extra files. |
| **Production Service** | `EnvironmentFile` in Systemd | Secure and standard Linux practice. |
| **CI/CD (GitHub Actions)** | Secrets Vault | Encrypted and never touches your server files. |

**Pro-Tip:** If you ever accidentally commit a secret to GitHub, changing the password isn't enough—you must also "rotate" (generate a new) API key or password immediately, as the old one will remain in the Git history!

Would you like to try writing a small script that tests if it can "see" these variables across different Linux environments?
