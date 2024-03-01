#!/bin/bash
set -x

#Create a script that will take bacakup of files

#Check the directory is exits or not
BASE1="/home/shrinath/scripts"

#Backup Directory
BASE2="/home/shrinath/backup"

#Deleted directory
BASE3="/home/shrinath/tmp/deleted_files"

#Create backup directory if not exists
mkdir -p "$BASE2"

#Get current timestamp
time=$(date +"%M%H%S%d%m%Y")

#Navigate to directory
cd "$BASE1" || exit

#Iterate over files 
for file in *.txt
do
	#Skip directories
	if [[ -f "$file" ]]
	then
		#Backup the original file
		cp "$file" "$BASE2/${file}.${time}.bkp"

		#Rename file with time
		rm -rf "$file"

		echo "Renamed and taken backup of $file"
	fi
done
