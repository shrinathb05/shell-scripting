import subprocess
import os
import time

# <!-- # 🧪 DAY 3 – PRACTICE EXERCISES (35 TOTAL) -->

# ## 🟢 LEVEL 1 – LOOP BASICS (1–12)

'''
# 1. Print numbers from 1 to 10
for i in range(1,11):
    print(i)

# 2. Print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

# 3. Print even numbers from 1 to 20
for i in range(0,21,2):
    print(i)

# 4. Loop through string `"devops"`
course = "devops"
for i in course:
    print(i)
    
# 5. Print each character of hostname
import subprocess
host = subprocess.getoutput("hostname")
for i in host:
    print(i)

# 6. Loop 5 times and print a message
msg = "Hi"
for i in range(5):
    print(msg)

# 7. Print numbers divisible by 3
for i in range(1,31):
    if i % 3 == 0:
        print(i) 

# 8. Loop through list of names
names = ["shri", "omkar", "Suraj", "Pravin"]
for name in names:
    print(name)

# 9. Skip number 5 using `continue`
for i in range(1,10):
    if i == 5:
        continue
    print(i)


# 10. Stop loop at number 7 using `break`
for i in range(1,10):
    if i == 7:
        break
    print(i)


# 11. Print index + value from list
names = ["shri", "omkar", "Suraj", "Pravin"]
for index, name in enumerate(names):
    print(index, name)

# 12. Reverse loop using `range()`
for i in range(10,0,-1):
    print(i)

# ---

# ## 🟡 LEVEL 2 – LINUX + DEVOPS (13–24)
# <!-- 
# 13. Loop through files from `ls`
import subprocess
loop_file = subprocess.getoutput("ls")
for i in loop_file:
    print(i)

# 14. Count number of files
import subprocess
output = subprocess.getoutput("ls | wc -l")
print(output)


# 15. Loop through `/etc` directory
dir = subprocess.getoutput("ls /etc")
print(dir)
for i in dir:
    print(i)


# 16. Loop through users from `/etc/passwd`
out = subprocess.getoutput("cat /etc/passwd | tail -5").strip().split("\n")
for i in out:
    print(i)
'''
# 17. Loop through services and check status
services = ["ssh", "cron", "nginx"]
for service in services:
    status = subprocess.getoutput(f"systemctl is-active {service}")
    print(f"{service} service : {status}")
    if status != "active":
        print(f"The {service} service is inactive starting the services...")
        time.sleep(3)
        subprocess.getoutput(f"sudo systemctl start {service}")
        print(f"Inactive service {service} started successfully")
        time.sleep(3)


# 18. Retry command 3 times
# 19. Loop through log lines
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