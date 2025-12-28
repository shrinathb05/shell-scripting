# Python Operators

# 01.Arithmetic operators
from ast import Or


x = 2
y = 4

# Addition
total = x + y
print(total)

# Substraction
total = x - y
print(total)

# Multiplication
total = x * y
print(total)

# Division
total = y / x
print(total)

# Modulus
total = y % x
print(total)

# Power square
total = y ** x
print(total)

#----------------------------------------------------------

# Comparision Operator
# This operator will print values in boolen format like True or False
a = 30
b = 60

out = a < b     # less than 
print(out)

out = a > b     # greater than 
print(out)

out = a != b    # not equal to
print(out)

out = a <= b    # less than equal
print(out)

out = a >= b    # greater than equal
print(out)

#----------------------------------------------------------

# Assignment Operator
c = 3
d = 10

# c += d # c is similar euql to c = c + d
# print(c)

c -= d # c is similar euql to c = c - d
print(c)

#----------------------------------------------------------

# Logical Operators
# AND (if once condition is true and another is false then it will return as false)
# OR (If once condition os true and another is false then it will return true)

# Examples:-
'''
TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or TRUE = TRUE
FALSE or FALSE = FALSE
FALSE and TRUE = FALSE
TRUE and FALSE = FALSE
'''

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y) # One condition will be TRUE
print(out)

out = (a > b) or (x < y) # One condition will be TRUE
print(out)

out = (a > b) or (x > y) # One condition will be FALSE
print(out)


out = (a < b) and (x > y) # One condition will be FALSE
print(out)

out = (a > b) and (x < y) # One condition will be FALSE
print(out)

out = (a > b) and (x > y) # One condition will be FALSE
print(out)

# NOT operator
out = not(x < y) # If condition is TRUE the not operator will make it FALSE
print(out)

out = not(x > y) # If condition is FALSE the not operator will make it TRUE
print(out)


# Membership Operator

first_tuple = (str1, "DevOps", 54, num1, 5.4)
ans = "DevOps"

