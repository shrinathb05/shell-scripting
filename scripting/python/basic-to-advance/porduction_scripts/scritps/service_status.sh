#!/bin/bash

service="nginx"

if ! systemctl is-active --quiet $service;then
    echo "$service is down!"
    echo "$service is starting"
    systemctl start nginx
else
    echo "Service is running fine!"
fi