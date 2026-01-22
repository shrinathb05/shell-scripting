#!/bin/usr/env python3

# > First learn logic → then bind it to the real environment (Linux).


# ---

# # 🐧 DAY 2 (LINUX MODE)

# ## Conditions + Decisions on Ubuntu

# 🎯 Goal:
# Make decisions based on **real system data**.

# ---

# ## 🟢 DAY 2 – LINUX PRACTICE (25 EXERCISES)

# ---

# ### 🟢 LEVEL 1 – BASIC CONDITIONS (1–8)
import subprocess
import os
import sys

# 1. Check if current user is `root`.
user = subprocess.getoutput("whoami")
if user == "root":
    print(f"The user is : {user}")
else:
    print(f"Invalid user: {user}")

# 2. Check if hostname length > 5.
host = subprocess.getoutput("hostname")
if len(host) > 5:
    print(f"The hostname {host} is greater than 5 characters")
else:
    print(f"The hostname {host} is less than 5 characters")

# 3. Check if `/etc/passwd` file exists.
file = "/etc/passwd"
if os.path.isfile(file):
    print(f"The file {file} exists")
else:
    print(f"The file {file} does not exist")

# 4. Check if `/tmp` directory exists.
dir = "/tmp"
if os.path.isdir(dir):
    print(f"The dir {dir} exists")
else:
    print(f"The dir {dir} does not exist")

# 5. Check if Python version is 3.
py_version = subprocess.getoutput("python3 --version")
if py_version.lower().startswith("python 3"):
    print(f"The current version is python3")
else:
    print("Current version not the python3")

# 6. Check if system uptime > 1 hour.
output = subprocess.getoutput("uptime -p")
#if "day" in output or "hour" in output:
if 'hour' in output or 'day' in output:
    print(f"The system is up from last {output} ")
else:
    print("The is just started")

# 7. Check if disk usage command runs successfully.
output = subprocess.getstatusoutput("df -h")
if output[0] == 0:
    print("The disk usage command runs successfully")
else:
    print("The disk usage command failed to run")


# 8. Print message if command output is empty.
output = subprocess.getoutput("df -h")
if output.strip() == "":
    print("The command output is empty")
else:
    print("The command output is not empty")

# ---

# ### 🟡 LEVEL 2 – DEVOPS CONDITIONS (9–17)

# 9. Alert if disk usage > 80%.
output = subprocess.getoutput("df -h | tail -1 | awk '{ print $5 }' | sed 's/%//'")
if int(output) > 80:
    print("The disk usage is over 80%")
else:
    print("The disk usage is under 80%")

# 10. Alert if memory usage > 70%.
#output = subprocess.getoutput("free -mh | grep -i 'mem' | awk '{ print $4 }' | sed 's/Gi//")
output = subprocess.getoutput("free -m | grep -i 'mem' | awk '{ print $3/$2 * 100.0 }' | cut -d'.' -f1")
int_output = int(output)
if int_output >  70:
    print("The memory space is ver low")
else:
    print("The memory usage is normal")

# 11. Check if `ssh` service is running.
ssh_service = subprocess.getoutput("systemctl is-active ssh")
if ssh_service == "active":
    print("The ssh service is running")
else:
    print("The ssh service is not running")

# 12. Check if `cron` service is active.
cron = subprocess.getoutput("systemctl is-active cron")
if cron == "active":
    print("The cron service is running")
else:
    print("The cron service is not running")

# 13. Skip deployment if OS is not Ubuntu.
output = subprocess.getoutput("grep '^ID=' /etc/os-release").split("=")[1].strip()
if output == "ubuntu":
    print(f"The OS is {output} proceeding with the deployment")
else:
    print("The selected OS not a correct OS skipping the deployment........")


# 14. Alert if `/var/log/syslog` contains `"error"`.
file = '/var/log/syslog'
if 'error' in file.lower():
    print(f'The file {file} has some errors !')
else:
    print('Logs are fine...')

# 15. Restart service if inactive (print only).
nginx_service = subprocess.getoutput("systemctl is-inactive nginx")
if nginx_service != "active":
    print("The Nginx service is Inactive")
else:
    print("The service working proper.....")

# 16. Block script if user is not root.
user = subprocess.getoutput("whoami")
if user == "root":
    print(f"The user is a root user: {user}")
else:
    print(f"The user is not a root user: {user}")

# 17. Print success if command exit code is 0.
status, output = subprocess.getstatusoutput("ls /tmp")
if status == 0:
    print("The command executed successfully")
else:
    print("The command failed to execute")
# ---

# ### 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)

# 18. Decide backup based on day (Linux date).
day = subprocess.getoutput("date +%A")
if day == "sunday":
    print("Taking the weekly backup")
else:
    print("Taking the daily backup")


# 19. Check multiple services at once.
# Example 1
service1 = subprocess.getoutput("systemctl is-active nginx")
service2 = subprocess.getoutput("systemctl is-active ssh")
service3 = subprocess.getoutput("systemctl is-active cron")

if service1 == "active" and service2 == "active" and service3 == "active":
    print("The all services are working fine")
else:
    print("There is an issue with one of the servie...")

# Example 2
services = ['nginx', 'ssh', 'cron']

if all(s == "active" for s in services):
    print("All services are running")
else:
    print("One or more services down")

# 20. Alert if any service is down.
service1 = subprocess.getoutput("systemctl is-active nginx")
if service1 != "active":
    print("The Nginx service is not working")
else:
    print("The service is working proper")

# 21. Decide scaling based on CPU load.

cpu_usage = int(subprocess.getoutput("top -bn1 | grep 'Cpu(s)' | awk '{ print $2 }' | cut -d . -f1"))
if cpu_usage > 85:
    print("CPU need to scale up")
else:
    print("CPU is working fine....")

# 22. Stop script if disk is full.
disk_space = int(subprocess.getoutput("df -h / | tail -1 | awk '{ print $5 }' | sed 's/%//'"))
if disk_space > 80:
    print("The disk is out space stopping the script....")
else:
    print("No issue with the disk space")

# # 23. Confirm user input before action.
# user = input("Enter your name: ").strip

# if user:
#     print("the user is logged in")
# else:
#     print("Invalid username")

# 24. Combine multiple conditions.
cpu_usage = int(subprocess.getoutput("top -bn1 | grep 'Cpu(s)' | awk '{ print $2 }' | cut -d . -f1"))
disk_space = int(subprocess.getoutput("df -h / | tail -1 | awk '{ print $5 }' | sed 's/%//'"))

if cpu_usage > 80 and disk_space > 85:
    print("CRITICAL: CPU and DISK are in high!")
elif cpu_usage > 80:
    print("High cpu usage")
elif disk_space > 85:
    print("High disk usage")
else:
    print("system is healthy!")

# 25. Print final system health status.
host = subprocess.getoutput("hostname").strip()
usr = subprocess.getoutput("whoami").strip()
sys_time = subprocess.getoutput("uptime -p").strip()
os_name = subprocess.getoutput("grep '^ID=' /etc/os-release").split("=")[1].strip()
disk = subprocess.getoutput("df -h /").strip()
mem = subprocess.getoutput("free -htl").strip()

print("--" * 60)
print("                          System Health Status")
print("--" * 60)
print("The hsotname:                        {host}")
print("The current logged in user:          {usr}")
print("The machine up from last:            {sys_time}")
print("The machine OS name:                 {os_name}")
print("--" * 60)
print("The disk space of filesystems: ")
print(disk)
print("--" * 60)
print("The system memory details: ")
print(mem) 
print("--" * 60)
print("                          System Health Status")
print("--" * 60)


# ---

# ## ⚠️ IMPORTANT SAFETY NOTE

# 🚫 Do **NOT** run destructive commands
# ✔ Read-only commands only
# ✔ Print instead of execute restarts

# ---

# ## 🧠 WHY THIS MATTERS (REALITY)

# Real DevOps engineers:

# * Don’t practice fake variables
# * Use **actual system data**
# * Write scripts that **observe → decide → act**

# You are now training **exactly like that**.

# ---

# ## ✅ HOW TO USE THIS

# You can:

# * Practice these alongside Day 3
# * Strengthen fundamentals deeply
# * Re-run them anytime

# ---
