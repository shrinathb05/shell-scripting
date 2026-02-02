# 🟢 LEVEL 1 – BASIC CONDITIONS (1–8)
'''
# Check if a number is greater than 10.
num1= int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))

if num1 > num2:
    print(f"The {num1} is greater than {num2}")
else:
    print(f"The {num1} is smaller than {num2}")


        
# Check if CPU usage is above 80.
CPU_USAGE = 96

if CPU_USAGE > 80:
    print(f"Warning CPU is high {95}% ..!")
else:
    print(f"CPU usage is {CPU_USAGE}% ")

# Check if service status is "running".
status = "running"
if status == "running":
    print("The service is running")
else:
    print("The service is down")

# Compare two numbers and print the bigger one.
a = int("Enter a number: ")
b = int("Enter a number: ")

if a > b:
    print(f"{a} is greater")
elif a < b:
    print(f"{b} is greater")
else:
    print(f"Both are equal")


# Check if a string equals "prod".
env = ['DEV','UAT', 'PRE-PROD', 'PROD']
enter_env = input("Enter the environment for deployment: ")

if "DEV" and "UAT" and "PRE-PROD" and "PROD" in enter_env:
    print(f"The deployment is running in {enter_env}")
else:
    print(f"Invalid Environment! ")


# Check if retry count is less than 3.
retry_count = 0 # Start at 0 attempts
max_retries = 3

while retry_count < max_retries:
        user = input("Enter the environment for testing: ")

        if user == "dev":
            print("Envronement is accepted proceeding....")
            break # This will exit the loop if got correct
        else:
            retry_count += 1 # Increment the attempt count
            remaining = max_retries - retry_count

            if remaining > 0:
                print(f"Wrong environment.... You have {remaining} attempts left.")
            else:
                print("You have reached with your limit ....")        

# Check if disk usage equals 100.
disk_usage = 98

if disk_usage >= 98:
    print(f"The Disk space is {disk_usage}% and it's fo going to be 100% very soon take action !")
else:
    print("The disk space is fine")

# Print message if value is not equal to zero.
user_input = input("Enter a number: ")
if user_input.isdigit():
    user_input = int(user_input)
    if user_input != 0:
        print(f"The Entered value {user_input} is not equal to Zero")
    else:
        print(f"The Entered value {user_input} is equal to Zero")
else:
    print("That's not even a number!")

# 🟡 LEVEL 2 – DEVOPS CONDITIONS (9–17)
# Alert if disk usage > 85.
TH = 85

if TH > 80:
    print("Alert")
else:
    print("working fine")


# Print message if service is stopped.
service = "Stopped"

if service.lower() == "stopped":
    print("Service stopped")
else:
    print("Service is running")

# Check if environment is "prod".
env = "prod"

print("Correct environment" if "prod" in env else "Wrong env")

# Check if log contains "error".
log = "Nginx is failed with Error"
print("ERROR found" if "error" in log.lower() else "Fine")

# Restart service if status != "running".
import subprocess
from datetime import time

status = subprocess.getoutput("systemctl is-active").strip()
if status != "active":
    print("Service stopped")
    print("starting the service")
else:
    print("service is running")

# Alert if CPU > 80 AND memory > 75.
cpu = 90
mem = 85

if cpu > 85 and mem > 75:
    print(f"The CPU {cpu}% and Memory {mem}% on high")
else:
    print("CPU and memory are fine")


# Skip deployment if env != "prod".
env = "UAT"

if env != "prod":
    print("Wrong environment skipping the depoyment")
else:
    print("Proceeding for deployment....")
# Alert if retries exceeded limit.
# Print success if exit code == 0.
exit_code = 3
if exit_code != 0:
    print("Failuer")
else:
    print("succss")


# 🔵 LEVEL 3 – PRODUCTION LOGIC (18–25)
# Check multiple service statuses.
#!/usr/bin/python3
import subprocess
import time
services = ["nginx", "ssh", "cron"]

for service in services:
    # Check the status of the specific services
    status = subprocess.getoutput(f"systemctl is-active {service}")

    if status != "active":
        print(f"Service one of service {service} is down! Attempting to start...")
        time.sleep(2)
        subprocess.getoutput(f"systemctl start {service}")

        # Verify if it started
        new_status = subprocess.getoutput(f"systemctl is-active {service}")
        print(f"Service {services} is no {new_status}")
    else:
        print(f"Service {service} working fine")
    '''
# Decide backup based on day.
BACKUP_OPTIONS = ["DAY", "WEEK", "MONTH", "QUATERLY","HALF-QUATERLY" "YEARLY"]
user_input = input("Enter the day to take backup: ").strip().upper()

if user_input in BACKUP_OPTIONS:
    if user_input == "DAY":
        print("Taking daily backup !!")
    elif user_input == "WEEK":
        print("Taking weekly backup !!")
    elif user_input == "MONTH":
        print("Taking monthly backup !!")
    elif user_input == "QUARTERLY":
        print("Taking quarterly backup !!")
    # ... and so on
else:
    # This triggers if the user types something not in the list
    print("Invalid option. Initial backup started....")

# OPTIONS 2
#!/usr/bin/python3

# 1. Define all possible actions in one place
# Note: Fixed the missing comma and the spelling of QUARTERLY
backup_messages = {
    "DAY": "Taking daily backup !!",
    "WEEK": "Taking weekly backup !!",
    "MONTH": "Taking monthly backup !!",
    "QUARTERLY": "Taking quarterly backup !!",
    "HALF-QUARTERLY": "Taking half-quarterly backup !!",
    "YEARLY": "Taking yearly backup !!"
}

user_input = input("Enter the day to take backup: ").strip().upper()

# 2. Use .get() to find the message or provide the default "Initial backup"
message = backup_messages.get(user_input, "Initial backup started....")

print(message)

# ---------------------------------------------------------------
# OPTION 3 Prodcution like
#!/usr/bin/python3
import tarfile
import os
from datetime import datetime

# Configuration
SOURCE_DIR = "/var/www/html"  # Folder to back up
BACKUP_DEST = "/backups"      # Where to save the zip
BACKUP_OPTIONS = ["DAY", "WEEK", "MONTH", "QUARTERLY", "YEARLY"]

user_input = input("Enter backup frequency (DAY/WEEK/MONTH): ").strip().upper()

if user_input in BACKUP_OPTIONS:
    # 1. Generate filename: e.g., backup_DAY_2026-02-03.tar.gz
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_name = f"backup_{user_input}_{date_str}.tar.gz"
    final_path = os.path.join(BACKUP_DEST, file_name)

    print(f"Starting {user_input} backup of {SOURCE_DIR}...")

    try:
        # 2. Create the compressed tarball
        with tarfile.open(final_path, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        
        print(f"Success! Backup saved to: {final_path}")
    except PermissionError:
        print("Error: You need root/sudo privileges to back up these files!")
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print("Invalid option. No backup performed.")


# production ready

#!/usr/bin/python3
import os
import tarfile
import time
from datetime import datetime

# --- Configuration ---
SOURCE_DIR = "/var/www/html"
BACKUP_DEST = "/backups"
RETENTION_DAYS = 30
SECONDS_IN_DAY = 86400  # 24 * 60 * 60

# --- 1. Identify Action ---
backup_messages = {
    "DAY": "Taking daily backup !!",
    "WEEK": "Taking weekly backup !!",
    "MONTH": "Taking monthly backup !!"
}

user_input = input("Enter backup frequency: ").strip().upper()
print(backup_messages.get(user_input, "Initial backup started...."))

# --- 2. Perform Backup ---
if not os.path.exists(BACKUP_DEST):
    os.makedirs(BACKUP_DEST)

date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
file_name = f"backup_{user_input}_{date_str}.tar.gz"
final_path = os.path.join(BACKUP_DEST, file_name)

with tarfile.open(final_path, "w:gz") as tar:
    tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
print(f"Backup created: {final_path}")

# --- 3. Clean up Old Backups ---
print(f"Cleaning up files older than {RETENTION_DAYS} days...")
current_time = time.time()

for file in os.listdir(BACKUP_DEST):
    file_path = os.path.join(BACKUP_DEST, file)
    
    # Check if it's a file (not a folder)
    if os.path.isfile(file_path):
        file_age_seconds = os.path.getmtime(file_path)
        
        # Calculate age in days
        if (current_time - file_age_seconds) > (RETENTION_DAYS * SECONDS_IN_DAY):
            print(f"Deleting expired backup: {file}")
            os.remove(file_path)

print("Maintenance complete.")
