# 🧪 DAY 1 PRACTICE – 20 EXERCISES

# ⚠️ You MUST write scripts for each. No shortcuts.

# 🟢 LEVEL 1 – BASIC LOGIC (1–7)

# Create a script that prints your name and role as "DevOps Engineer".
name="Shrinath"
role="Devops Engineer"
print(f"My name is {name} and my role is {role}.")
# Store a server name in a variable and print it.
server_name="server01"
print(f"The server name is {server_name}.")

# Store CPU usage as a number and print it.
cpu_usage=75
print(f"The current CPU usage is {cpu_usage}%.")
# Print the data type of:
    # a string
    # an integer
string_example="Hello, shri"
interger_example=42
print(f"The data type of string_example is {type(string_example)}.")
print(f"The data type of interger_example is {type(interger_example)}.")

# Take user input for username and print a welcome message.
username=input("Enter your username: ")
print(f"Welcome, {username}!")

# Store today’s task (string) and print it.
today_task="Monitor server health"
print(f"Today's task is: {today_task}")

# Store True in a variable called server_up and print it.
server_up=True
print(f"Is the server up? {server_up}")

# 🟡 LEVEL 2 – INTERMEDIATE LOGIC (8–14)
# Take user input for two numbers and print their sum.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum_result=num1+num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
# Take user input for two numbers and print their product.
num3=int(input("Enter first number: "))
num4=int(input("Enter second number: "))
product_result=num3*num4
print(f"The product of {num3} and {num4} is {product_result}.")
# Store a float value representing memory usage and print it.
memory_usage=65.5
print(f"The current memory usage is {memory_usage}%.")
# Take user input for a server status (string) and print it.
server_status=input("Enter the server status: ")
print(f"The server status is: {server_status}")
# Store False in a variable called maintenance_mode and print it.
maintenance_mode=False
print(f"Is maintenance mode enabled? {maintenance_mode}")
# Take user input for a file name and print it with ".log" extension.
file_name=input("Enter the file name: ")
log_file=f"{file_name}.log"
print(f"The log file name is: {log_file}")
# Store the number of active connections (integer) and print it.
active_connections=120
print(f"The number of active connections is: {active_connections}")     

# Store:
# hostname
# IP address
# Print them in one line.
hostname="server01"
ip_address="192.168.1.100"
print(f"Hostname: {hostname}, IP Address: {ip_address}")
# Store disk usage percentage and print:
# Disk usage is 70%
disk_usage=70
print(f"Disk usage is {disk_usage}%")           
# Store number of running containers and print it.
running_containers=5
print(f"Number of running containers: {running_containers}")
# Ask user for environment name (dev/prod) and print it.
environment=input("Enter environment name (dev/prod): ")
print(f"Environment is: {environment}")
# Store log file path and print it.
log_file_path="/var/log/app.log"
print(f"Log file path is: {log_file_path}")
# Store backup status (True or False) and print it.
backup_status=True
print(f"Backup status is: {backup_status}")
# Store retry count and print it.
retry_count=3
print(f"Retry count is: {retry_count}")

# Store API endpoint URL and print it.
api_endpoint="https://api.example.com/v1/resource"
print(f"API endpoint URL is: {api_endpoint}")
# Store server uptime in hours and print it.
server_uptime=240
print(f"Server uptime is: {server_uptime} hours")   
# Store SSL certificate status (valid/expired) and print it.
ssl_certificate_status="valid"
print(f"SSL certificate status is: {ssl_certificate_status}")
# Store number of failed login attempts and print it.
failed_login_attempts=2
print(f"Number of failed login attempts: {failed_login_attempts}")
# Store system load average and print it.
system_load_average=1.5
print(f"System load average is: {system_load_average}")
# Store firewall status (enabled/disabled) and print it.
firewall_status="enabled"
print(f"Firewall status is: {firewall_status}")
# Store database connection string and print it.
db_connection_string="Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword;"
print(f"Database connection string is: {db_connection_string}")
# Store email server address and print it.
email_server_address="smtp.example.com"
print(f"Email server address is: {email_server_address}")
# Store scheduled task time and print it.
scheduled_task_time="02:00 AM"
print(f"Scheduled task time is: {scheduled_task_time}")
# Store system timezone and print it.
system_timezone="UTC"
print(f"System timezone is: {system_timezone}")

# Level 3 THINK LIKE A SCRIPT and ADVANCED LOGIC (15–20)
# Take user input for a server name and port number, then print them in the format "server_name:port".
server_name=input("Enter server name: ")
port_number=input("Enter port number: ")
print(f"{server_name}:{port_number}")

# Take user input for a username and domain, then print the email in the format "username@domain.com".
username=input("Enter username: ")
domain=input("Enter domain: ")
print(f"{username}@{domain}")

# Take user input for a file name and extension, then print the full file name.
file_name=input("Enter file name: ")
extension=input("Enter file extension: ")
print(f"{file_name}.{extension}")

# Take user input for a first name and last name, then print the full name.
first_name=input("Enter first name: ")
last_name=input("Enter last name: ")        
print(f"{first_name} {last_name}")

# Take user input for a city and country, then print them in the format "city, country".
city=input("Enter city: ")
country=input("Enter country: ")
print(f"{city}, {country}")

# Take user input for a product name and price, then print them in the format "product: $price".
product_name=input("Enter product name: ")
price=input("Enter price: ")
print(f"{product_name}: ${price}")

# Take user input for three variables and print them in a formatted message.
var1=input("Enter first variable: ")
var2=input("Enter second variable: ")
var3=input("Enter third variable: ")
print(f"Variables are: {var1}, {var2}, {var3}") 

# Store service name and its status and print both.
service_name="nginx"
service_status="running"
print(f"Service name: {service_name}, Status: {service_status}")

# Store memory usage as float and print it.
memory_usage=81.5
print(f"Memory usage is: {memory_usage}%")

# Print a formatted message using f-string with 3 variables.
name="Alice"
age=30
city="New York"
print(f"Name: {name}, Age: {age}, City: {city}")

# Print a startup message:
startup_message="System started successfully."
print(startup_message)

# Store a boolean indicating if the server is active and print it.
server_active=True
print(f"Is the server active? {server_active}") 
# Store a float representing temperature and print it.
temperature=36.6
print(f"Current temperature is: {temperature}°C")