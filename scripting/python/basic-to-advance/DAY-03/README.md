
* 🐧 **Ubuntu/Linux-first**
* 🐍 Python + Linux commands
* 🛠 Real production-style automation
* ❌ No toy examples

---

# 🐧 UPDATED TRAINING MODE (IMPORTANT)

### From TODAY onward, we will:

✅ Use **Ubuntu commands**
✅ Use Python modules that interact with Linux
✅ Simulate **real DevOps tasks**
✅ Write scripts you can actually run on servers

This is how **professional DevOps engineers learn Python**.

---

# 📅 DAY 3 (UPDATED):

## Python + Ubuntu Linux (Loops with Real Commands)

⚠️ We are still on **DAY 3**, but now **Linux-powered**.

---

## 🔹 TOPIC 1: Running Linux Commands from Python

### ✅ Method 1 (Modern & Recommended): `subprocess`

```python
import subprocess

output = subprocess.getoutput("uname -a")
print(output)
```

✔ Used in real DevOps automation
❌ `os.system()` is NOT recommended anymore

---

## 🔹 TOPIC 2: Looping Over Linux Command Output

```python
import subprocess

files = subprocess.getoutput("ls").splitlines()

for file in files:
    print(f"Found file: {file}")
```

---

## 🔹 TOPIC 3: Checking Disk Usage (REAL TASK)

```python
import subprocess

disk = subprocess.getoutput("df -h /")
print(disk)
```

---

## 🔹 TOPIC 4: Loop + Condition (Production Pattern)

```python
import subprocess

lines = subprocess.getoutput("df -h").splitlines()

for line in lines:
    if "/dev" in line:
        print(line)
```

---

## 🔹 TOPIC 5: Service Status Check (Ubuntu)

```python
import subprocess

services = ["ssh", "cron", "nginx"]

for service in services:
    status = subprocess.getoutput(f"systemctl is-active {service}")
    print(f"{service}: {status}")
```

---

## 🔹 TOPIC 6: Retry Logic (Linux + Python)

```python
import subprocess
import time

attempt = 1

while attempt <= 3:
    status = subprocess.getoutput("systemctl is-active nginx")

    if status == "active":
        print("Nginx is running")
        break

    print("Retrying...")
    time.sleep(2)
    attempt += 1
else:
    print("Nginx failed after retries")
```

---

# 🧪 DAY 3 PRACTICE – **LINUX-BASED (25 EXERCISES)**

⚠️ Run these **on your Ubuntu machine**

---

## 🟢 LEVEL 1 – BASIC LINUX LOOPS (1–8)

1. Use Python to run `pwd` and print output.
2. Run `ls` and loop over each file.
3. Count number of files in current directory.
4. Run `whoami` and print username.
5. Loop 5 times and print `"Checking system..."`.
6. Run `uptime` and print output.
7. Loop through characters of `hostname`.
8. Print each directory in `/etc`.

---

## 🟡 LEVEL 2 – DEVOPS REAL TASKS (9–17)

9. Check disk usage using `df -h`.
10. Alert if disk usage > 80%.
11. Loop through services (`ssh`, `cron`) and print status.
12. Restart service if not active (print only, no real restart).
13. Retry ping to `google.com` 3 times.
14. Scan `/var/log/syslog` for `"error"`.
15. Loop through users from `/etc/passwd`.
16. Print memory usage using `free -h`.
17. Print running processes count.

---

## 🔵 LEVEL 3 – PRODUCTION AUTOMATION (18–25)

18. Monitor disk every 5 seconds (3 loops).
19. Stop loop if critical alert found.
20. Retry command until success.
21. Parse output of `df -h`.
22. Combine `for + if + subprocess`.
23. Loop through network interfaces.
24. Print health summary.
25. Final automation script with logs.

---

## ⚠️ SAFETY RULE (VERY IMPORTANT)

🚫 **DO NOT run destructive commands**

* No `rm`
* No `shutdown`
* No `reboot`
* No `systemctl restart` yet

We simulate first.

---

## 🧠 HOW REAL DEVOPS ENGINEERS DO THIS

✔ Test commands manually first
✔ Automate with Python
✔ Log every step
✔ Never assume success
✔ Always retry safely

---

# ✅ YOUR NEXT STEP

📌 Do **ALL 25 Linux-based exercises**
📌 Use `subprocess.getoutput()`
📌 Run on Ubuntu

> **DAY 3 COMPLETED (LINUX MODE)**

