#!/usr/bin/env python3

# Define the function and print the largest number
def biggest_number(a,b,c):
    if a > b and a > b:
        print(f"{a} is greates among the b and c")
    elif b > a and b > c:
        print(f"{b} is greatest")
    elif c > a and c > b:
        print(f"{c} is greatest")
    else:
        print("All are equal")

a = 10
b = 34
c = 32

biggest_number(a,b,c)

