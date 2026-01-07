#!/usr/bin/python3
# ## 🔹 TOPIC 1: Running Linux Commands from Python

## 🔹 TOPIC 1: Running Linux Commands from Python

### ✅ Method 1 (Modern & Recommended): `subprocess`

# ```python
import subprocess

output = subprocess.getoutput("uname -a")
print(output)

# ```

# ✔ Used in real DevOps automation
# ❌ `os.system()` is NOT recommended anymore
# ❌ `commands` module is deprecated since Python 2.6 and removed in Python 3   
# ❌ `subprocess` is more powerful and flexible
# ❌ `subprocess` can handle complex scenarios (piping, redirection, etc.)
# ❌ `subprocess` provides better error handling and security   
# ❌ `subprocess` is the preferred way to run shell commands in Python 3
# ```
### ✅ Method 2 (Deprecated): `os.system()`
# ```python
import os   
os.system("uname -a")
# ```
# ```
### ✅ Method 3 (Deprecated): `commands` module (Python 2 only)
# ```python
import commands
output = commands.getoutput("uname -a")
print(output)
# ```
# ```

# ✔ Used in legacy scripts
# ❌ Deprecated since Python 2.6 and removed in Python 3
# ❌ `subprocess` is the preferred way to run shell commands in Python 3
# ❌ `commands` module is less flexible and powerful compared to `subprocess`   
# ❌ `commands` module has limited error handling capabilities
# ❌ `commands` module is not secure for handling untrusted input
# ❌ `subprocess` can handle complex scenarios (piping, redirection, etc
# ❌ `subprocess` provides better error handling and security
# ```   
# ### ✅ Summary:
# - Use `subprocess` for running Linux commands from Python.
# - Avoid using `os.system()` and `commands` module in new code.
