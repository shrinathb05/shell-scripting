#!/bin/bash

dir=$1

if [ -d $dir ]
then
	ls -lrt "$dir"
else
	echo "Directory Not exists"
fi	
