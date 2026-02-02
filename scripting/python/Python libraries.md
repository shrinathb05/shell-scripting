To help you structure your automation projects, here is the breakdown of common Linux tasks mapped to the specific Python libraries you should use.

### 1. File and Directory Management

Use these when you need to organize data, move logs, or create backup structures.

* **Manipulating file paths?** Use `pathlib` (modern/clean) or `os.path`.
* **Copying or moving files/folders?** Use `shutil`.
* **Searching for files with patterns (e.g., `*.log`)?** Use `glob`.
* **Checking if a file/folder exists?** Use `os.path.exists` or `pathlib.Path.exists`.

### 2. System and Resource Monitoring

Use these to keep an eye on the health of your Linux hardware and OS.

* **Checking basic disk space?** Use `shutil.disk_usage`.
* **Detailed CPU, RAM, and Process stats?** Use `psutil`.
* **Reading system environment variables?** Use `os.environ`.
* **Checking system uptime or load averages?** Use `os.getloadavg`.

### 3. Executing Commands and Scripts

Use these when you need Python to "type" commands into the Linux terminal for you.

* **Running a simple shell command?** Use `subprocess.getoutput`.
* **Running a command and checking if it failed?** Use `subprocess.run` or `subprocess.getstatusoutput`.
* **Running long-running background tasks?** Use `subprocess.Popen`.
* **Handling complex piping (`ls | grep`)?** Use `subprocess` with `shell=True`.

### 4. Remote Server Management

Use these when your script needs to "jump" from one server to another via SSH.

* **Executing commands on a remote server?** Use `paramiko` or `fabric`.
* **Transferring files between servers (SFTP)?** Use `paramiko`.
* **Automating configuration across many servers?** Use `ansible-runner`.

### 5. Data and Configuration

Use these to handle the "brains" of your script—settings and log data.

* **Reading/Writing `.json` config files?** Use `json`.
* **Reading/Writing `.yaml` or `.yml` files?** Use `PyYAML`.
* **Parsing `.csv` log reports?** Use `csv` or `pandas`.
* **Recording script events/errors to a file?** Use `logging`.

---

### 6. Networking and Connectivity

Use these to check if your services are reachable over the network.

* **Testing if a port is open (e.g., Port 80)?** Use `socket`.
* **Pinging an IP address?** Use `subprocess` (calling the `ping` command).
* **Sending a request to a URL/API?** Use `requests`.
* **Sending an email alert?** Use `smtplib`.
--------------------------------------------------------------------------------------------------------------------------

To give you the most practical "production-grade" experience, I have separated these into **four distinct scripts**. Each script focuses on a specific pillar of Linux automation using the libraries we discussed.

---

### 1. The Resource & Health Monitor

**Libraries used:** `shutil`, `psutil`, `logging`, `sys`
This script monitors the physical health of the server and exits with specific codes if thresholds are met.

```python
#!/usr/bin/python3
import shutil
import psutil
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def monitor_system():
    # SHUTIL: Check Disk Usage
    total, used, free = shutil.disk_usage("/")
    disk_percent = (used / total) * 100
    
    # PSUTIL: Check CPU and RAM
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    logging.info(f"Stats -> CPU: {cpu_usage}% | RAM: {ram_usage}% | Disk: {disk_percent:.1f}%")

    if disk_percent > 90 or ram_usage > 95:
        logging.critical("System resources exhausted!")
        sys.exit(1) # Production scripts use exit codes for monitoring tools

if __name__ == "__main__":
    monitor_system()

```

---

### 2. The Remote Fleet Manager

**Libraries used:** `paramiko` (or `fabric`), `getpass`
Use this to run commands across multiple servers without logging into each one manually.

```python
#!/usr/bin/python3
import paramiko

servers = ["192.168.1.10", "192.168.1.11"]
user = "admin"
command = "uptime"

def manage_remote():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for ip in servers:
        print(f"--- Connecting to {ip} ---")
        try:
            # In production, use SSH keys instead of passwords
            ssh.connect(ip, username=user, key_filename='/home/user/.ssh/id_rsa')
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
        except Exception as e:
            print(f"Failed to connect to {ip}: {e}")
        finally:
            ssh.close()

if __name__ == "__main__":
    manage_remote()

```

---

### 3. The Log & File Janitor

**Libraries used:** `os`, `pathlib`, `tarfile`, `datetime`
This handles the "cleanup" and "archiving" of production logs.

```python
#!/usr/bin/python3
import os
import tarfile
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("/var/log/myapp")
ARCHIVE_DIR = Path("/backups/logs")

def archive_logs():
    # PATHLIB: Filter files
    log_files = list(LOG_DIR.glob("*.log"))
    
    if not log_files:
        return

    # DATETIME: Unique archive name
    timestamp = datetime.now().strftime("%Y%m%d")
    archive_name = ARCHIVE_DIR / f"logs_archive_{timestamp}.tar.gz"

    # TARFILE: Compress files
    with tarfile.open(archive_name, "w:gz") as tar:
        for log in log_files:
            tar.add(log, arcname=log.name)
            # OS: Remove file after archiving
            os.remove(log)
            
    print(f"Archived {len(log_files)} logs to {archive_name}")

if __name__ == "__main__":
    archive_logs()

```

---

### 4. The Network & API Sentinel

**Libraries used:** `socket`, `requests`, `json`
This script checks if a local service is listening and sends a "Heartbeat" to a monitoring API or Slack.

```python
#!/usr/bin/python3
import socket
import requests
import json

WEB_HOOK_URL = "https://hooks.slack.com/services/T000/B000/XXXX"

def network_sentinel():
    # SOCKET: Check if Port 80 is open
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 80))
    
    status = "UP" if result == 0 else "DOWN"
    
    # REQUESTS & JSON: Send notification
    payload = {"text": f"Server Health Report: Web Service is {status}"}
    
    try:
        requests.post(WEB_HOOK_URL, data=json.dumps(payload))
    except requests. exceptions.RequestException as e:
        print(f"Could not send alert: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    network_sentinel()

```

---

### Summary Checklist for Production:

1. **`logging`**: Never use `print()` for long-running scripts; use logs so you can troubleshoot later.
2. **`try/except`**: Always wrap network (socket/requests) and file (os/tarfile) operations in try blocks to prevent the script from crashing.
3. **`sys.exit()`**: Use `sys.exit(0)` for success and `sys.exit(1)` (or higher) for failures so cron jobs or CI/CD pipelines can detect issues.
4. **`json`**: Store your variables (IPs, paths, thresholds) in a `.json` file so you don't have to edit the code to change a setting.

Would you like me to help you combine these into a single "Master Dashboard" script?


This **Master Dashboard Script** is the "Grand Finale." It imports every library we've discussed and organizes them into a single, modular system. It uses a **JSON configuration** to drive the logic and a **Main Loop** to execute health checks, remote management, and cleanup in one go.

### The Production Master Dashboard

```python
#!/usr/bin/python3
import os, sys, subprocess, shutil, json, logging, socket, tarfile, time
from pathlib import Path
from datetime import datetime

# --- EXTERNAL LIBRARIES (Install via pip install psutil requests paramiko) ---
import psutil
import requests
import paramiko

# 1. LOGGING SETUP
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("master_admin.log"), logging.StreamHandler()]
)

class AutomationMaster:
    def __init__(self, config_path):
        # 2. JSON & PATHLIB: Load Config
        self.config_path = Path(config_path)
        self.load_config()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    def load_config(self):
        if not self.config_path.exists():
            logging.error("Config file missing!")
            sys.exit(1)
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)

    # 3. PSUTIL & SHUTIL: Local Health
    def check_local_resources(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        _, used, _ = shutil.disk_usage("/")
        logging.info(f"Local Health -> CPU: {cpu}% | RAM: {ram}%")
        
        if cpu > self.config['thresholds']['cpu']:
            self.send_alert(f"High CPU Alert: {cpu}%")

    # 4. SUBPROCESS & SOCKET: Service Check
    def check_services(self):
        for srv in self.config['services']:
            status = subprocess.getoutput(f"systemctl is-active {srv}")
            if status != "active":
                logging.warning(f"Service {srv} is DOWN! Restarting...")
                subprocess.run(["sudo", "systemctl", "start", srv])
            
            # Use SOCKET to verify network response
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if s.connect_ex(('127.0.0.1', 80)) != 0:
                    logging.error("Web Service Port 80 not responding!")

    # 5. PARAMIKO: Remote Fleet Check
    def check_remote_nodes(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for node in self.config['remote_nodes']:
            try:
                ssh.connect(node, username=self.config['ssh_user'])
                _, stdout, _ = ssh.exec_command("uptime")
                logging.info(f"Node {node} Uptime: {stdout.read().decode().strip()}")
            except Exception as e:
                logging.error(f"Remote Node {node} unreachable: {e}")

    # 6. TARFILE & OS: Maintenance
    def cleanup_and_backup(self):
        backup_name = f"/tmp/backup_{self.timestamp}.tar.gz"
        with tarfile.open(backup_name, "w:gz") as tar:
            tar.add(self.config['backup_src'], arcname="web_data")
        logging.info(f"Maintenance: Backup created at {backup_name}")

    # 7. REQUESTS: Alerting System
    def send_alert(self, message):
        if self.config['webhook_url']:
            try:
                requests.post(self.config['webhook_url'], json={"text": message})
            except Exception as e:
                logging.error(f"Webhook failed: {e}")

    def run_all(self):
        logging.info("--- Starting Master Automation Cycle ---")
        self.check_local_resources()
        self.check_services()
        self.check_remote_nodes()
        self.cleanup_and_backup()
        logging.info("--- Cycle Complete ---")

# --- EXECUTION ---
if __name__ == "__main__":
    # Example config.json structure:
    # {
    #   "thresholds": {"cpu": 80, "ram": 90},
    #   "services": ["nginx", "cron"],
    #   "remote_nodes": ["10.0.0.5"],
    #   "ssh_user": "ubuntu",
    #   "backup_src": "/var/www/html",
    #   "webhook_url": ""
    # }
    master = AutomationMaster("config.json")
    master.run_all()

```

---

### Why this structure works for you:

* **Object-Oriented (`class`)**: By using a class, you can easily share data (like the `config`) between different parts of the script without using messy global variables.
* **Decoupled Config**: If you add a new server or a new service, you **don't touch the code**. You just update the `config.json` file.
* **Resilience**: The script uses `try/except` for remote nodes and webhooks, so if one server is down, the whole script doesn't crash; it just logs the error and moves to the next task.
* **Unified Logging**: Both the terminal and the `master_admin.log` file get the same updates, giving you a perfect audit trail for your Linux environment.

### Your Final Challenge

To master this, try setting up a **Cron Job** to run this script every hour.

1. Run `crontab -e`.
2. Add: `0 * * * * /usr/bin/python3 /path/to/your/script.py`.

Would you like me to explain how to secure the SSH keys or the sensitive Webhook URLs so they aren't sitting in plain text in your config file?
