# Slicing
# getting slice from data or data from subdata
# There are index number from 0 to n numbers

planet1="Closest of Sun"
print(planet1)

# Slicing particular character
print(planet1[0])
print(planet1[1])
print(planet1[2])

# Negative indexing (Reverse order)
# this indexing will start from the end of the string
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Range slicing a string that means get substring from string
print(planet1[1:4])
print(planet1[:])
print(planet1[:7]) # till the string
print(planet1[11:])

'''
# Slicing Tuple
devops=("Linux", "Vagrant", "Bash-scripting", "AWS", "Jenkins", "Python", "Ansible", "Docker")
print(devops[0])
print(devops[2])
print(devops[3])

# range
print(devops[1:4])
print(devops[1:4][1])

print(devops[1:4][1][5:11][-1])



# Slicing List
devops=["Linux", "Vagrant", "Bash-scripting", "AWS", "Jenkins", "Python", "Ansible", "Docker"]
print(devops[0])
print(devops[2])
print(devops[3])

# range
print(devops[1:4])
print(devops[1:4][1])

print(devops[1:4][1][5:11][-1])

'''

# Dictionary Example
skills = {"Devops" : ("AWS", "Jenkins", "Python", "Ansible", "Docker"), "Development": ["Java", "Python", "Ruby", "Shell", "C++", "NodeJS"]} # value is in Tuple and List format

# Printing
print(skills)
print(skills["Devops"])
print(skills["Development"])

# Slicing
print(skills["Devops"][-1][:4]) # printing the doc
print(skills["Devops"][2][:2]) # printing the py

print(skills["Development"][4][0:2]) # printing the c+

