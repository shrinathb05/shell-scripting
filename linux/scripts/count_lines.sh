#!/bin/bash

#Directory
#path="/mnt/e/Devops/#scripts/scripts/$1"

file=$1

#Check the file exist or not and print the lines
if [[ -f $file ]]
then
	echo "File exist"
	line_count=$(wc -l < "$file")
	echo "Number of lines in $file file : $line_count"
else
	echo "File not present"
fi

