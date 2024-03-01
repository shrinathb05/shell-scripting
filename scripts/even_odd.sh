#!/bin/bash
#Check the entered number is even or odd

read -p "Enter number: " NUM

if (( $NUM % 2 == 0 )) 
then
	echo "Even Number"
else
	echo "Odd Number..."
fi
