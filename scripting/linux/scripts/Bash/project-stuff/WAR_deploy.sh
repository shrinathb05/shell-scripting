#!/bin/bash

# Stages
# Clean working directory

# Stage 1
# Working Directory
cd /home/ltfadmin.dn/app/Launch_Agent/var/work//Welcome_KIT
sudo rm -rf *

# Stage 2 Downloading artifacts from the github
Downloading files to /home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT.

# Stage 3 taking backup of file and removing the old files from backup directory

################### Clean Old Backup files ########################
cd /home/ltfadmin.dn/app/Launch_Agent/Backup/
find . -type f -name "WelcomeKitApp.war_*" -printf '%T@\t%p\n' |
sort -t $'\t' -g |
head -n -2 |
cut -d $'\t' -f 2- |
xargs rm -f
################### Backup deployable files ########################
timestamp=$('`date +%Y%m%d%H%M%S`')
cd /home/ltfadmin.dn/ApacheTomcat/webapps
mv WelcomeKitApp.war /home/ltfadmin.dn/app/Launch_Agent/Backup/WelcomeKitApp.war_$timestamp

# Stage 4
sleep 30s

# Stage 5 check directory is exist or not before deployment
cd /home/ltfadmin.dn/ApacheTomcat/webapps
DIR="WelcomeKitApp"
if [ ! -d "$DIR "];then
    echo "The $DIR is not available"
else
    echo "The $DIR is available"
    exit 1
fi

# -------------------------------

# Stage 6 Deploy war file
#-------------------------------
# working directory: /home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT
cd /home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT/ 
cp -r WelcomeKitApp.war /home/ltfadmin.dn/ApacheTomcat/webapps
 



