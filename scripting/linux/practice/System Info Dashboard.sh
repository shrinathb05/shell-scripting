# 14. System Info Dashboard

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