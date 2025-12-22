#!/bin/bash
#Check and display the hidden files 

for file in .*
do
	if [ -f "$file" ]
	then
		echo "$file"
	fi
done
