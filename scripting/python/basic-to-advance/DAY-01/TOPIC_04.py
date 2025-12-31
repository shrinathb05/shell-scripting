# TOPIC 4: Printing & Reading Input
# In this topic, we will learn how to print output to the console and read input from the user in Python.
# Printing Output
# To print output to the console, we use the print() function. Here are some examples
print("Hello, World!")  # Prints a string
print(42)               # Prints an integer
print(3.14)             # Prints a float
print(True)            # Prints a boolean value 

# You can also print multiple values by separating them with commas
name = "Alice"
age = 30
print("Name:", name, "Age:", age)   

# Reading Input
# To read input from the user, we use the input() function. This function waits for the user to type something and press Enter.
user_name = input("Enter your name: ")
print("Hello,", user_name)  # Greets the user by name

# You can also read numbers by converting the input string to the desired type
user_age = int(input("Enter your age: "))  # Reads an integer
print("You are", user_age, "years old.")
user_height = float(input("Enter your height in meters: "))  # Reads a float
print("You are", user_height, "meters tall.")

# Summary
# In this topic, we learned how to use the print() function to display output and the input() function to read input from the user in Python.   
# Practice Exercise
# Write a program that asks the user for their favorite color and food, then prints a message including both.
favorite_color = input("What is your favorite color? ")
favorite_food = input("What is your favorite food? ")
print("Your favorite color is", favorite_color, "and your favorite food is", favorite_food + ".")   

# f-strings (formatted string literals)
# f-strings provide a way to embed expressions inside string literals, using curly braces {}.
# They are prefixed with the letter 'f' or 'F'.
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Using f-string to format output

# You can also perform operations inside the curly braces
width = 5
height = 10
print(f"The area of a rectangle with width {width} and height {height} is {width * height}.")  # Calculates area inside f-string

# Summary
# f-strings are a convenient way to format strings in Python, allowing you to include variables and expressions directly within the string.
# Practice Exercise
# Write a program that asks the user for their name and age, then prints a message using an f-string.
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello, {user_name}! You are {user_age} years old.")


# Practice Exercise
# Write a program that asks the user for the length and width of a rectangle, then calculates and prints the area using an f-string.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width   
print(f"The area of the rectangle is {area}.")

# Write a program that asks the user for their first and last name, then prints a greeting using an f-string.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name} {last_name}! Welcome!")


# Write a program that asks the user for a number, then prints the square of that number using an f-string.
number = float(input("Enter a number: "))
square = number ** 2
print(f"The square of {number} is {square}.")


# Write a program that asks the user for their city and country, then prints a message using an f-string.
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")  


# Write a program that asks the user for the radius of a circle, then calculates and prints the circumference using an f-string.
import math 
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle with radius {radius} is {circumference}.")


# Write a program that asks the user for their favorite movie and actor, then prints a message using an f-string.
favorite_movie = input("What is your favorite movie? ")
favorite_actor = input("Who is your favorite actor? ")
print(f"Your favorite movie is {favorite_movie} and your favorite actor is {favorite_actor}.")


# Write a program that asks the user for the base and height of a triangle, then calculates and prints the area using an f-string.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}.")


# Write a program that asks the user for their favorite book and author, then prints a message using an f-string.
favorite_book = input("What is your favorite book? ")
favorite_author = input("Who is your favorite author? ")
print(f"Your favorite book is {favorite_book} and your favorite author is {favorite_author}.")


# Write a program that asks the user for the length of a side of a square, then calculates and prints the perimeter using an f-string.
side_length = float(input("Enter the length of a side of the square: "))
perimeter = 4 * side_length 
print(f"The perimeter of the square is {perimeter}.")   


# Write a program that asks the user for their favorite sport and team, then prints a message using an f-string.
favorite_sport = input("What is your favorite sport? ")
favorite_team = input("What is your favorite team? ")
print(f"Your favorite sport is {favorite_sport} and your favorite team is {favorite_team}.")


# Write a program that asks the user for the radius of a sphere, then calculates and prints the volume using an f-string.
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
print(f"The volume of the sphere with radius {radius} is {volume}.") 


# Write a program that asks the user for their favorite holiday destination and activity, then prints a message using an f-string.
favorite_destination = input("What is your favorite holiday destination? ")
favorite_activity = input("What is your favorite activity? ")
print(f"Your favorite holiday destination is {favorite_destination} and your favorite activity is {favorite_activity}.")


# Write a program that asks the user for the length and width of a rectangle, then calculates and prints the perimeter using an f-string.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is {perimeter}.")   


# Write a program that asks the user for their favorite musician and song, then prints a message using an f-string.
favorite_musician = input("Who is your favorite musician? ")
favorite_song = input("What is your favorite song? ")
print(f"Your favorite musician is {favorite_musician} and your favorite song is {favorite_song}.")


# Write a program that asks the user for the height and base of a triangle, then calculates and prints the area using an f-string.
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}.")       


# Write a program that asks the user for their favorite TV show and character, then prints a message using an f-string.
favorite_tv_show = input("What is your favorite TV show? ")
favorite_character = input("Who is your favorite character? ")
print(f"Your favorite TV show is {favorite_tv_show} and your favorite character is {favorite_character}.")

# Write a program that asks the user for the diameter of a circle, then calculates and prints the circumference using an f-string.
diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"The circumference of the circle with diameter {diameter} is {circumference}.")  


# Write a program that asks the user for their favorite season and reason, then prints a message using an f-string.
favorite_season = input("What is your favorite season? ")
reason = input("Why do you like this season? ")
print(f"Your favorite season is {favorite_season} because {reason}.")


# Write a program that asks the user for the length of a rectangle and its width, then calculates and prints the area using an f-string.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width   
print(f"The area of the rectangle is {area}.")


# Write a program that asks the user for their favorite animal and habitat, then prints a message using an f-string.
favorite_animal = input("What is your favorite animal? ")
habitat = input("What is its natural habitat? ")
print(f"Your favorite animal is {favorite_animal} and it lives in {habitat}.")


# Write a program that asks the user for the side length of a cube, then calculates and prints the volume using an f-string.
side_length = float(input("Enter the side length of the cube: "))
volume = side_length ** 3
print(f"The volume of the cube is {volume}.")   


# Write a program that asks the user for their favorite hobby and reason, then prints a message using an f-string.
favorite_hobby = input("What is your favorite hobby? ")
reason = input("Why do you enjoy this hobby? ")
print(f"Your favorite hobby is {favorite_hobby} because {reason}.")


# Write a program that asks the user for the length of a rectangle and its width, then calculates and prints the diagonal using an f-string.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
diagonal = (length**2 + width**2) ** 0.5
print(f"The diagonal of the rectangle is {diagonal}.")   


# Write a program that asks the user for their favorite cuisine and dish, then prints a message using an f-string.
favorite_cuisine = input("What is your favorite cuisine? ")
favorite_dish = input("What is your favorite dish? ")
print(f"Your favorite cuisine is {favorite_cuisine} and your favorite dish is {favorite_dish}.")


# Write a program that asks the user for the radius of a cylinder and its height, then calculates and prints the volume using an f-string.
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * radius**2 * height
print(f"The volume of the cylinder is {volume}.")


# Write a program that asks the user for their favorite video game and character, then prints a message using an f-string.
favorite_video_game = input("What is your favorite video game? ")
favorite_character = input("Who is your favorite character? ")
print(f"Your favorite video game is {favorite_video_game} and your favorite character is {favorite_character}.")


# Write a program that asks the user for the length of a rectangle and its width, then calculates and prints the area using an f-string.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width           
print(f"The area of the rectangle is {area}.")


# Write a program that asks the user for their favorite dessert and reason, then prints a message           
favorite_dessert = input("What is your favorite dessert? ")
reason = input("Why do you like this dessert? ")
print(f"Your favorite dessert is {favorite_dessert} because {reason}.") #using an f-string.


# Write a program that asks the user for the radius of a circle, then calculates and prints the area using an f-string.
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print(f"The area of the circle with radius {radius} is {area}.")    


# Write a program that asks the user for their favorite actor and movie, then prints a message using an f-string.
favorite_actor = input("Who is your favorite actor? ")
favorite_movie = input("What is your favorite movie? ")
print(f"Your favorite actor is {favorite_actor} and your favorite movie is {favorite_movie}.")


# Write a program that asks the user for the height and base of a triangle, then calculates and prints the area using an f-string.
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = 0.5 * base * height          
print(f"The area of the triangle is {area}.")

