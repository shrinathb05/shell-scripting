#!/bin/bash
#Script to count the words from a sentence

#Take input from user
read -p "Enter a sentence: " sentence

#word count
word_count=$(echo $sentence | wc -w)

#Print the count
echo "The total word count of is : $word_count"
echo "#################################################################"
echo "#################################################################"


#Print count of words from a file
w_count=$(wc -w < test.log)
l_count=$(wc -l < test.log)
c_count=$(wc -c < test.log)

echo "Total word count is : $w_count"
echo "Total line count is : $l_count"
echo "Total Character count is : $c_count"

echo "#################################################################"
echo "#################################################################"

#Print total word,line,character count from file as taking input from the user 
read -p "Enter file name: " file

w_count=$(wc -w < $file)
l_count=$(wc -l < $file)
c_count=$(wc -c < $file)


echo "Total word count is : $w_count"
echo "Total line count is : $l_count"
echo "Total Character count is : $c_count"

