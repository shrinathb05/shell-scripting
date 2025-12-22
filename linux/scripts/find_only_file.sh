#!/bin/bash
#Find only files in presnet directory and another directory

#Enter path to print the files
read -p "Enter Path : " path

files=$(find $path -maxdepth 1 -type f -ls)

echo "$files"
