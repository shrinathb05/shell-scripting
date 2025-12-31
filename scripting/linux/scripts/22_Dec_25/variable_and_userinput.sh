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


# Read username and display it's home directory
read -p "Enter username: " user
eval echo "~$user"

echo
echo "-------------------------------------------------------------------------------------------------"
echo


# Take input for a service name and check it's status
read -p "Enter Service name: " svc
sudo systemctl status $svc
if [[ $? -eq 0 ]]; then
	echo "The $svc is running !!!"
else
	echo " The $svc is not running"
fi
echo
echo "-------------------------------------------------------------------------------------------------"
echo
comment

# Ask for a package name and check if installed
read -p "Enter package: " pkg
dpkg -l | grep "$pkg"
if [[ $? -eq 0 ]]; then
	echo "Package $pkg is installed"
else
	echo "Package $pkg is not installed"
fi
echo	
