
## 🔹 TOPIC 5: Service Status Check (Ubuntu)

# ```python
import subprocess

services = ["ssh", "cron", "nginx"]

for service in services:
    status = subprocess.getoutput(f"systemctl is-active {service}")
    print(f"{service}: {status}")
# ```

# ---
# ## 🔹 EXPLANATION:
# - We import the `subprocess` module to execute shell commands.
# - We define a list of services we want to check: `ssh`, `cron`, and `nginx`.
# - We loop through each service in the list.
# - For each service, we use `subprocess.getoutput()` to run the command `systemctl is-active <service>` and capture its output.
# - The output is then printed in a formatted string showing the service name and its status.   

# ---
# ## 🔹 OUTPUT:
# - The output will display the status of each specified service, indicating whether it is active, inactive, or failed.
# ssh: active
# cron: active
# nginx: inactive
# ---
# ## 🔹 ADDITIONAL NOTES:
# - You can modify the list of services to check the status of other services as needed.
# - Ensure you have the necessary permissions to check the status of services on your system.
# ---
# ## 🔹 END OF TOPIC 5: