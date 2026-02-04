#!/bin/bash

# Syntax of CASE

# case $variable in
#     option1)
#         command ;;
#     option1)
#         command ;;
#     option1)
#         command ;;
#     *)
#     default commands ;;
# esac

# Simple example
read -p "Enter a number from (1-3): " num

case $num in
    1) echo "You choose One" ;;
    2) echo "You choose Two" ;;
    3) echo "You choose Three" ;;
    *) echo "Invalid choice" ;;
esac

echo "-----------------------------------------------------------------------------"
echo "-----------------------------------------------------------------------------"

# Example 1 OS information tool

echo "1. Hostname"
echo "2. Uptime"
echo "3. list files"
echo "4. Disk Usage"
echo "5. Mem Usage"
echo "6. Machine Name"
echo "7. Exit."

read -p "Chosse any option to check the OS information: " opt

case $opt in
    1) Hostname ;;
    2) uptime -p ;;
    3) ls -lrt ;;
    4) df -h ;;
    5) free -mh ;;
    6) uname ;;
    7) exit 0 ;;
    *) echo "Invalid Option !"


# Service control script

read -p "Enter Service Name: " service
read -p "Action (start|stop|status|restart|enable): " action

case $action in
    start) systemctl start "$service" ;;
    stop) systemctl stop "$service" ;;
    status) systemctl status "$service" ;;
    restart) systemctl restart "$service" ;;
    enable) systemctl enable "$service" ;;
    *) echo "Invalid Option " exit 0 ;;
esac


# function + CASE

disk() {df -h}
mem() {free -mh}
uptime_info() {uptime -p}

read -p "Enter yout choice(disk/mem/uptime): " choice

case $choice in
    disk) disk ;;
    mem) mem ;;
    up) uptime_info ;;
    *) echo "Invalid Option !"
esac

# Menu to show current user directory and date
echo "1. Current User"
echo "2. Date "
echo "3. Current Directory "

read -p "Enter to check (user/date/dir): " choice

case $choice in
    1) whoami ;;
    2) date ;;
    3) pwd ;;
    *) echo "Invalid Option" exit 0


# Calculator of 2 numbers

read -p "Enter first nummber: " a
read -p "Enter second nummber: " b
read -p "Operation (add/sub/mul/div/): " opt

case $opt in
    Add) echo "Result: $((a+b))"
    Sub) echo "Result: $((a-b))"
    Mul) echo "Result: $((a*b))"
    Div) echo "Result: $((a/b))"
    *) echo "Invalid Option !" exit 0
esac


# OS command selector

read -p "Select a command to check output (ls/pwd/user): " cmd

case $cmd in
    1) ls ;;
    2) pwd ;;
    3) whoami ;;
    *) echo "Invalid Option!" exit 0
esac

# Service Manager

read -p "Enter Service Name: " service
read -p "Action (start/stop/restart/status/enable): " action

case $action in
    Start) sudo systemctl start "${service}" ;;
    Stop) sudo sustemctl stop "${service}" ;;
    Restart ) sudo sustemctl restart "${service}" ;;
    Status) sudo sustemctl status "${service}" ;;
    Enable) sudo sustemctl enable "${service}" ;;
    *) echo "Invalid Option!" exit 0
esac



# USER Operation Menu
echo "1. List Users:"
echo "2. Count Users: "

read -p "Choose: " opt

case $opt in
    1) cut -d: -f1 /etc/passwd | tail -5 ;;
    2) cut -d: -f1 /etc/passwd | wc -l ;;
    *) echo "Invalid " ;;
esac

# network Info Menu

echo "1. IP Address "
echo "2. Routing Tables "
echo "3. DNS "

read -p "Choose: " net

case $net in
    1) ip a ;;
    2) ip route ;;
    3) cat /etc/resolv.conf ;;
    *) echo "Invalid ! " ;;
esac


# 11. Menu-Based Backup Tool
read -p "Enter a directory to take backup: " src
bkp_dir="/var/backup_$(date +%F_%H_%M)"

case $src in
    *)
        cp -r "$src" "$bkp_dir"
        echo "Backup completed to: $bkp_dir"
        ;;
esac


# Log analysis menu

# Variables of file
log_file_1="/var/log/syslog"
log_file_2="/var/log/auth.log"


# Options
# Options
echo "--------------------------"
echo "   LOG ANALYSIS TOOL"
echo "--------------------------"
echo "1. Show Critical Errors (syslog)"
echo "2. Show Warnings (syslog)"
echo "3. Show SSH Login Attempts (auth.log)"
echo "4. Exit."

# Taking user input
read -p "Select an option [1-4]: " logopt

if [ ! -f $log_file_1 ];then
    echo "Error: $log_file_1 not found"
    exit 1
fi

case $logopt in
    1) 
        echo "Searching for ERRORS......"
        grep -iE "ERROR|CRITICAL" "$log_file_1" | tail -n 5
        ;;
    2)  
        echo "Searching for WARNINGS........"
        grep -iE "WARNING" "$log_file_1" | tail -n 5
        ;;
    3)
        echo "Searching SSH logs......"
        grep "sshd" "$log_file_2" | tail -n 5 
        ;;
    4)
        echo "Exiting......"
        exit 0
        ;;    
    *) 
        echo "Invalid Option" 
        exit 1
        ;;
esac


# 13. Cleanup Tool

# directorys
dir1="/tmp/logs"
dir2="/var/log"

if [ ! -d $dir1 ];then
    echo "Error: $dir1 not found !.."
    exit 1
fi

echo "1. Clean Logs From (/tmp/logs) Directory"
echo "2. Remove Old Logs"
echo "3. Exit."

read -p "Select an option [1-3]: " opt

case $opt in
    1)
        # The Confirmation Gate
        read -p "WARNING: This will delete ALL files in $dir1. Are you sure? [y/N]: " confirm
        if [[ "$confirm" =~ ^[Yy]$ ]]; then
            echo "Cleaning $dir1..."
            rm -rf "${dir1:?}"/*
            echo "Files deleted."
            echo "$(date): User $USER deleted files in $dir1" >> /var/log/cleanup_history.log
        else
            echo "Operation cancelled."
        fi
        ;;
    2)
        read -p "Delete logs older than 7 days in $dir2? [y/N]: " confirm
        if [[ "$confirm" =~ ^[Yy]$ ]]; then
            find "$dir2" -type f -mtime +7 -name "*.log" -delete
            echo "Old logs removed."
            echo "$(date): User $USER deleted files in $dir2" >> /var/log/cleanup_history.log
        else
            echo "Operation cancelled."
        fi
        ;;
    3)
        exit 0 ;;
    *)
        echo "Invalid Option!" exit 1 ;;
esac  

# 14. Server Info Dashboard

#!/bin/bash

# --- Colors ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

while true; do
    clear
    echo -e "${BLUE}====================================================${NC}"
    echo -e "          LIVE SERVER MONITOR (2s Refresh)          "
    echo -e "          Last Update: $(date +'%H:%M:%S')          "
    echo -e "${BLUE}====================================================${NC}"

    # 1. System Load
    LOAD=$(uptime | awk -F'load average:' '{ print $2 }' | cut -d, -f1)
    echo -e "${GREEN}[+] CPU Load:${NC} $LOAD"

    # 2. Zombie Processes Logic
    # 'Z' status in ps indicates a zombie
    ZOMBIES=$(ps aux | awk '{if ($8=="Z") print $0}' | wc -l)
    if [ "$ZOMBIES" -gt 0 ]; then
        echo -e "${RED}[!] Zombie Processes:${NC} $ZOMBIES (Action Required)"
    else
        echo -e "${GREEN}[+] Zombie Processes:${NC} 0"
    fi

    # 3. Running Services (Total)
    # Counts active services using systemctl
    RUNNING_SERVICES=$(systemctl list-units --type=service --state=running --no-legend | wc -l)
    echo -e "${GREEN}[+] Active Services:${NC} $RUNNING_SERVICES"

    # 4. Critical Service Check (Example: SSH)
    # systemctl is-active --quiet ssh
    # if [ $? -eq 0 ]; then
    #     echo -e "${GREEN}[+] SSH Service:${NC} RUNNING"
    # else
    #     echo -e "${RED}[!] SSH Service:${NC} DOWN"
    # fi

    # --- Array of services you want to monitor ---
    SERVICES=("nginx" "cron" "apache2" "ssh" "mysql")

    echo -e "${YELLOW}--- Service Status Check ---${NC}"

    for SERVICE in "${SERVICES[@]}"; do
        # Check if the service is active
        systemctl is-active --quiet "$SERVICE"
        
        if [ $? -eq 0 ]; then
            # Service is running
            printf "%-15s : ${GREEN}[RUNNING]${NC}\n" "$SERVICE"
        else
            # Service is down or not installed
            printf "%-15s : ${RED}[DOWN/NOT FOUND]${NC}\n" "$SERVICE"
        fi
    done


    # 5. Memory & Disk
    MEM=$(free -m | awk '/Mem:/ {printf "%d/%dMB", $3, $2}')
    DISK=$(df -h / | awk 'NR==2 {print $5}')
    echo -e "${GREEN}[+] Memory:${NC} $MEM"
    echo -e "${GREEN}[+] Disk Usage:${NC} $DISK"

    echo -e "${BLUE}====================================================${NC}"
    echo "Press [CTRL+C] to stop the monitor..."
    
    sleep 2
done

# Optinon 2 fully

#!/bin/bash

# --- Configuration ---
ADMIN_EMAIL="shrinath7028@gmail.com"
MAX_RETRIES=3
LOG_FILE="/var/log/service_healer.log"
SERVICES=("nginx" "cron" "apache2" "ssh" "mysql")

# --- Colors ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

# 1. Logic: Declare Associative Array OUTSIDE the loop
# This ensures it remembers how many times it tried to restart a service
declare -A RETRY_COUNT
for S in "${SERVICES[@]}"; do RETRY_COUNT[$S]=0; done

# Check for root (Needed to restart services)
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}Error: This script must be run as root (sudo) to repair services!${NC}"
   exit 1
fi

# --- Function: Send Email Alert ---
send_alert() {
    local SERVICE=$1
    local SUBJECT="CRITICAL: $SERVICE Failed on $(hostname)"
    local BODY="The monitor attempted to restart $SERVICE $MAX_RETRIES times, but it is still DOWN. Manual intervention required."
    echo "$BODY" | mail -s "$SUBJECT" "$ADMIN_EMAIL"
    echo "$(date): Alert sent for $SERVICE" >> "$LOG_FILE"
}

while true; do
    clear
    echo -e "${BLUE}====================================================${NC}"
    echo -e "         LIVE SELF-HEALING SERVER MONITOR           "
    echo -e "         Last Update: $(date +'%H:%M:%S')           "
    echo -e "${BLUE}====================================================${NC}"

    # --- System Stats ---
    LOAD=$(uptime | awk -F'load average:' '{ print $2 }' | cut -d, -f1)
    ZOMBIES=$(ps aux | awk '{if ($8=="Z") print $0}' | wc -l)
    
    echo -e "${GREEN}[+] CPU Load:${NC} $LOAD"
    if [ "$ZOMBIES" -gt 0 ]; then
        echo -e "${RED}[!] Zombie Processes: $ZOMBIES${NC}"
    else
        echo -e "${GREEN}[+] Zombie Processes: 0${NC}"
    fi

    echo -e "\n${YELLOW}%-15s %-15s %-10s${NC}" "SERVICE" "STATUS" "ACTION"
    echo -e "${BLUE}----------------------------------------------------${NC}"

    # --- Service Monitoring & Repair Logic ---
    for SERVICE in "${SERVICES[@]}"; do
        systemctl is-active --quiet "$SERVICE"
        
        if [ $? -eq 0 ]; then
            RETRY_COUNT[$SERVICE]=0  # Reset counter if healthy
            printf "%-15s ${GREEN}%-15s${NC} %-10s\n" "$SERVICE" "[RUNNING]" "None"
        else
            COUNT=${RETRY_COUNT[$SERVICE]}

            if [ "$COUNT" -lt "$MAX_RETRIES" ]; then
                printf "%-15s ${RED}%-15s${NC} ${YELLOW}%-10s${NC}\n" "$SERVICE" "[DOWN]" "RESTARTING"
                systemctl restart "$SERVICE" >> "$LOG_FILE" 2>&1
                ((RETRY_COUNT[$SERVICE]++))
                echo "$(date): Restarting $SERVICE (Attempt $((COUNT+1)))" >> "$LOG_FILE"
                
            elif [ "$COUNT" -eq "$MAX_RETRIES" ]; then
                printf "%-15s ${RED}%-15s${NC} ${RED}%-10s${NC}\n" "$SERVICE" "[FAILED]" "ALERTING"
                send_alert "$SERVICE"
                ((RETRY_COUNT[$SERVICE]++)) # Prevent duplicate emails
                
            else
                printf "%-15s ${RED}%-15s${NC} %-10s\n" "$SERVICE" "[GAVE UP]" "See Logs"
            fi
        fi
    done

    # --- Memory & Disk ---
    echo -e "\n${BLUE}----------------------------------------------------${NC}"
    MEM=$(free -m | awk '/Mem:/ {printf "%d/%dMB (%.2f%%)", $3, $2, $3*100/$2}')
    DISK=$(df -h / | awk 'NR==2 {print $5}')
    echo -e "${GREEN}[+] Memory Usage:${NC} $MEM"
    echo -e "${GREEN}[+] Disk Usage:  ${NC} $DISK"

    echo -e "${BLUE}====================================================${NC}"
    echo "Logs: tail -f $LOG_FILE"
    echo "Press [CTRL+C] to stop..."
    
    sleep 2
done