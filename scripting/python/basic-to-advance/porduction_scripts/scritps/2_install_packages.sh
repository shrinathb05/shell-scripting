#!/bin/bash

# Update and Update the package
sudo apt update -y && sudo apt upgrade -y

# Install the necessary tool when creating the vm server
sudo apt install wget vim curl tar zip net-tools -y
