#!/bin/bash

<<comment
# Ask user for a directory name and display all files in it
read -p "Enter directory: " dir
ls "$dir"

echo
echo "-------------------------------------------------------------------------------------------------"
echo

# Ask user for a process name and show if it's running
read -p "Enter process name: " pname
proc=$(pgrep -l "$pname")

if [[ -n "$proc" ]]; then
	echo "The $pname is running !!!"
else
	echo " The $pname is not running"
fi

echo
echo "-------------------------------------------------------------------------------------------------"
echo
#comment

# Accept a port number and check if it's open
read -p "Enter the port: " port
ss -tulpn | grep ":$port"

if [[ $? -eq 0 ]]; then
	echo "Port $port is open"
else
	echo "Port $port is closed"
fi
echo
echo "-------------------------------------------------------------------------------------------------"
echo
comment

# Read username and display it's home directory
read -p "Enter username: " user
eval echo "~$user"

