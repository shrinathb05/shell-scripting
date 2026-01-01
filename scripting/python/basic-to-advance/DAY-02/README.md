
Welcome to **DAY 2**.

---

# 📅 DAY 2 – CONDITIONS & DECISION MAKING

## Thinking Like an Automation System (if / elif / else)

⚠️ **Professional Rule**
We will not move forward until:

* You finish all exercises
* You confirm completion

---

## 🎯 DAY 2 GOAL

By the end of Day 2, you will:

* Control script behavior using logic
* Write production-style checks
* Make automation decisions like a DevOps engineer
* Understand **why something runs**, not just **how**

---

## 🔹 TOPIC 1: Comparison Operators (FOUNDATION)

| Operator | Meaning       | Example               |
| -------- | ------------- | --------------------- |
| `==`     | equal         | `status == "running"` |
| `!=`     | not equal     | `env != "prod"`       |
| `>`      | greater       | `cpu > 80`            |
| `<`      | less          | `disk < 20`           |
| `>=`     | greater/equal | `memory >= 70`        |
| `<=`     | less/equal    | `retries <= 3`        |

```python
cpu_usage = 85
print(cpu_usage > 80)
```

---

## 🔹 TOPIC 2: if Statement (DECISION POINT)

```python
disk_usage = 90

if disk_usage > 80:
    print("WARNING: Disk usage high")
```

Python executes the block **only if condition is True**.

---

## 🔹 TOPIC 3: if–else

```python
service_status = "running"

if service_status == "running":
    print("Service is healthy")
else:
    print("Service is down")
```

---

## 🔹 TOPIC 4: if–elif–else (MULTIPLE CONDITIONS)

```python
cpu = 95

if cpu < 50:
    print("CPU is normal")
elif cpu < 80:
    print("CPU is high")
else:
    print("CPU is critical")
```

---

## 🔹 TOPIC 5: Logical Operators (REAL POWER)

| Operator | Meaning           |
| -------- | ----------------- |
| `and`    | both must be true |
| `or`     | any one true      |
| `not`    | reverse result    |

```python
env = "prod"
cpu = 90

if env == "prod" and cpu > 80:
    print("CRITICAL alert")
```

---

## 🔹 REAL DEVOPS EXAMPLE (VERY IMPORTANT)

```python
log = "ERROR: nginx stopped"

if "error" in log.lower():
    print("ALERT: Issue detected")
else:
    print("System normal")
```

---

# 🧪 DAY 2 PRACTICE – **25 EXERCISES**

⚠️ **Write actual Python code. No pseudo-code.**

---

## 🟢 LEVEL 1 – BASIC CONDITIONS (1–8)

1. Check if a number is greater than 10.
2. Check if CPU usage is above 80.
3. Check if service status is `"running"`.
4. Compare two numbers and print the bigger one.
5. Check if a string equals `"prod"`.
6. Check if retry count is less than 3.
7. Check if disk usage equals 100.
8. Print message if value is not equal to zero.

---

## 🟡 LEVEL 2 – DEVOPS CONDITIONS (9–17)

9. Alert if disk usage > 85.
10. Print message if service is stopped.
11. Check if environment is `"prod"`.
12. Check if log contains `"error"`.
13. Restart service if status != `"running"`.
14. Alert if CPU > 80 AND memory > 75.
15. Skip deployment if env != `"prod"`.
16. Alert if retries exceeded limit.
17. Print success if exit code == 0.

---

## 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)

18. Check multiple service statuses.
19. Decide backup based on day.
20. Alert if log contains `"ERROR"` or `"FAILED"`.
21. Validate username input.
22. Block script if environment is `"test"`.
23. Decide scaling based on CPU.
24. Perform action only if user confirms `"yes"`.
25. Print final status based on multiple conditions.

---

## ⚠️ COMMON MISTAKES (READ CAREFULLY)

❌ Using `=` instead of `==`
❌ Forgetting indentation
❌ Comparing string with number
❌ Case-sensitive checks without `.lower()`
❌ Writing complex logic without testing step-by-step

---

## 🧠 HOW PROFESSIONALS WRITE CONDITIONS

✔ Print values before checking
✔ Normalize inputs
✔ Handle edge cases
✔ Prefer readability over clever logic

---

# ✅ YOUR TASK NOW

📌 Complete **ALL 25 exercises**
📌 Write real Python scripts

> **DAY 2 COMPLETED**
