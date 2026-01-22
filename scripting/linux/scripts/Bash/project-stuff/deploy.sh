#!/bin/bash

set -x

# Define VARIABLES
WORKING_DIR="/home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT"
BACKUP_DIR="/home/ltfadmin.dn/app/Launch_Agent/Backup/"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
DEPLOY_DIR="/home/ltfadmin.dn/ApacheTomcat/webapps"
APP_NAME="WelcomeKitApp"

GITHUB_TOKEN="your_personal_access_token" # Use a secret variable in real life
REPO_URL="https://api.github.com/repos/YourOrg/WelcomeKitRepo/releases/assets/ASSET_ID"


# FUNCTIONS
# Clean working directory
clean_working_dir() {
    cd $WORKING_DIR || exit 1
    rm -rf ./*
}

# Download Artifact from github repository.

download_artifact() {
    echo "Stage 2: Downloading artifact from GitHub..."
    cd "$WORKING_DIR" || exit 1

    curl -L -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/octet-stream" \
        "$REPO_URL" -o "${APP_NAME}.war"

    if [ $? -eq 0 ] && [ -s "${APP_NAME}.war" ]; then
        echo "Download successful. $(ls -lh ${APP_NAME}.war | awk '{print $5}')"
    else
        echo "ERROR: Download failed!"
        exit 1
    fi
}

# BACKUP CLEANUP
cleanup_backups() {
    echo "Cleaning old backups..."
    cd $BACKUP_DIR
    find . -type f -name "{$APP_NAME}.war_*" -printf '%T@\t%p\n' | sort -t $'\t' -g | \ 
    head -n -2 | cut -d $'\t' -f 2- | xargs rm -f
}

# Take backup of old war file
backup_war() {
    echo "Backing up old WAR..."
    cd $DEPLOY_DIR || exit 1
    if [ -f "{$APP_NAME.war}" ];then
        mv "{$APP_NAME}.war" $BACKUP_DIR/${APP_NAME}.war_$TIMESTAMP
    else
        echo "No existing WAR found to backup. Skipping."
    fi
}

# Check directory status before deployment
check_dir_status_before() {
    cd $DEPLOY_DIR
    
    # Checks the directory exist or not
    if [ ! -d "$APP_NAME" ]; then
        echo "The $APP_NAME is not available"
    else
        echo "The $APP_NAME is available"
        exit 1
    fi
}

# Deploy War file
deploy_war() {
    # cd $WORKING_DIR 
    cp -r "$WORKING_DIR/${APP_NAME}.war" "$DEPLOY_DIR"
}

# Checksum the war files
checksum() {
    # Define paths
    SOURCE_FILE="$WORKING_DIR/${APP_NAME}.war"
    DEST_FILE="$DEPLOY_DIR/${APP_NAME}.war"

    # Capture the first column (the number) of the cksum for both
    SOURCE_CK=$(cksum "$SOURCE_FILE" | awk '{print $1}')
    DEST_CK=$(cksum "$DEST_FILE" | awk '{print $1}')

    if [ "$SOURCE_CK" == "$DEST_CK" ]; then
        echo "SUCCESS: Checksums match. File integrity verified."
    else
        echo "ERROR: Checksum mismatch! The file was corrupted during deployment."
        exit 1  # This triggers the "Deployment Failed" box in your flowchart
    fi
}

# Check directory status after deployment
check_dir_status_after() {
    cd $DEPLOY_DIR || exit 1
    
    # Checks the directory exist or not
    if [ -d "$APP_NAME" ]; then
        echo "The $APP_NAME is created successfully"
    else
        echo "ERROR: The $APP_NAME is not created"
        exit 1
    fi
}

# The Notification Function
send_notification() {
    local status="$1"
    local subject="Deployment $status: $APP_NAME - $(date)"
    local recipient="admin@yourdomain.com"
    
    # Construct the message body
    local message="Deployment of $APP_NAME has $status.\n\nTimestamp: $TIMESTAMP\nServer: $(hostname)\nCheck the logs at $WORKING_DIR/deploy.log for details."

    echo -e "$message" | mailx -s "$subject" "$recipient"
}


# The Rollback Function

rollback() {
    echo "CRITICAL: Deployment failed. Initiating Auto-Rollback..."
    
    # Define the backup we just created
    local LAST_BACKUP="$BACKUP_DIR/${APP_NAME}.war_$TIMESTAMP"
    
    if [ -f "$LAST_BACKUP" ]; then
        echo "Restoring previous version: $LAST_BACKUP"
        cp "$LAST_BACKUP" "$DEPLOY_DIR/${APP_NAME}.war"
        echo "Rollback successful. The previous version has been restored."
    else
        echo "FATAL ERROR: Could not find backup file for rollback!"
    fi
    
    send_notification "FAILED & ROLLED BACK"
    # Exit with 1 so the deployment tool (and you) knows the overall process failed
    exit 1
}

# --- EXECUTION FLOW ---

# The Complete Flow Check
# Now that you have all the functions, your execution order at the bottom of the script should look like this to match your original flowchart:
# clean_working_dir (Start fresh)
# download_artifact (Get the new WAR)
# cleanup_backups (Keep only the 2 newest in Backup folder)
# backup_war (Move currently running WAR to Backup with timestamp)
# check_dir_status_before (Wait for Tomcat to finish undeploying old folder)
# deploy_war (Copy new WAR to webapps)
# checksum (Verify the copy was perfect)
# check_dir_status_after (Verify Tomcat created the new folder)
# clean_working_dir (Final cleanup)

########################################################################################################################
# STAGE 1 Clean working directory
clean_working_dir
########################################################################################################################
# Stage 2 Downloading artifacts from the github
echo "Downloading files to $WORKING_DIR..."
download_artifact
########################################################################################################################
# Stage 3 taking backup of file and removing the old files from backup directory
################### Clean Old Backup files ########################
cleanup_backups
################### Backup deployable files ########################
backup_war
# Stage 4 sleep
sleep 30s
# Stage 5 check directory is exist or not before deployment
check_dir_status_before
# Stage 6 Deploy war file
deploy_war
# Stage 7 sleep
sleep 30s
# Stage 8 checksum check the war file is deployed properly or not
checksum
# Stage 9 check directory is exist or not after deployment
check_dir_status_after
# STage 10 clean working directory after deployment
clean_working_dir

# Success Notification
send_notification "SUCCESSFUL"

echo "DEPLOYMENT COMPLETED SUCCESSFULLY"