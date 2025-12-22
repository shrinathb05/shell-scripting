#!/bin/bash

set -x

#Directory path
BASE="/mnt/e/Devops/#scripts/scripts"

#commit message
commit_message="All files commited successfully"

#Checking only files and commiting
for file in *
do
	if [[ -f "$file" ]]
	then
		git add .
		git commit -m "$commit_message"
		git push -u origin main
	fi
done
