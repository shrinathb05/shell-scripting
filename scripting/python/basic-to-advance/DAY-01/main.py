s = "hello"
t = s
s = s.upper()
print(t)

print("Hello"[:-1])

a, *b, c = [1, 2, 3, 4, 5]
print(b)

# program
total = 0
for i in range(1, 5):
    total += i
print(total)

# List slicing
a = [1, 2, 3, 4]
a[1:3] = [9]
print(a)


x = y = [10, 20]
x += [30]
print(y)

cart = ("shoes", "Bag", "watch")
a, b, c = cart
print(b)

for i in []:
    print("loop")
else:
    print("else")

# program 
word = "Worker"
num = 123425
print(word[3] + str(num))

# program
x = 0
y = [0]
if x:
    print("A")
elif y and x == False:
    if y[0]:
        print("B")
    else:
        print("C")
else:
    print("D")

# program
a = "9"
a += "1"
print(int(a) - 10)



# practice program

# Create a script that prints your name and role as "DevOps Engineer".
name = "Shrinath Bhosale"
role = "Devops Engineer"
print(f"My name is {name} and my role is {role}")

# Store a server name in a variable and print it.
server = "Pre-prod"
print(f"The server we are currently is using is {server}")

# Store CPU usage as a number and print it.
cpu=85
print(f"CPU usage is {cpu}%")

# Prints the datatype of a variable storing memory usage.
string = "256GB"
print(type(string))

int=43
print(type(int))

# Take user input for username and print a welcome message.
username = input("Enter your username: ")
print(f"welcome {username} to the system! ")


# Take user input for age and print whether the user is an adult or not.
age = int(input("enter your age"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")



































