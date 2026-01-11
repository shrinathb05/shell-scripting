# function define

def biggest_number(a,b,c):
	if a > b and a > c:
		print(f"{a} is the greatest among the both")
	elif b > a and b > c:
		print(f"{b} is greatest")
	elif c > a and c > b:
		print(f"{c} is greatest")
	else:
		print("All are euqal")


a = 10
b = 20
c = 30

biggest_number(a,b,c)