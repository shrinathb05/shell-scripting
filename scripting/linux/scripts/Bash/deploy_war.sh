#!/bin/bash

# Exit on error, print commands
set -xe 

# --- LOCAL VARIABLES ---
WORKING_DIR="/home/shri/Desktop/projects/app/var/work"
REPO_DIR="$WORKING_DIR/webapp-java"
LOCAL_WAR="$REPO_DIR/target/maven-web-app.war"

# --- REMOTE VARIABLES ---
REMOTE_USER="root"
REMOTE_IP="10.181.63.247"
DEPLOY_DIR="/opt/tomcat/webapps"
BACKUP_DIR="/opt/tomcat/backup"
TIMESTAMP=$(date +%Y%m%d%H%M%S)

REPO_URL="https://github.com/shrinathb05/webapp-java.git"

# 1. Start fresh
clean_working_dir() {
    rm -rf "$WORKING_DIR"/*
}

# 2. Get code
download_artifact() {
    cd "$WORKING_DIR"
    git clone "$REPO_URL"
}

# 3. Build locally
package_build() {
    cd "$REPO_DIR"
    mvn clean package
    if [ ! -f "$LOCAL_WAR" ]; then
        echo "Build failed!"
        exit 1
    fi
}

# 4. REMOTE OPERATIONS (Backup, Stop, Cleanup)
# We send these commands in one single SSH "envelope"
prepare_remote_server() {
    echo "Running remote backup and cleanup..."
    ssh ${REMOTE_USER}@${REMOTE_IP} << EOF
        # Backup existing WAR
        if [ -f "${DEPLOY_DIR}/maven-web-app.war" ]; then
            mv "${DEPLOY_DIR}/maven-web-app.war" "${BACKUP_DIR}/maven-web-app.war_${TIMESTAMP}"
        fi

        # Cleanup old backups (Keep only latest 2)
        cd "${BACKUP_DIR}"
        find . -type f -name "maven-web-app.war_*" -printf '%T@\t%p\n' | sort -t $'\t' -g | head -n -2 | cut -d $'\t' -f 2- | xargs rm -f

        # Stop Tomcat (Use systemctl for LXC/Ubuntu)
        systemctl stop tomcat || /opt/tomcat/bin/shutdown.sh || true
EOF
}

# 5. Push the built WAR to Remote
deploy_war() {
    echo "Pushing WAR to remote server..."
    scp "$LOCAL_WAR" ${REMOTE_USER}@${REMOTE_IP}:${DEPLOY_DIR}/
}

# 6. Start Remote Tomcat
start_remote_tomcat() {
    ssh ${REMOTE_USER}@${REMOTE_IP} "systemctl start tomcat || /opt/tomcat/bin/startup.sh"
}

# --- EXECUTION ---
clean_working_dir
download_artifact
package_build
prepare_remote_server
deploy_war
start_remote_tomcat

echo "DEPLOYMENT FINISHED SUCCESSFULLY"