# ### 🟢 LEVEL 1 – BASIC CONDITIONS (1–8)

# 1. Check if current user is `root`.
import subprocess
user = subprocess.getoutput("whoami").strip()
if user == 'root':
    print(f"The user is: {user} user")
else:
    print(f"The user is not a Root user")

# 2. Check if hostname length > 5.
hostname = subprocess.getoutput("hostname").strip()
if len(hostname) > 5:
    print(f"The hostname {hostname} length is greater than 5")
else:
    print(f"The hostname {hostname} lenght is leass than 5")

# 3. Check if `/etc/passwd` file exists.
# Example 1
file_path = subprocess.getoutput("ls /etc/passwd").strip()
if file_path:
    print(f"The file is exist's")
else:
    print("The file does not exist's")

# Example 2 --- recommended
import os
file_path = "/etc/passwd"
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File not found: {file_path}")


# 4. Check if `/tmp` directory exists.
# Example --- 1
dir = subprocess.getoutput("ls /tmp").strip()
if dir:
    print("The /tmp directory exist")
else:
    print("The /tmp directory does not exist")

# Example 2 --- recommended

import os
dir = "/tmp"
if os.path.isdir(dir):
    print(f"The Directory exist's: {dir}")
else:
    print(f"The directory not found: {dir}")


# 5. Check if Python version is 3.
# Example 1
py_version = subprocess.getoutput("python --version")
if "3" in py_version:
    print(f"The python version is: {py_version}")
else:
    print("The python version is old version")


# Example 2
import sys
# sys.version_info[0] returns the major version number (e.g., 3)
if sys.version_info[0] == 3:
    print(f"The python version is: {sys.version}")
else:
    print("This is not Python 3")
    

# 6. Check if system uptime > 1 hour.
import subprocess
uptime_str = subprocess.getoutput("uptime -p")
if 'day' in uptime_str or 'hour' in uptime_str:
    print(f"The system is up from more than an hour: {uptime_str}")
else:
    print(f"The system is just started: {uptime_str}")

# 7. Check if disk usage command runs successfully.
result = subprocess.run(["df", "-h"], capture_output = True, text = True)
if result.returncode == 0:
    print("Success: Disk usage command run successully")
else:
    print("Error: command failed with the exit code {result.reurtncode}")

# 8. Print message if command output is empty.
output = subprocess.getoutput("grep 'fakeuser' /etc/passwd")
if not output:
    print("The user not found or it's empty")
else:
    print(f"Data found: {output}")

# ---

# ### 🟡 LEVEL 2 – DEVOPS CONDITIONS (9–17)

# 9. Alert if disk usage > 80%.
# /dev/root directory space
disk_usage = subprocess.getoutput("grep 'dev/root' df -h | awk '{ print $5 }' | sed 's/%//'")
if disk_usage > 75:
    print(f"Disk usage is in critical condition: {disk_usage}% please check")
else:
    print("No issue with the disk space!")

# 10. Alert if memory usage > 70%.
mem_usage = subprocess.getoutput("freem -m | grep 'Mem' | awk '{ print $4}'")
if mem_usage > 70:
    print(f"Out of memory: {mem_usage}")
else:
    print(f"Memmory usage is fine")

# 11. Check if `ssh` service is running.
ssh_service = subprocess.getoutput("systemctl is-active sshd")
if ssh_service == "active":
    print("SSH service is running")
else:
    print("SSH service is not running")


# 12. Check if `cron` service is active
cron_service = subprocess.getoutput("systemctl is-active cron")
if cron_service == "active":
    print("Cron service is running")
else:
    print("Cron service is not running")

# 13. Skip deployment if OS is not Ubuntu.
os_name = subprocess.getoutput("grep '^ID=' /etc/os-release").split('=')[1].strip('"')
if output == "ubuntu":
    print("The selected OS is ubuntu os proceeding with depooyment..")
else:
    print("The OS is wrong rejecting the deployment")

# 14. Alert if `/var/log/syslog` contains `"error"`.
dir = '/var/log/syslog'
if 'error' in dir.lower:
    print("There is error in the {dir} file critical")
else:
    print("The system is working fine")

# 15. Restart service if inactive (print only).


# 16. Block script if user is not root.
# 17. Print success if command exit code is 0.

# ---

# ### 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)

# 18. Decide backup based on day (Linux date).
# 19. Check multiple services at once.
# 20. Alert if any service is down.
# 21. Decide scaling based on CPU load.
# 22. Stop script if disk is full.
# 23. Confirm user input before action.
# 24. Combine multiple conditions.
# 25. Print final system health status.
