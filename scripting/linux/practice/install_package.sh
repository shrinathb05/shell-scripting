#!/bin/bash
udpate_pkg() {
    $(sudo apt update -y)
}
upgrade_pkg() {
    $(sudo apt upgrade -y)
}

install_tools() {
    $(sudo apt install net-tools wget tar zip curl -y )
}

nginx_server() {
    sudo apt install nginx -y
}

udpate_pkg
upgrade_pkg
install_tools
nginx_server
