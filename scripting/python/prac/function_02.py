#!/usr/bin/env python3
import subprocess

opsystem = subprocess.getoutput("uname")

# Defing a function to check the os name
def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to linux")
    elif opsystem == "Linux" or opsystem == "Mac":
        print("You are good to go")

for i in range(1,6):
    check_os(opsystem)
