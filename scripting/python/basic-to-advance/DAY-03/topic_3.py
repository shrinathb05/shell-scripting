
## 🔹 TOPIC 3: Checking Disk Usage (REAL TASK)

# ```python
import subprocess

disk = subprocess.getoutput("df -h /")
print(disk)
# ```

# ---
# ## 🔹 EXPLANATION:
# - We use the `subprocess` module to run the `df -h /` command, which displays disk usage information for the root filesystem.
# - The output of the command is captured as a single string and printed directly.
# - This demonstrates how to execute a Linux command from Python and display its output.    
# ---
# ## 🔹 OUTPUT
# - The output will show the disk usage statistics for the root filesystem in a human-readable format.
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       100G   60G   40G  60% /

# ---
# ## 🔹 ADDITIONAL NOTES
# - You can modify the command to check disk usage for different filesystems by changing the path after `df -h`.    
# ---
# ## 🔹 END OF TOPIC 3: