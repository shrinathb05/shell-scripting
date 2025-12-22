#!/bin/bash

set -x
# Function to generate random password
generate_password() {
    # Define characters to use in the password
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+="

    # Generate password of given length
    length="$1"
    password=""
    for i in $(seq 1 "$length"); do
        password="$password${chars:RANDOM % ${#chars}:1}"
    done
    echo "$password"
}

# Prompt user for password length
read -p "Enter password length: " length

# Generate password
password=$(generate_password "$length")

echo "Generated Password: $password"
