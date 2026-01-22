# String datatypes
str1 = "alpha"
str2 = 'beta'
str3 = '''gama string'''
str4 = """delta string"""

# Numbers
num1 = 123
flt1 = 2.0

############################################################

# list array(collection of variables)
# lists are mutable
# list's can be editable 
# collection of multi datatypes, enclosed in square brackets '[]'
first_list = [str1, "DevOps", 54, num1, 5.4]

# printing list
print(first_list)

############################################################

# Tuple (Its a collection of datatype same as list)
# tuples are imuttable
# tumple's can't edit the content
# tuple's are enclosed in round brackets '()'

first_tuple = (str1, "DevOps", 54, num1, 5.4)

# printing tuple
print(first_tuple)

############################################################

# Dictionary (It is also a collection of data)
# It's a collection of data in key value pairs
# are enlcosed in curly braces '{}'
first_dict = {"Name":"shri", "weight":74, "Exercises":["Boxing","dancing","running"]}

# Printing Dictionary
print(first_dict)

print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_disct is a:", type(first_dict))

# Boolean Datatype
x = True
y = False
print(x)
print(y)

print("X is a: ", type(x))
print("Y is a: ", type(y))