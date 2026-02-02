
# ## 🟢 LEVEL 1 – STRING BASICS (1–10)
'''
# 1. Store your name as a string and print it.
name = "Shrinath"
print(name)

# 2. Print length of a string `"devops"`.
string = "devops"
print(len(string))

# 3. Convert `"LINUX"` to lowercase.
string = "LINUX"
print(string.lower())

# 4. Convert `"python"` to uppercase.
string = "python"
print(string.upper())

# 5. Remove spaces from `"  server01  "`.
string = "  server01    "
print(string.strip())


# 6. Check if `"ERROR"` exists in `"ERROR: disk full"`.
disk_log = "ERROR: disk full"

if "error" in disk_log.lower():
    print("There is error in the logs need to check asap.....")
else:
    print("Logs are fine no issue!")

# 7. Store a log message and print it.
msg = "System is working fine!!!!"
print(msg)

# 8. Replace `"dev"` with `"prod"` in `"dev_server"`.
SERVER = "dev_server"
print(SERVER.replace("dev", "prod"))

# 9. Split `"nginx running"` into words.
status = "Nginx Running"
print(status.split())

# 10. Join `["disk", "full"]` into one string.
disk = ["disk", "full"]
result = " ".join(disk)
print(result)


# ---

# ## 🟡 LEVEL 2 – REAL DEVOPS STRING TASKS (11–20)

# 11. Store a log line and check if `"WARNING"` exists.
LOGS = "WARNING: Disk / space is reached 90% please check..."
if "warning" in LOGS.lower():
    print("Its there")
else:
    print("Not present")

# 12. Replace IP `192.168.1.10` with `192.168.1.20`.
old_ip = "192.168.1.10"
new_ip = old_ip.replace("192.168.1.10", "192.168.1.20")
print(new_ip)

# 13. Extract service name from `"service=nginx status=running"`.
status = "service=nginx status=running"
service_name = status.split()[0].split("=")[1]
print(service_name)

# 14. Split file path `"/var/log/syslog"`.
path = "/var/log/syslog"
print(path.split("/"))


# 15. Remove newline characters from `"log line\n"`.
new_line = "log line\n"
print(new_line.strip())
print(new_line.rstrip("\n"))

# 16. Count characters in a hostname.
host = "shrinath"
print(len(host))

# 17. Convert environment name to uppercase.
env = "prod"
print(env.upper())

# 18. Check if log contains `"failed"`.
log_file = "Nginx service is failed...!"
if "failed" in log_file:
    print("The service is failed")
else:
    print("The service is runnig fine")

# 19. Join parts of a config line.
string = ["Config", "Line"]
result = " ".join(string)
print(result)

# 20. Replace `"http"` with `"https"` in a URL.
site = "http://www.google.com"
new_site = site.replace("http", "https")
print(new_site)
# ---
'''
# ## 🔵 LEVEL 3 – THINK LIKE A PRO (21–30)
'''
# 21. Read log input from user and print it.
user = input("Enter log for details: ")
print(f"User entered the input is: {user}")


# 22. Check if user-entered string contains `"error"`.
user_input = input("Enter your input: ")
if "error" in user_input.lower():
    print(f"User enter a error message for service! {user_input}")
else:
    print(f"User entered a {user_input} message so service is working fine")

# 23. Normalize input (strip + lowercase).
normal = input("Enter a message: ")
print(normal.strip().lower())


# 24. Parse `"user=root action=login"` and print user.
text = "user=root action=login"
user = text.split()[0].split("=")[1]
action = text.split()[1].split("=")[1]
print(user)
print(action)

# 25. Replace sensitive data `"password=123"` → `"password=****"`.
data = "password=123"
new_data = data.replace("123", "***")
print(new_data)

# 26. Count how many times `"ERROR"` appears.
enter_text = input("Enter a error message: ")
print(enter_text.lower().count("error"))
'''

# 27. Extract filename from path.
path = "/var/log/kern.log"
filename = path.split("/")[-1]
print(filename)


# 28. Build a status message using f-strings.
message = "Building a docker image please wait for some time...."
print(f"The docker is : {message}")

# 29. Clean log text before printing.
log_text = "   ERROR: Disk space low   \n"
cleaned_logs = log_text.strip()
print(cleaned_logs)

# 30. Print a final automation completion message.
msg = "The applciation successfully deployed with atutomation script"
print(msg)

