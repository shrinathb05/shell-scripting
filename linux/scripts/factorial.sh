#!/bin/bash
#Write a script to print the factorial of numbers

read -p "Enter the number: " num
factorial=1

for (( i=1; i<=num; i++ ))
do
	factorial=$((factorial * i))
done

echo "Factorial of $num is : $factorial"
