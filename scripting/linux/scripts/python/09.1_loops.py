# for loop nested loop (loop inside the looop)
'''
vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "Astrazeneca"]
for vac in vaccines:
    print("")
    print("I would like to take shot of " )
    print("")
    # again for loop in vac
    for i in vac:
        print(i)
'''        

# While loop example
import time

x = 2
while True:
    print(f"The value of X is: {x}")
    print("Looping......")
    x *= 2
    time.sleep(1)
    