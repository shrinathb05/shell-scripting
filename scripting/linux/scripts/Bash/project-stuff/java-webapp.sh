#!/bin/bash

set -xe 

# Define VARIABLES
WORKING_DIR="/home/shri/Desktop/projects/app/var/work"
REPO_DIR="/home/shri/Desktop/projects/app/var/work/webapp-java"
BACKUP_DIR="/opt/tomcat/backup"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
DEPLOY_DIR="/opt/tomcat/webapps"

#GITHUB_TOKEN="your_personal_access_token" # Use a secret variable in real life
REPO_URL="https://github.com/shrinathb05/webapp-java.git"


# clean working directory
clean_working_dir() {
    cd $WORKING_DIR || exit 1
    rm -rf ./*
}
# download the artifact from github in working directory
download_artifact() {
    git clone $REPO_URL
}

# build the project using maven
# mvn clean package
package_build() {
    cd $GO_TO_REPO_DIR || exit 1
    mvn clean package

    # check war file created or not in target directory
    if [ -f "$GO_TO_REPO_DIR/target/maven-web-app.war" ]; then
        echo "WAR file created successfully."
    else
        echo "WAR file not found! Build failed."
        exit 1
    fi
}

# Connect to remote server
remote_server() {
    echo "Connecting to remote server..."
    sleep 2
    ssh root@10.181.63.247

    # backup old war file
    echo "Backing up old WAR..."
    cd $DEPLOY_DIR || exit 1
    if [ -f "maven-web-app.war" ];then
        mv "maven-web-app.war" $BACKUP_DIR/maven-web-app.war_$TIMESTAMP
    else
        echo "No existing WAR found to backup. Skipping."
    fi
    
    sleep 3

    # cleanup old backups
    echo "Cleaning old backups..."
    cd $BACKUP_DIR
    find . -type f -name "maven-web-app.war_*" -printf '%T@\t%p\n' | sort -t $'\t' -g | \ 
    head -n -2 | cut -d $'\t' -f 2- | xargs rm -f   

    sleep 3

    #stop tomcat server
    echo "Stopping Tomcat server..."
    stop
    sleep 5

}

# copy war file to tomcat server /opt/tomcat/webapps
depploy_war() {
    echo "Deploying new WAR file..."
    scp -r shri@192.168.1.6:$REPO_DIR/target/maven-web-app.war root@10.181.63.247:$DEPLOY_DIR

}

start_tomcat() {
    echo "Starting Tomcat server..."
    start
    sleep 5
}

# FUNCTIONS CALLING SEQUENCE
clean_working_dir
download_artifact
package_build
remote_server
depploy_war
start_tomcat

# END OF SCRIPT