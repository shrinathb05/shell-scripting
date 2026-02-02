#!/bin/bash

# disk usage
disk=$(df -h /)

if disk > 80; then
    echo "High usage!..."
else
    echo "Normal usage"
fi