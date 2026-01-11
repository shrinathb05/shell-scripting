
# <!-- # 🧪 DAY 3 – PRACTICE EXERCISES (35 TOTAL) -->

# ## 🟢 LEVEL 1 – LOOP BASICS (1–12)

# 1. Print numbers from 1 to 10
for i in range(1,11):
    print(i)

# 2. Print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

# 3. Print even numbers from 1 to 20
for i in range(2,21,2):
    print(i)

# 4. Loop through string `"devops"`
for char in "devops":
    print(char)

# 5. Print each character of hostname
hostname = "my-computer"
for char in hostname:
    print(char)
# 6. Loop 5 times and print a message
for i in range(5):
    print("This is loop iteration", i+1)
# 7. Print numbers divisible by 3
for i in range(1, 31):
    if i % 3 == 0:
        print(i)
# 8. Loop through list of names
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
# 9. Skip number 5 using `continue`
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# 10. Stop loop at number 7 using `break`
for i in range(1, 11):
    if i == 7:
        break
    print(i)
# 11. Print index + value from list
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}") 
# 12. Reverse loop using `range()`
for i in range(10, 0, -1):
    print(i)


# ---

# ## 🟡 LEVEL 2 – LINUX + DEVOPS (13–24)
# <!-- 
# 13. Loop through files from `ls`
import os
for filename in os.listdir('.'):
    print(filename)

# 14. Count number of files
file_count = len(os.listdir('.'))
print("Number of files:", file_count)

# 15. Loop through `/etc` directory
for filename in os.listdir('/etc'):
    print(filename)

# 16. Loop through users from `/etc/passwd`
with open('/etc/passwd', 'r') as f:
    for line in f:
        user = line.split(':')[0]
        print(user)

# 17. Loop through services and check status
import subprocess
services = ['ssh', 'cron', 'nonexistentservice']
for service in services:
    result = subprocess.run(['systemctl', 'is-active', service], capture_output=True, text=True)
    status = result.stdout.strip()
    print(f"Service {service} is {status}") 

# 18. Retry command 3 times
import time
command = ['ping', '-c', '1', 'google.com']
for i in range(3):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Command succeeded.")
        break
    else:
        print("Command failed. Retrying...")
        time.sleep(1)

# 19. Loop through log lines
with open('/var/log/syslog', 'r') as f:
    for line in f:
        print(line.strip())

# 20. Print CPU usage list values
# 21. Skip inactive services
# 22. Break loop on critical alert
# 23. Print deployment steps
# 24. Loop through directories in `/var/log` -->

# ---

# ## 🔵 LEVEL 3 – PRODUCTION AUTOMATION (25–35)
# <!-- 
# 25. Retry service start until success
# 26. Monitor disk usage in loop
# 27. Alert if usage exceeds threshold
# 28. Scan logs for ERROR
# 29. Stop monitoring on critical alert
# 30. Loop through network interfaces
# 31. Combine `if` inside `for`
# 32. Combine `while` + retry logic
# 33. Iterate over dictionary (service → status)
# 34. Build monitoring loop with summary
# 35. Final automation loop with report

# --- -->