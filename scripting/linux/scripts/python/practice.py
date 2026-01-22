# 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)
# Check multiple service statuses.
service = ["running", "stopped", "initated"]

if "initated" in service:
	print('The service is started')
elif "running"in service:
	print("The service is running!!!")
elif "stopped" in service:
	print("The service is stopped!!!")
else:
	print("The service is not showing any status")

# Decide backup based on day.
day = "monday"
if day == "monday":
	print("Taking the weekly backup...")
else:
	print("Takind the incremental backup")

# Alert if log contains "ERROR" or "FAILED".
log = "Alert there is ERROR is the failed logs"
if "error" in log.lower() or "failed" in log.lower():
	print("There is issue with the system please check...!")
else:
	print("The system is working fine")

# Validate username input.
user = input("enter the username: ")
if user:
	print(f"Hi {user}, Welcome to the journey")
else:
	print("invalid username !")

# Block script if environment is "test".
env = "prod"
if env == "test":
	print("The environment is test so blocking the script eecution")
else:
	print("This is prod environment proceeding with the script execution")

# Decide scaling based on CPU.
cpu = 80
if cpu > 80:
	print("The cpu is critical state!")
else:
	print("The system is fine")

# # Perform action only if user confirms "yes".
# user = input("Please provide your confirmaton: ")
# if user == "yes".lower():
# 	print("This is correct username")
# else:
# 	print("Invalid username")

# # Print final status based on multiple conditions.

# num = int(input("Enter a number: "))
# print("Even" if num%2==0 else "Odd")

print("even" if 4%2==0 else "odd")