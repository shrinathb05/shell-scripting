# checking the nginx service is running or not then restarting it

import random
import time

'''
# List of servers we want to manage
SERVERS = {
    "Web-Server-01": "192.168.1.10",
    "DB-Server-01": "192.168.1.11",
    "Load-Balancer": "192.168.1.12",
    "Backup-Node": "192.168.1.13",
    "Cache-Master": "192.168.1.14"
}

# Convert keys to a list and shuffle them
server_names = list(SERVERS.keys())
random.shuffle(server_names)

# Pick one server that "needs" a restart (like your LUCKY vaccine)
TARGET_SERVER = random.choice(server_names)

print(f"--- Starting Global Infrastructure Audit ---")
print(f"Target system for maintenance today: {TARGET_SERVER}\n")

for name in server_names:
    ip = SERVERS[name]
    print(f"Connecting to {name} [{ip}]...")
    time.sleep(0.5)  # Simulating network latency
    
    if name == TARGET_SERVER:
        print("##############################################")
        print(f"CRITICAL: Service on {name} is DOWN!")
        print(f"ACTION: Executing 'sudo systemctl restart nginx'...")
        print(f"STATUS: {name} is now BACK ONLINE.")
        print("##############################################\n")
    else:
        print("----------------------------------------------")
        print(f"STATUS: {name} is running normally.")
        print("----------------------------------------------\n")

print("Audit Complete.")

'''

'''

import subprocess

# Define your server fleet
SERVERS = [
    {"name": "Web-01", "ip": "192.168.1.10"},
    {"name": "Web-02", "ip": "192.168.1.11"},
    {"name": "DB-Main", "ip": "192.168.1.20"},
    {"name": "App-Server", "ip": "192.168.1.30"}
]

SERVICE = "nginx"

def check_and_restart_all():
    print(f"--- Beginning System-Wide Check for {SERVICE} ---\n")
    
    for server in SERVERS:
        print(f"Checking {server['name']} ({server['ip']})...")
        
        # In a real scenario, this command would be sent via SSH
        # Example command: ssh user@ip "systemctl is-active nginx"
        ssh_command = ["ssh", f"admin@{server['ip']}", f"systemctl is-active {SERVICE}"]
        
        try:
            # Check status
            status = subprocess.run(ssh_command, capture_output=True, text=True)
            current_state = status.stdout.strip()

            if current_state == "active":
                print(f"  [OK] {server['name']} is healthy.")
            else:
                print(f"  [ALERT] {server['name']} is {current_state}! Restarting...")
                # Run restart command
                subprocess.run(["ssh", f"admin@{server['ip']}", f"sudo systemctl restart {SERVICE}"])
                print(f"  [FIXED] {SERVICE} restarted on {server['name']}.")
                
        except Exception as e:
            print(f"  [ERROR] Could not connect to {server['name']}: {e}")
        
        print("-" * 40)

if __name__ == "__main__":
    check_and_restart_all()
'''

# 1. Define your list of servers
SERVERS = ["Web-Server-01", "Web-Server-02", "Database-01", "Cache-Node"]

# 2. Define the service we are looking for
SERVICE = "Nginx"

print("--- STARTING SYSTEM CHECK ---")

# 3. Loop through EVERY server (no randomness)
for server in SERVERS:
    print(f"Checking {server}...")

    # For this example, let's pretend Web-Server-02 is the one that is down
    if server == "Web-Server-02":
        status = "INACTIVE"
    else:
        status = "ACTIVE"

    # 4. Logic to handle the status
    if status == "ACTIVE":
        print(f"  [OK] {SERVICE} is running fine.")
    else:
        print(f"  [!] ALERT: {SERVICE} is DOWN on {server}!")
        print(f"  [>] Running command: sudo systemctl restart {SERVICE}")
        print(f"  [+] {server} has been RESTARTED.")
    
    print("------------------------------")

print("--- ALL SERVERS CHECKED ---")