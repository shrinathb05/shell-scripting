
<!-- --- -->

# 📄 DAY 3 – (WITH 30+ EXERCISES)

---

````markdown
# DAY 3 – Python Loops for DevOps Automation (Linux Mode)

## 🎯 Goal of Day 3
Loops allow DevOps engineers to:
- Automate repetitive tasks
- Scan logs
- Monitor servers
- Retry failed operations
- Perform health checks

Without loops, automation is impossible.

---

## 1️⃣ for Loop (Most Used in DevOps)

A `for` loop iterates over a collection (list, string, command output).

### Example
```python
for i in range(1, 6):
    print(i)
````

<!-- ### DevOps Example -->

```python
servers = ["web1", "web2", "db1"]

for server in servers:
    print(f"Checking server: {server}")
```

---

## 2️⃣ range() – Control Execution Count

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

Used for:

* retries
* batch jobs
* deployments

---

## 3️⃣ Looping Over Linux Command Output

Linux commands return strings → split → loop.

```python
import subprocess

files = subprocess.getoutput("ls").splitlines()

for file in files:
    print(file)
```

---

## 4️⃣ while Loop – Retry & Monitoring

Runs until condition becomes false.

```python
retry = 1

while retry <= 3:
    print(f"Retry attempt {retry}")
    retry += 1
```

### Retry Service Example

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
```

---

## 5️⃣ break & continue

### break

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### continue

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 6️⃣ Core DevOps Pattern: Loop + Condition

```python
services = ["nginx", "ssh", "cron"]

for service in services:
    status = subprocess.getoutput(f"systemctl is-active {service}")

    if status != "active":
        print(f"ALERT: {service} is down")
```

This pattern is used everywhere in production.

---

<!-- # 🧪 DAY 3 – PRACTICE EXERCISES (35 TOTAL) -->

## 🟢 LEVEL 1 – LOOP BASICS (1–12)

1. Print numbers from 1 to 10
2. Print numbers from 10 to 1
3. Print even numbers from 1 to 20
4. Loop through string `"devops"`
5. Print each character of hostname
6. Loop 5 times and print a message
7. Print numbers divisible by 3
8. Loop through list of names
9. Skip number 5 using `continue`
10. Stop loop at number 7 using `break`
11. Print index + value from list
12. Reverse loop using `range()`

---

## 🟡 LEVEL 2 – LINUX + DEVOPS (13–24)
<!-- 
13. Loop through files from `ls`
14. Count number of files
15. Loop through `/etc` directory
16. Loop through users from `/etc/passwd`
17. Loop through services and check status
18. Retry command 3 times
19. Loop through log lines
20. Print CPU usage list values
21. Skip inactive services
22. Break loop on critical alert
23. Print deployment steps
24. Loop through directories in `/var/log` -->

---

## 🔵 LEVEL 3 – PRODUCTION AUTOMATION (25–35)
<!-- 
25. Retry service start until success
26. Monitor disk usage in loop
27. Alert if usage exceeds threshold
28. Scan logs for ERROR
29. Stop monitoring on critical alert
30. Loop through network interfaces
31. Combine `if` inside `for`
32. Combine `while` + retry logic
33. Iterate over dictionary (service → status)
34. Build monitoring loop with summary
35. Final automation loop with report

--- -->

## ❌ Common Mistakes

* Infinite `while` loops
* Missing retry increment
* No exit condition
* No logging
* Over-nesting loops

---

## ✅ Professional Best Practices

✔ Always log inside loops
✔ Always have exit conditions
✔ Prefer `for` over `while` unless retrying
✔ Test Linux commands manually first
✔ Fail fast on critical errors

---

## 📌 Summary

Today you mastered:

* for loops
* while loops
* break / continue
* Linux command iteration
* Retry logic
* Monitoring patterns

This is **core DevOps automation skill**.

<!-- ``` -->
