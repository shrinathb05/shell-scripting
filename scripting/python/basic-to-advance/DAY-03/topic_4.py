## 🔹 TOPIC 4: Loop + Condition (Production Pattern)

# ```python
import subprocess

lines = subprocess.getoutput("df -h").splitlines()

for line in lines:
    if "/dev" in line:
        print(line)
# ```
# ---
# ## 🔹 EXPLANATION
# - We use the `subprocess` module to run the `df -h` command, which displays disk usage information for all filesystems.
# - The output is split into individual lines using the `splitlines()` method.
# - We then loop through each line and check if it contains the string `"/dev", which typically indicates a physical disk.
# - If the condition is met, we print that line.
# - This pattern is useful for filtering command output based on specific criteria.    
# ---
# ## 🔹 OUTPUT:
# - The output will show only the lines from the `df -h` command that correspond to physical disks.
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       100G   60G   40G  60% /
# /dev/sdb1       200G  150G   50G  75% /data   
# ---
# ## 🔹 ADDITIONAL NOTES:
# - This approach can be extended to filter other types of output or apply more complex conditions.
# ---
# ## 🔹 END OF TOPIC 4:

