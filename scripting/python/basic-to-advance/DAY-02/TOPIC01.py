# 🔹 TOPIC 1: Comparison Operators (FOUNDATION)
# Operator	Meaning	Example
# ==	equal	        status == "running"
# !=	not equal	    env != "prod"
# >	    greater	c       pu > 80
# <	    less	        disk < 20
# >=	greater/equal	memory >= 70
# <=	less/equal	    retries <= 3

# Example Usage:
cpu_usage = 85
print(f"Is CPU usage greater than 80%? {cpu_usage > 80}")

# Check if environment is not production
environment = "staging"
print(f"Is the environment not production? {environment != 'prod'}")
# Check if memory usage is less than or equal to 70%
memory_usage = 65
print(f"Is memory usage less than or equal to 70%? {memory_usage <= 70}")
# Check if disk space is equal to 20%
disk_space = 20
print(f"Is disk space equal to 20%? {disk_space == 20}")
# Check if retries are greater than or equal to 3
retries = 4
print(f"Are retries greater than or equal to 3? {retries >= 3}")
# Check if status is not equal to "running"
status = "stopped"
print(f"Is status not equal to 'running'? {status != 'running'}")
# Check if disk space is less than 50%
disk_space = 45
print(f"Is disk space less than 50%? {disk_space < 50}")
# Check if CPU usage is less than or equal to 90%
cpu_usage = 90
print(f"Is CPU usage less than or equal to 90%? {cpu_usage <= 90}")
# Check if environment is equal to "dev"
environment = "dev"
print(f"Is the environment equal to 'dev'? {environment == 'dev'}")
# Check if memory usage is greater than 80%
memory_usage = 75
print(f"Is memory usage greater than 80%? {memory_usage > 80}")
# Check if retries are not equal to 5
retries = 5
print(f"Are retries not equal to 5? {retries != 5}")    
# Check if status is equal to "running"
status = "running"
print(f"Is status equal to 'running'? {status == 'running'}")
# Check if disk space is greater than or equal to 30%
disk_space = 35
print(f"Is disk space greater than or equal to 30%? {disk_space >= 30}")
# Check if CPU usage is not equal to 100%
cpu_usage = 95
print(f"Is CPU usage not equal to 100%? {cpu_usage != 100}")
# Check if environment is less than "test" (lexicographical comparison)
environment = "dev"
print(f"Is the environment less than 'test'? {environment < 'test'}")
# Check if memory usage is greater than or equal to 60%
memory_usage = 60
print(f"Is memory usage greater than or equal to 60%? {memory_usage >= 60}")
# Check if retries are less than 10
retries = 8
print(f"Are retries less than 10? {retries < 10}")
# Check if status is not equal to "stopped"
status = "running"
print(f"Is status not equal to 'stopped'? {status != 'stopped'}")
# Check if disk space is equal to 100%
disk_space = 100
print(f"Is disk space equal to 100%? {disk_space == 100}")
# Check if CPU usage is greater than or equal to 50%
cpu_usage = 55
print(f"Is CPU usage greater than or equal to 50%? {cpu_usage >= 50}")
# Check if environment is equal to "prod"
environment = "prod"
print(f"Is the environment equal to 'prod'? {environment == 'prod'}")
# Check if memory usage is less than 40%
memory_usage = 35
print(f"Is memory usage less than 40%? {memory_usage < 40}")
# Check if retries are greater than 2
retries = 3
print(f"Are retries greater than 2? {retries > 2}")
# Check if status is equal to "paused"  
status = "paused"
print(f"Is status equal to 'paused'? {status == 'paused'}")
# Check if disk space is not equal to 75%
disk_space = 80
print(f"Is disk space not equal to 75%? {disk_space != 75}")
# Check if CPU usage is less than 70%
cpu_usage = 65
print(f"Is CPU usage less than 70%? {cpu_usage < 70}")
# Check if environment is greater than "dev" (lexicographical comparison)
environment = "staging"
print(f"Is the environment greater than 'dev'? {environment > 'dev'}")
# Check if memory usage is equal to 90%
memory_usage = 90
print(f"Is memory usage equal to 90%? {memory_usage == 90}")
# Check if retries are less than or equal to 4
retries = 4
print(f"Are retries less than or equal to 4? {retries <= 4}")
# Check if status is greater than "idle" (lexicographical comparison)
status = "running"
print(f"Is status greater than 'idle'? {status > 'idle'}")

