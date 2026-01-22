#!/bin/bash

# --- LOGGING CONFIGURATION ---
LOG_DIR="/home/shri/Desktop/projects/app/var/logs"
mkdir -p "$LOG_DIR"

# Create a unique filename with the date and time
LOG_FILE="$LOG_DIR/deploy_$(date +%Y%m%d_%H%M%S).log"

# Redirect output to this specific file AND the screen
exec > >(tee "$LOG_FILE") 2>&1

echo "--- Deployment Started at $(date) ---"
echo "--- Logging to: $LOG_FILE ---"


# --- LOCAL VARIABLES ---
WORKING_DIR="/home/shri/Desktop/projects/app/var/work"
REPO_DIR="$WORKING_DIR/webapp-java"
LOCAL_WAR="$REPO_DIR/target/maven-web-app.war"

# --- REMOTE VARIABLES ---
REMOTE_USER="root"
REMOTE_IP="10.181.63.247"
DEPLOY_DIR="/opt/tomcat/webapps"
BACKUP_DIR="/opt/tomcat/backup"
APP_FOLDER_NAME="maven-web-app" 
TIMESTAMP=$(date +%Y%m%d%H%M%S)
REPO_URL="https://github.com/shrinathb05/webapp-java.git"

# 1. Start fresh locally
clean_local_working_dir() {
    echo "Cleaning local workspace..."
    rm -rf "$WORKING_DIR"/*
}

# 2. Build the project
build_project() {
    mkdir -p "$WORKING_DIR"
    git clone "$REPO_URL" "$REPO_DIR"
    cd "$REPO_DIR"
    mvn clean package
    if [ ! -f "$LOCAL_WAR" ]; then
        echo "ERROR: Maven build failed."
        exit 1
    fi
}

# 3. Remote Backup and residue cleanup
prepare_remote_server() {
    ssh ${REMOTE_USER}@${REMOTE_IP} << EOF
        # Stop Tomcat using your 'stop' soft link
        echo "Stopping Tomcat..."
        stop || true 

        # Backup existing WAR
        if [ -f "${DEPLOY_DIR}/${APP_FOLDER_NAME}.war" ]; then
            mv "${DEPLOY_DIR}/${APP_FOLDER_NAME}.war" "${BACKUP_DIR}/${APP_FOLDER_NAME}.war_${TIMESTAMP}"
        fi
        
        # Keep only latest 2 backups
        cd "${BACKUP_DIR}" && find . -type f -name "${APP_FOLDER_NAME}.war_*" -printf '%T@\t%p\n' | sort -t $'\t' -g | head -n -2 | cut -d $'\t' -f 2- | xargs rm -f

        # Clean old directory residue if exists
        if [ -d "${DEPLOY_DIR}/${APP_FOLDER_NAME}" ]; then
            echo "Removing old directory residue..."
            rm -rf "${DEPLOY_DIR}/${APP_FOLDER_NAME}"
        fi
EOF
}

# 4. Push and Verify Checksum
deploy_and_verify_checksum() {
    echo "Calculating local checksum..."
    LOCAL_SHA=$(sha256sum "$LOCAL_WAR" | awk '{print $1}')

    echo "Pushing WAR to remote..."
    scp "$LOCAL_WAR" ${REMOTE_USER}@${REMOTE_IP}:${DEPLOY_DIR}/

    echo "Verifying remote checksum..."
    REMOTE_SHA=$(ssh ${REMOTE_USER}@${REMOTE_IP} "sha256sum ${DEPLOY_DIR}/${APP_FOLDER_NAME}.war" | awk '{print $1}')

    if [ "$LOCAL_SHA" == "$REMOTE_SHA" ]; then
        echo "SUCCESS: Checksums match ($LOCAL_SHA)."
    else
        echo "ERROR: Checksum mismatch! Deployment aborted."
        exit 1
    fi
}

# 5. Start and Check Directory
start_and_verify_dir() {
    ssh ${REMOTE_USER}@${REMOTE_IP} << EOF
        # Start Tomcat using your 'start' soft link
        echo "Starting Tomcat..."
        start

        echo "Waiting for Tomcat to extract WAR..."
        sleep 12
        
        if [ -d "${DEPLOY_DIR}/${APP_FOLDER_NAME}" ]; then
            echo "SUCCESS: ${APP_FOLDER_NAME} directory found and extracted."
        else
            echo "ERROR: Tomcat failed to extract the WAR file."
            exit 1
        fi
EOF
}

# --- EXECUTION SEQUENCE ---
clean_local_working_dir
build_project
prepare_remote_server
deploy_and_verify_checksum
start_and_verify_dir
clean_local_working_dir  # Final cleanup of build files

echo "********************************************"
echo "   DEPLOYMENT FULLY COMPLETED SUCCESSFULLY  "
echo "********************************************"

echo "--- Deployment Completed at $(date) ---"
