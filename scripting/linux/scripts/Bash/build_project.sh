#!/bin/bash

# Define project path
PROJECT_ROOT="/home/ltfadmin.dn/app/source/WelcomeKitApp"

# Navigate to the project directory
cd "$PROJECT_ROOT" || { echo "Directory not found"; exit 1; }

echo "Starting build process..."

# One-line Maven command: Clean old files, Compile code, Run Tests, and Package WAR
mvn clean package

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "-------------------------------------------------------"
    echo "BUILD SUCCESSFUL"
    echo "Your artifact is ready at: $PROJECT_ROOT/target/WelcomeKitApp.war"
    echo "-------------------------------------------------------"
else
    echo "-------------------------------------------------------"
    echo "BUILD FAILED"
    echo "Please check the Maven error logs above."
    echo "-------------------------------------------------------"
    exit 1
fi