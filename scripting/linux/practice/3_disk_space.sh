#!/bin/bash

disk_usage=$(df -h)
mkdir -p /var/tmp/logs/
echo "The current disk space of each filesystem is: $disk_usage" >> /var/tmp/logs/disk_space.log

