'''
Making program for skills in IT organization for the users to check the related
skills are present in which team
'''
print("This IT organization has various skills")
print("Find out your match")

print("Enter capitalised values")

# list 
Devops = ['Jenkins', 'Shell', 'Git', 'Github', 'Docker', 'Kubernetes', 'Terraform']

# tuple
Development = ('NodeJs', 'Python', '.Net', 'Java', 'ReactJs', 'AngularJs')

# Dictonary
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1253}

# USER input
usr_skill = input("Enter your skills: ")

# Check in the database if we have the skills
if (usr_skill in Devops):
    print(f"We have {usr_skill} in Devops Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Dev Team.")
elif (usr_skill in cntr_emp1.values() or usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print(f"{usr_skill} Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling.")