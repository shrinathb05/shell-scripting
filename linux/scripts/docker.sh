#!/bin/bash

package_installation() {
	sudo apt update -y
	sleep 3
}
echo "************************ DEPLOYMENT in progress ***************************************"
sleep 3s
project_setup() {
	wget https://www.tooplate.com/zip-templates/2106_soft_landing.zip
	unzip 2106_soft_landing.zip
	sleep 3s
	mv 2106_soft_landing /var/www/html/
	#cd webapp
	sleep 3s
	rm -rf 2106_soft_landing.zip
	sleep 3s

}
<<'COMMENT'
#docker_setup() {
	echo "Creating Docker File.........................."
	sleep 3s	
	
	
	echo "
			FROM nginx:alpine
			COPY . /usr/share/nginx/html/
		" >> Dockerfile
	sleep 3s	
	
	
	echo "Docker File Created SUCCESSFULLY......................."
	docker build -t web:03 .
	sleep 2
	
	echo "Image successfully build......................................."
	sleep 3s
	
	echo "Starting Docker Container........................................."
	sleep 3s
	docker run -d --rm -p 8083:80 --name webs web:03
	sleep 3
}
COMMENT
echo "************************ DEPLOYMENT STARTED ***************************************"
package_installation
project_setup
docker_setup

echo "************************ DEPLOYMENT DONE 	*****************************************"
