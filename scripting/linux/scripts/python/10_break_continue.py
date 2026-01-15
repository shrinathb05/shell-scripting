''' 
Break and Continue
    Using for loops and while loops in Python allow you to automate and repeat tasks in an efficient manner.
    But sometimes you wish to interept or change the flow or exit from the loop while its executing.
    In Python, break and continue statements can alter the flow of a normal loop. The break and continue statements are used in these cases.

The break statement provides you with the opportunity to exit out of a loop when an external condition is triggered, 
this external condition could be if block which evaluates to true somehere in the iteration and use break keyword to exit from the loop.



# Brake statement

for i in "DevOps":
    print(i)
    if i == "v":
        print("found the date.")
        break
print("out of loop")
'''
# -----------------------------------------------------------------------------------------------------------
'''

# Python continue statement
    The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
    Loop does not terminate but continues on with the next iteration.


# Continue statement
for i in "DevOps":
    if i == "v":
        print("Found my data.")
        continue
    print(f"The value of i is: {i}")

print("Out of loop")
'''

# Example 3
# We are getting some randorm value from the list and priting it
import random

'''

VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "Astrazeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"************** Testing vaccine {vac}")
    if vac == LUCKY:
        print("####################################")
        print(f"{LUCKY} Vaccine, TEST SUCCESSFULL.....")
        print("####################################")
        break
    else:
        print("$$$$$$$$$$$$$$$$$$$")
        print("TEST FAILED")
        print("$$$$$$$$$$$$$$$$$$$")
        print("")
'''

# Continue
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "Astrazeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"************** Testing vaccine {vac}")
    if vac == LUCKY:
        print("####################################")
        print(f"{LUCKY} Vaccine, TEST SUCCESSFULL.....")
        print("####################################")
        continue
    else:
        print("$$$$$$$$$$$$$$$$$$$")
        print("TEST FAILED")
        print("$$$$$$$$$$$$$$$$$$$")
        print("")
