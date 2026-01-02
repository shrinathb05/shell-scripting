
# topic 1
cpu_usage = 50
print(cpu_usage > 34)

# topic 2
disk_usage = 90
if disk_usage > 90:
	print(f"The Disk space is greter than {disk_usage} kindly check !!")

# 4 if-else

service_status = "running"

if service_status == "running":
	print("Service is up and running!!!")
else:
	print("Service is not running kindly check !!")

# 5.
cpu = 95
if cpu < 50:
	print("CPU is normal")
elif cpu < 80:
	print("CPU is high")
else:
	print("CPU is critical please check !!!")

# 6 Logical Operator
env = "prod"
cpu = 90

if env == "prod" and cpu > 80:
	print("Critical Alert !: need to check asap")
	
# Real scenario example
log = "ERROR: nginx stopped"

if "error" in log.lower():
	print("Alert: Issue is there in logs")
else:
	print("System is normal")

#-----------------------------------------------------------------------------------------

# ## 🟢 LEVEL 1 – BASIC CONDITIONS (1–8)

# 1. Check if a number is greater than 10.
a = 16
b = 10
if a > b:
	print(f"The number {a} is greater than {b}")
else:
	print(f"The number {a} is less than {b}")

# 2. Check if CPU usage is above 80.
cpu_usage = 80
if cpu_usage > 80:
	print(f"It's critical the cpu is reached at {cpu_usage}% is in critical condition")
else:
	print("System is working fine")

# 3. Check if service status is `"running"`.
service = "running"
if service == "running":
	print("The service is running")
else:
	print("The service is not running")

# 4. Compare two numbers and print the bigger one.
a = 5
b = 25

if a > b:
	print(f"{a} is greater than {b}")
else:
	print(f"{b} is greater than {a}")
	
# 5. Check if a string equals `"prod"`.
env = "prod"

if env == "prod":
	print(f"Then the selected environment is {env}")


# 6. Check if retry count is less than 3.
retry_count = 3
if retry_count < 3:
	print(f"The Retry count {retry_count} is remaing try again.....")
else:
	print(f"You have reached with the limit..")


# 7. Check if disk usage equals 100.
disk_usage = 90
if disk_usage == 100:
	print(f"The disk space is {disk_usage} and is equal to 100")
else:
	print(f"The disk space is {disk_usage} and is not equal to 100")


# 8. Print message if value is not equal to zero.

if x != 0:
	print(f"The value {x} is not equal to zero")
else:
	print(f"The value {x} is equal to zero")

# ---

# ## 🟡 LEVEL 2 – DEVOPS CONDITIONS (9–17)

# 9. Alert if disk usage > 85.
disk_usage = 90
if disk_usage > 85:
	print(f"The disk space is beyond {85}% kindly reduce the space")
else:
	print("The disk space is normal")


# 10. Print message if service is stopped.
service = "stopped"
if service == "stopped":
	print(f"The service is nor running")
else:
	print("The service is working fine")


# 11. Check if environment is `"prod"`.
env = "prod"
if env == "prod":
	print("You selected the correct environment")
else:
	print("You selected the wrong environment")

# 12. Check if log contains `"error"`.
log = "ERROR: Alert! please check"
if "error" in log.lower():
	print("There is an error need to check the system asap")
else:
	print("The system is workign fine")

# 13. Restart service if status != `"running"`.
service = "stopped"
if service != "running":
	print("The service is not running. Starting service..........")
else:
	print("The service is up and running")

# 14. Alert if CPU > 80 AND memory > 75.
cpu = 90
mem = 85

if cpu > 80 and mem > 75:
    print("ALERT: CPU and Memory are high")
else:
    print("System is stable")

# 15. Skip deployment if env != `"prod"`.
env = "prod"

if env == "prod":
	print("selected the correct environment, Starting with the deployment.....")
else:
	print("selected the correct environment.....!")



# 16. Alert if retries exceeded limit.
retry_count = 5
if retry_count > 4:
	print("You reached with your limit...")
else:
	print("TRY AGAIN!...")

# 17. Print success if exit code == 0.
exit_code = 0
if exit_code !=0:
	print("Failure! Alert!...")
else:
	print("SUCCESSFULLY DEPLOYED...")


# ---

# ## 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)

# 18. Check multiple service statuses.
service1 = 'Running'
service2 = 'Started'
service3 = 'Stopped'

if service1 != "Running" or service2 != "Started" or service3 != 'Stopped':
	print("One or more services are down")
else:
	print("All service is running..")

# 19. Decide backup based on day.
day = "sunday"
if day == "sunday":
	print(f"today is {day} performing weekly backup")
else:
	print("Performing the daily incremental backup")

# 20. Alert if log contains `"ERROR"` or `"FAILED"`.
log = "ERROR: Deployment FAILED"
if "error" in log.loewr() or "failed" in log.lower():
	print("ALERT! issue found in logs")

# 21. Validate username input.
user = input("Enter your name: ").strip()
if user:
	print(f"Hi! {user}, Welcome to our team")
else:
	print("Invalid username")

# 22. Block script if environment is `"test"`.
env = "prod"
if env == "test":
	print("The selected env is test environment blocking the script execution.......")
else:
	print("The selected environment is prod proceeding with script execution....")

# 23. Decide scaling based on CPU.
cpu_usage = 85
if cpu_usage > 80:
	print("The CPU is high! please check as soon as possible ............!")
else:
	print("The CPU is fine no need of scaling")

# 24. Perform action only if user confirms `"yes"`.
user = input("Write your answer in Yes/No: ")
if user.lower() == "yes":
	print(f"The user given {user} answer and it;s correct")
else:
	print(f"The user given {user} answer and it;s not correct")

# 25. Print final status based on multiple conditions.

cpu = 80
mem = 75
disk = 85

if cpu < 85 and mem < 80 and disk < 90:
	print("The all services are working fine")
else:
	print("Form the 3 services any one is in critical condition")
# ---
