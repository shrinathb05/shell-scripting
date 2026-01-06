
# ## 🔹 TOPIC 2: Looping Over Linux Command Output

# ```python
import subprocess

files = subprocess.getoutput("ls").splitlines()

for file in files:
    print(f"Found file: {file}")

# ```

# ---
# ### Explanation:
# - We use the `subprocess` module to run the `ls` command, which lists files in the current directory.
# - The output of the command is captured as a single string, which we then split into individual lines using `splitlines()`.
# - We loop over each file name in the list and print it out.
# - This demonstrates how to execute a Linux command from Python and process its output line by line.   
# ---