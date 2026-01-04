# 🐧 DAY 1 (LINUX MODE)

## Python Basics + Strings using Ubuntu

🎯 Goal:
Learn Python basics while interacting with the Linux system.

---

## 🟢 DAY 1 – LINUX PRACTICE (20 EXERCISES)

### 🔹 Setup (Use in all scripts)

```python
import subprocess
```

---


# ### 🟢 LEVEL 1 – BASIC LINUX + PYTHON (1–7)

# 1. Run `whoami` and print the output.
import subprocess
output = subprocess.getoutput("whoami")
print(output)

# 2. Run `hostname` and store it in a variable.
import subprocess
my_hostname = subprocess.getoutput("hostname")
print(my_hostname)

# 3. Print the length of the hostname.
import subprocess
my_hostname = subprocess.getoutput("hostname")
print(len(my_hostname))


# 4. Convert hostname to uppercase.
my_hostname = subprocess.getoutput("hostname")
print(len(my_hostname))

# 5. Remove newline from command output.
output = subprocess.getoutput("whoami")
print(output.strip())

# 6. Run `pwd` and print working directory.
output = subprocess.getoutput("pwd")
print(f"The present working directory is {output} !")


# 7. Print Python version using `python3 --version`.
version = subprocess.getoutput("python3 --version")
print(f"The python current version is: {version}")

# ---

# ### 🟡 LEVEL 2 – STRINGS + LINUX OUTPUT (8–14)

# 8. Run `ls` and print each file name.
file_name = subprocess.getoutput("ls")
print(f"The files are contain in the directory are: {file_name}")

# 9. Count number of files in current directory.
count = subprocess.getoutput("ls | wc -l")
print(f"The count is: {count}")


# 10. Check if `"bin"` exists in output of `ls /`.
output = subprocess.getoutput("ls /")
if "bin" in output:
    print("The bin found in the output")
else:
    print("Bin does not exist in root directory ! Hence Not found!")

# 11. Replace `/home` with `/root` in a path string.

BASE = "/home/python_scripting"
print(f"The old path: {BASE}")
newpath = BASE.replace("home", "root")
print(f"The new_path: {newpath}")


# 12. Split output of `uname -a` into words.
output = subprocess.getoutput("uname -a")
print(output.split())

# 13. Join words back using `-`.
output = subprocess.getoutput("uname -a")
print(output.join("-"))


# 14. Extract kernel version from `uname -r`.
output = subprocess.getoutput("uname -r")
print(output)

# ---

# ### 🔵 LEVEL 3 – REAL DEVOPS STRINGS (15–20)

# 15. Read `/etc/os-release` and print OS name.
output = subprocess.getoutput("grep 'PRETTY_NAME' /etc/os-release")
os_version = output.split("=")[1].replace('"', '')
print(os_version)

# 16. Check if OS is Ubuntu.
output = subprocess.getoutput("cat /etc/os-release | grep PRETTY_NAME")
if "ubuntu" in output.lower():
    print("The OS is ubuntu")
else:
    print("The Os is not a ubuntu machine")

# 17. Scan `/etc/passwd` for `"root"`.
output = subprocess.getoutput("grep '^root' /etc/passwd")
if output:
    print(f"The user {output} is found")
else:
    print("There is no root user")

# 18. Print first 5 users from `/etc/passwd`.
output = subprocess.getoutput("head -n 5 /etc/passwd ")
if output:
    print("The users are below:")
    print(output)
else:
    print("Something wrong check with correct directory")

# 19. Clean and print `uptime` output.
output = subprocess.getoutput("uptime -p")
print(f"The System is up: {output.strip()}")


# 20. Print a formatted system summary.
user = subprocess.getoutput("whoami")
host = subprocess.getoutput("hostname")
time = subprocess.getoutput("uptime -p")

print("-" * 40)
print("          SYSTEM SUMMARY")
print("-" * 40)
print(f"USER: {user}")
print(f"HOST: {host}")
print(f"System Uptime: {time.strip()}")
print("-" * 40)


# ---
---


## ⚠️ IMPORTANT SAFETY NOTE

🚫 Do **NOT** run destructive commands
✔ Read-only commands only
✔ Print instead of execute restarts

---

## 🧠 WHY THIS MATTERS (REALITY)

Real DevOps engineers:

* Don’t practice fake variables
* Use **actual system data**
* Write scripts that **observe → decide → act**

You are now training **exactly like that**.

---
