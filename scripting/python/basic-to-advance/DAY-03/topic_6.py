## 🔹 TOPIC 6: Retry Logic (Linux + Python)

# ```python
import subprocess
import time

attempt = 1

while attempt <= 3:
    status = subprocess.getoutput("systemctl is-active nginx")

    if status == "active":
        print("Nginx is running")
        break

    print("Retrying...")
    time.sleep(2)
    attempt += 1
else:
    print("Nginx failed after retries as service is not active")
    print("Starting Nginx service.......")
    time.sleep(2)
    subprocess.getoutput("sudo systemctl start nginx")
    print("Nginx service started successfully")
# ```

# ---
# ## 🔹 EXPLANATION:
# - We import the `subprocess` and `time` modules.
# - We initialize a variable `attempt` to 1.
# - We enter a `while` loop that runs up to 3 times.
# - Inside the loop, we use `subprocess.getoutput()` to check the status of the Nginx service.
# - If the status is "active", we print a success message and break out of the loop.
# - If not, we print "Retrying..." and wait for 2 seconds before incrementing the attempt counter.
# - If all attempts fail, we print a failure message.
# ---
# ## 🔹 OUTPUT: 
# - The output will indicate whether Nginx is running or if it failed after retries.
# Nginx is running
# ---
# ## 🔹 ADDITIONAL NOTES:
# - You can adjust the number of retries and the delay between retries as needed.
# - Ensure you have the necessary permissions to check and manage services on your system.
# ---
# ## 🔹 END OF TOPIC 6:
