
## Phase 1 Exercises (The Challenge)

# Complete these 15 exercises. You can write them in a single file called `phase1_practice.py` or separate files.

# 1. **Print** "Python is ready for DevOps!" to the console.

print("Python is ready for DevOps")

# 2. Create a variable `instance_id` with the value `"i-0abcd1234efgh5678"` and print its **type**.
instance_id = "i-0abcd1234efgh5678"

# 3. Assign `cpu_utilization = 45.5`. Convert it to an **integer** and print the result.
cpu_utilization = 45.5
print("The CPU Utilization is:", cpu_utilization)

# 4. Define `first_name = "Dev"` and `last_name = "Ops"`. Combine them into a variable `full_name` with a space in between.
first_name = "Dev"
last_name = "Ops"
full_name=(first_name + last_name)
print("The full name is : ", full_name)

# 5. Take the string `log_line = "ERROR: Disk Full"`. Extract/slice only the word `"ERROR"` from it.
log_line = "ERROR: Disk Full"
print(log_line[:5])

# 6. Use an **f-string** to print: "The service [service_name] is running on port [port_number]" using variables.
service="Nginx"
port=80
print(f"The {service} service is currently running on port {80}")

# 7. Check if the character `@` exists in the string `email = "admin@internal.local"`.
email="admin@internal.local"
print(email[5])

# 8. Create a variable `path = "/usr/local/bin"`. Use a string method to replace `local` with `bin`.
path="/usr/local/bin"
new_path=path.replace("local", "bin")
print(path)
print(new_path)

# 9. Given `raw_input = "  web-server-01  "`, remove the leading and trailing whitespace.



# 10. Split the string `csv_data = "node1,10.0.0.1,running"` into a list of 3 items.
# 11. Calculate the result of  (2 to the power of 8) to find the total IPs in a /24 subnet (roughly).
# 12. Create a variable `is_active = True`. Print its value and then negate it (flip it to False) and print again.
# 13. Take a user's name via `input()` and print it in **all uppercase**.
# 14. Create a multiline string (using triple quotes `"""`) that looks like a small config file.
# 15. Find the **index** of the word "failed" in the string: "Build status: failed. Please check logs."
