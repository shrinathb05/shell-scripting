 ## 🟢 LEVEL 1 – STRING BASICS (1–10)
'''
# 1. Store your name as a string and print it.
name = "Shrinath Bhosale"
print(f"My name is {name}")

# 2. Print length of a string `"devops"`.
string = "devops"
print(len(string))

# 3. Convert `"LINUX"` to lowercase.
print("LINUX".lower())

# 4. Convert `"python"` to uppercase.
print("python".upper())

# 5. Remove spaces from `"  server01  "`.
string = "  server01  "
print(string.strip())

# 6. Check if `"ERROR"` exists in `"ERROR: disk full"`.
msg = "ERROR: disk full"
print(msg.find("ERROR") != -1)
print("ERROR" in msg)

# 7. Store a log message and print it.
LOG = "Thu 01 Jan 2026 05:32:15 PM IST shri"
print(LOG) 

# 8. Replace `"dev"` with `"prod"` in `"dev_server"`.
string = "dev_server"
print(string.replace("dev", "prod"))

# 9. Split `"nginx running"` into words.
string = "Nginx Running"
print(string.split())

# 10. Join `["disk", "full"]` into one string.
string_example = ["Disk", "Full"]
print(" ".join(string_example))

#--------------------------------------------------------------------------------------------

#---

## 🟡 LEVEL 2 – REAL DEVOPS STRING TASKS (11–20)

# 11. Store a log line and check if `"WARNING"` exists.
log = "Alert! Warning: the /root directory spce is full!!!!"
print("Warning" in log)


# 12. Replace IP `192.168.1.10` with `192.168.1.20`.
ip_addr = "192.168.1.10"
print(ip_addr.replace("192.168.1.10", "92.168.1.20"))

# 13. Extract service name from `"service=nginx status=running"`.
service_info = "service=nginx status=running"
service_name = service_info.split()[0].split("=")[1]
service_status = service_info.split()[1].split("=")[1]
print(service_name)
print(service_status)
print(service_info.partition(" ")[0].partition("=")[2])
print(service_info.rpartition(" ")[0].rpartition("=")[2])
print(service_info.split(" ")[0].split("=")[1])
print(service_info.split(" ")[1].split("=")[1])
print(service_info[8:13])
print(service_info[25:32])
print(service_info[service_info.find("nginx"):service_info.find("nginx")+5])
print(service_info[service_info.find("running"):service_info.find("running")+7])
print(service_info[service_info.index("nginx"):service_info.index("nginx")+5])
print(service_info[service_info.index("running"):service_info.index("running")+7])
print(service_info.encode()[8:13].decode())
print(service_info.encode()[25:32].decode())


# 14. Split file path `"/var/log/syslog"`.
path = "var/log/syslog"
print(path.split("/"))
print(path.partition("/"))
print(path.rpartition("/"))
print(path.split("log"))    


# 15. Remove newline characters from `"log line\n"`.
newline = "log line\n"
print(newline.rstrip("\n"))
print(newline.strip())
print(newline.replace("\n", ""))
print(newline[:-1])
print(newline.removeprefix("log line").removesuffix("\n"))

# 16. Count characters in a hostname.
hostname = "ubuntu"
print(len(hostname))
print(hostname.__len__())
print(sum(1 for char in hostname))
print(hostname.count(hostname))
print(hostname.encode().__len__())
print(hostname.find("u")+1)  # first occurrence
print(hostname.rfind("u")+1)  # last occurrence
print(hostname.index("u")+1)  # first occurrence
print(hostname.rindex("u")+1)  # last occurrence    
print(list(hostname).__len__())
print(tuple(hostname).__len__())

# 17. Convert environment name to uppercase.
print("environment".upper())
print("ENVIRONMENT".lower())

# 18. Check if log contains `"failed"`.
log_details = "The service is failed to start please restart the service again"
print(log_details.find("failed") != -1)
print("failed" in log_details)

# 19. Join parts of a config line.
config_parts = ["server", "port", "service"]
print(" ".join(config_parts))
print("-".join(config_parts))
print("_".join(config_parts))
print("".join(config_parts))
print("/".join(config_parts))
print("|".join(config_parts))
print(",".join(config_parts))
print("->".join(config_parts))
print("<->".join(config_parts))

# 20. Replace `"http"` with `"https"` in a URL.
url = "http://www.google.com"
print(url.replace("http", "https"))
print(url.replace("http:", "https:"))
print("https" + url[4:])
print("https" + url.partition("http")[2][4:])
print("https" + url.rpartition("http")[2][4:])
print("https" + url.split("http")[1][4:])
print("https" + url.split("http:")[1][1:])
print(url.encode().replace(b"http", b"https").decode())

#--------------------------------------------------------------------------------------------

## 🔵 LEVEL 3 – THINK LIKE A PRO (21–30)

# 21. Read log input from user and print it.
log_input = input("Enter log for details: ")
print(f"The user entered the {log_input}")

# 22. Check if user-entered string contains `"error"`.
user_input = input("Enter a string to proceed further: ")
print("error" in user_input.lower())


# 23. Normalize input (strip + lowercase).
normal = input("Enter a normal message with spacese: ")
print(normal.strip().lower())
print(normal.lstrip().lower())
print(normal.rstrip().lower())  
print(normal.encode().strip().lower().decode())


# 24. Parse `"user=root action=login"` and print user.
text = "user=root action=login"
user = text.split()[0].split("=")[1]
action = text.split()[1].split("=")[1]
print(user)
print(action)

# 25. Replace sensitive data `"password=123"` → `"password=****"`.
data = "password123"
print(data.replace("password123", "***********"))

# 26. Count how many times `"ERROR"` appears.
enter_text = input("Enter the error mesasge: ")
print(enter_text.count("error"))

'''

# 27. Extract filename from path.
file_path = "var/log/sys.log"
file_name = file_path.split("/")[2]
print(file_name)

# 28. Build a status message using f-strings.
message = "Building a docker image keep waiting,,,,."
print(f"The docker is: {message}")

# 29. Clean log text before printing.
log_text = "   ERROR: Disk space low   \n"
cleaned_log = log_text.strip()
print(cleaned_log)

# 30. Print a final automation completion message.
