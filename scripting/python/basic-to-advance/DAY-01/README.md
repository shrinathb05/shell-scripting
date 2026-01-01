
---

# 📅 DAY 1 (UPDATED & FINAL)

## Python Fundamentals + String Operations (Logic First)

⚠️ **We are still on Day 1**
➡ You must complete this before Day 2
➡ Day 2 will depend heavily on strings

---

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
