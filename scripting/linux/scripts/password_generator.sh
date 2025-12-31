#!/bin/bash
set -x

#Password generator function
password_generator() {
	length="$1"
	password=""
	char_classes=("abcdefghijklmnopqrstuvwxyz" "1234567890" "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "~!@#$%^&*()_+{}:<>?/.,=-")
	char_count=${#char_classes[@]}

	for (( i=0; i<length; i++ ))
	do
		class_index=$((RANDOM % char_count))
		class=${char_classes[$class_index]}
		char_index=$((RANDOM % ${#class}))
		char=${class:$char_index:1}
		password=${password}${char}
	done

	echo "$Password"
}

#Length of the password
password_length=${1:-12}

#Generate Password
password=$(password_generator "$password_length")

echo "Generated Password: $password"
