#!/bin/bash
#Script to rename all files in a directory with a specific extension to have a prefix:
set -x

extension=$1
prefix=$2
BASE="/home/shrinath/backup/"

for file in *$extension
do
	mv "$file" "${file}$prefix"
done
for file in *_bkp
do
	mv "$file" "$BASE"
done

