
# 📅 DAY 1 

## Python Fundamentals – Thinking Like an Automation Engineer

### 🎯 DAY 1 GOAL

By the end of today, you will:

* Think in **variables and logic**
* Understand how scripts execute line-by-line
* Be comfortable writing **very small but correct scripts**
* Build confidence before touching advanced topics

---

## 🔹 TOPIC 1: Python Program Structure

### 🔍 Key Concepts

* Python runs **top to bottom**
* Every script is a **sequence of instructions**
* Whitespace & indentation matter

### Example:

```python
print("Script started")
print("Script running")
print("Script finished")
```

---

## 🔹 TOPIC 2: Variables (CORE OF LOGIC)

### 🔍 What professionals do:

Variables represent:

* server names
* IPs
* file paths
* counts
* flags (True/False)

```python
server_name = "web-01"
uptime_days = 12
is_running = True
```

---

## 🔹 TOPIC 3: Data Types (ABSOLUTE MUST)

| Type  | Example   | DevOps Use    |
| ----- | --------- | ------------- |
| str   | `"nginx"` | service names |
| int   | `5`       | retry count   |
| float | `75.5`    | CPU usage     |
| bool  | `True`    | health checks |

Check type:

```python
print(type(server_name))
```

---

## 🔹 TOPIC 4: Printing & Reading Input

```python
name = input("Enter your name: ")
print(f"Welcome {name}")
```

---

# 🧪 DAY 1 PRACTICE – **20 EXERCISES**

⚠️ **You MUST write scripts for each. No shortcuts.**

---

## 🟢 LEVEL 1 – BASIC LOGIC (1–7)

1. Create a script that prints your name and role as "DevOps Engineer".
2. Store a server name in a variable and print it.
3. Store CPU usage as a number and print it.
4. Print the data type of:

   * a string
   * an integer
5. Take user input for username and print a welcome message.
6. Store today’s task (string) and print it.
7. Store `True` in a variable called `server_up` and print it.

---

## 🟡 LEVEL 2 – REAL DEVOPS CONTEXT (8–14)

8. Store:

   * hostname
   * IP address
     Print them in one line.
9. Store disk usage percentage and print:

   ```
   Disk usage is 70%
   ```
10. Store number of running containers and print it.
11. Ask user for environment name (dev/prod) and print it.
12. Store log file path and print it.
13. Store backup status (`True` or `False`) and print it.
14. Store retry count and print:

```
Retry attempt: 3
```

---

## 🔵 LEVEL 3 – THINK LIKE A SCRIPT (15–20)

15. Take user input for server name and print:

```
Checking server: <server_name>
```

16. Store service name and its status and print both.
17. Store memory usage as float and print it.
18. Print a formatted message using **f-string** with 3 variables.
19. Print a startup message:

```
Automation Script Started
```

20. Print an end message:

```
Automation Script Completed Successfully
```

---

# ❌ COMMON BEGINNER MISTAKES (READ CAREFULLY)

❌ Using variables before assigning them
❌ Mixing strings and numbers without formatting
❌ Forgetting `f` in f-strings
❌ Wrong indentation
❌ Copy-pasting without understanding

---

# 🧠 HOW PROFESSIONALS PRACTICE (VERY IMPORTANT)

Senior DevOps engineers:

* Write **tiny scripts daily**
* Print everything to understand flow
* Never rush topics
* Practice same logic in multiple ways
* Debug by printing variables

You are training **exactly the same way**.

---

# ✅ YOUR TASK NOW

📌 **Do ALL 20 exercises**
📌 Write them as small scripts (can be separate or one file)
📌 Take your time


## Python Fundamentals + String Operations (Logic First)

## 🔹 TOPIC 5: Strings (VERY IMPORTANT FOR DEVOPS)

Strings represent:

* log lines
* file paths
* service names
* environment names
* command outputs

```python
log_line = "ERROR: Disk space is low"
```

---

## 🔹 STRING BASICS

```python
text = "devops"
```

| Operation  | Example             |
| ---------- | ------------------- |
| Length     | `len(text)`         |
| Uppercase  | `text.upper()`      |
| Lowercase  | `text.lower()`      |
| Capitalize | `text.capitalize()` |
| Check      | `"dev" in text`     |

---

## 🔹 MOST USED STRING FUNCTIONS (REAL-WORLD)

### 🔍 `find()`

```python
log = "ERROR: Service failed"
print(log.find("ERROR"))  # returns index
```

### 🔁 `replace()`

```python
path = "/var/log/nginx"
new_path = path.replace("nginx", "apache")
```

### ✂️ `split()`

```python
log = "ERROR Disk Full"
parts = log.split()
```

### 🔗 `join()`

```python
words = ["Disk", "Full"]
message = " ".join(words)
```

### 🧼 `strip()` (VERY COMMON)

```python
text = "  server01  "
print(text.strip())
```

---

## 🔹 DEVOPS STRING USE CASE EXAMPLE

```python
log = "ERROR: nginx service stopped"

if "ERROR" in log:
    print("Alert! Issue found in log")
```

(You’ll fully master `if` tomorrow.)

---

# 🧪 DAY 1 PRACTICE – **UPDATED TO 30 EXERCISES**

(Professional-grade training)

---

## 🟢 LEVEL 1 – STRING BASICS (1–10)

1. Store your name as a string and print it.
2. Print length of a string `"devops"`.
3. Convert `"LINUX"` to lowercase.
4. Convert `"python"` to uppercase.
5. Remove spaces from `"  server01  "`.
6. Check if `"ERROR"` exists in `"ERROR: disk full"`.
7. Store a log message and print it.
8. Replace `"dev"` with `"prod"` in `"dev_server"`.
9. Split `"nginx running"` into words.
10. Join `["disk", "full"]` into one string.

---

## 🟡 LEVEL 2 – REAL DEVOPS STRING TASKS (11–20)

11. Store a log line and check if `"WARNING"` exists.
12. Replace IP `192.168.1.10` with `192.168.1.20`.
13. Extract service name from `"service=nginx status=running"`.
14. Split file path `"/var/log/syslog"`.
15. Remove newline characters from `"log line\n"`.
16. Count characters in a hostname.
17. Convert environment name to uppercase.
18. Check if log contains `"failed"`.
19. Join parts of a config line.
20. Replace `"http"` with `"https"` in a URL.

---

## 🔵 LEVEL 3 – THINK LIKE A PRO (21–30)

21. Read log input from user and print it.
22. Check if user-entered string contains `"error"`.
23. Normalize input (strip + lowercase).
24. Parse `"user=root action=login"` and print user.
25. Replace sensitive data `"password=123"` → `"password=****"`.
26. Count how many times `"ERROR"` appears.
27. Extract filename from path.
28. Build a status message using f-strings.
29. Clean log text before printing.
30. Print a final automation completion message.

---

# 🧠 WHY THIS MATTERS (REALITY CHECK)

In production, DevOps engineers:

* Parse logs → strings
* Read configs → strings
* Handle CLI output → strings
* Modify YAML/JSON → strings

Mastering strings = **automation power**

---

# 🚫 DO NOT MOVE AHEAD IF:

❌ You don’t understand `find()`
❌ You can’t use `replace()`
❌ You’re guessing instead of thinking

---

# ✅ YOUR NEXT STEP

✔ Complete **all 30 exercises**
✔ Write code yourself
