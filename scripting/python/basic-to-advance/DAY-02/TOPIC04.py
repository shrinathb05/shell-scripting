# 🔹 TOPIC 4: if–elif–else (MULTIPLE CONDITIONS)

# Example 1: Grading System
score = 85  
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F' 
print(f"Score: {score}, Grade: {grade}")
# Output: Score: 85, Grade: B

# Example 2: Age Group Classification
age = 25
if age < 13:
    group = 'Child'
elif age < 20:
    group = 'Teenager'
elif age < 65:
    group = 'Adult'
else:
    group = 'Senior'
print(f"Age: {age}, Group: {group}")
# Output: Age: 25, Group: Adult

# Example 3: Day of the Week
day_number = 4
if day_number == 1:
    day_name = 'Monday'
elif day_number == 2:
    day_name = 'Tuesday'
elif day_number == 3:
    day_name = 'Wednesday'
elif day_number == 4:
    day_name = 'Thursday'
elif day_number == 5:
    day_name = 'Friday'
elif day_number == 6:
    day_name = 'Saturday'
elif day_number == 7:
    day_name = 'Sunday'
else:
    day_name = 'Invalid day number'
print(f"Day Number: {day_number}, Day Name: {day_name}")
# Output: Day Number: 4, Day Name: Thursday

# Example 4: Temperature Classification
temperature = 75
if temperature < 32:
    weather = 'Freezing'
elif temperature < 50:
    weather = 'Cold'
elif temperature < 70:
    weather = 'Cool'
elif temperature < 85:
    weather = 'Warm'
else:
    weather = 'Hot'
print(f"Temperature: {temperature}°F, Weather: {weather}")
# Output: Temperature: 75°F, Weather: Warm

# Example 5: Traffic Light System
light_color = 'Yellow'
if light_color == 'Red':    
    action = 'Stop'
elif light_color == 'Yellow':
    action = 'Caution'
elif light_color == 'Green':
    action = 'Go'       
else:
    action = 'Invalid color'
print(f"Light Color: {light_color}, Action: {action}")
# Output: Light Color: Yellow, Action: Caution

# Example 6: Movie Rating
movie_rating = 4.5
if movie_rating >= 4.5:
    rating = 'Excellent'
elif movie_rating >= 3.5:
    rating = 'Good'
elif movie_rating >= 2.5:
    rating = 'Average'
elif movie_rating >= 1.5:
    rating = 'Poor'
else:
    rating = 'Terrible'
print(f"Movie Rating: {movie_rating}, Rating Description: {rating}")
# Output: Movie Rating: 4.5, Rating Description: Excellent

# Example 7: BMI Classification
bmi = 22.5
if bmi < 18.5:
    category = 'Underweight'
elif bmi < 24.9:
    category = 'Normal weight'
elif bmi < 29.9:
    category = 'Overweight'
else:
    category = 'Obesity'
print(f"BMI: {bmi}, Category: {category}")
# Output: BMI: 22.5, Category: Normal weight

# Example 8: Shipping Cost Calculation
weight = 12  # in pounds
if weight <= 5:                                                                             
    cost = 5.00
elif weight <= 20:
    cost = 10.00        
else:
    cost = 20.00
print(f"Weight: {weight} lbs, Shipping Cost: ${cost}")
# Output: Weight: 12 lbs, Shipping Cost: $10.0

# Example 9: Loan Eligibility
income = 45000
credit_score = 680  
if income >= 50000 and credit_score >= 700:
    eligibility = 'Eligible for loan'
elif income >= 40000 and credit_score >= 650:
    eligibility = 'Maybe eligible for loan'
else:
    eligibility = 'Not eligible for loan'
print(f"Income: ${income}, Credit Score: {credit_score}, Loan Eligibility: {eligibility}")
# Output: Income: $45000, Credit Score: 680, Loan Eligibility: Maybe eligible for loan

# Example 10: Internet Speed Classification
speed = 75  # in Mbps
if speed < 25:
    speed_category = 'Slow'
elif speed < 100:
    speed_category = 'Average'
elif speed < 500:
    speed_category = 'Fast'
else:
    speed_category = 'Very Fast'
print(f"Internet Speed: {speed} Mbps, Category: {speed_category}")
# Output: Internet Speed: 75 Mbps, Category: Average

# End of TOPIC 4

# Example 11: CPU Performance Classification
cpu = 95

if cpu < 50:
    print("CPU is normal")
elif cpu < 80:
    print("CPU is high")
else:
    print("CPU is critical")
# Output: CPU is critical

# Example 12: Disk Space Warning
disk_space = 15 # in percentage
if disk_space > 80:
    print("Disk space is low")
elif disk_space > 50:
    print("Disk space is moderate")
else:
    print("Disk space is sufficient")
# Output: Disk space is sufficient

# Example 13: Water Quality Check
water_quality = 70 # in percentage
if water_quality >= 90:
    print("Water quality is excellent")
elif water_quality >= 70:
    print("Water quality is good")
elif water_quality >= 50:
    print("Water quality is fair")
else:
    print("Water quality is poor")
# Output: Water quality is good

# Example 14: Employee Performance Review
performance_score = 88  
if performance_score >= 90:
    performance = 'Outstanding'
elif performance_score >= 75:
    performance = 'Exceeds Expectations'
elif performance_score >= 60:
    performance = 'Meets Expectations'
else:
    performance = 'Needs Improvement'
print(f"Performance Score: {performance_score}, Performance Review: {performance}")
# Output: Performance Score: 88, Performance Review: Exceeds Expectations

# Example 15: Electricity Bill Calculation
units_consumed = 350
if units_consumed <= 100:
    bill_amount = units_consumed * 0.5
elif units_consumed <= 300:
    bill_amount = (100 * 0.5) + (units_consumed - 100) * 0.75
else:
    bill_amount = (100 * 0.5) + (200 * 0.75) + (units_consumed - 300) * 1.20
print(f"Units Consumed: {units_consumed}, Bill Amount: ${bill_amount:.2f}")
# Output: Units Consumed: 350, Bill Amount: $262.50

# End of TOPIC 4



























































































































