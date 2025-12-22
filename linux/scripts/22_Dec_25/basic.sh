#!/bin/bash

# print the current logged in user and hostname

echo "User: $(whoami)"
echo "Hostname: $(hostname)"

# Dispaly current date and time
echo "Current date and time is: date"

# Print system uptime
echo "The system is up from last: uptime"

# print the OS version
OS=$(cat /etc/os-release | grep PRETTY_NAME)
echo "The current os-version is $OS"

# show the current working directory
echo "The current directory is : pwd"

# Create a variable with the username and print it
tool="Dev-Ops"
echo "I would love to start the journey of $tool learning"

# Ask user for their name and greet them with the message
read -p "Enter your name: " name
echo "Hi Mr.$name! Welcome to our community thanks for joining"

# Print total number of users  currently logged in
c=$(who | wc -l)
echo "The current user logged in count is $c"

# Save system info into the file
echo "User: $(whoami)" >> system_info.txt
echo "host: $(hostname)" >> system_info.txt
date >> system_info.txt
uptime >> system_info.txt

