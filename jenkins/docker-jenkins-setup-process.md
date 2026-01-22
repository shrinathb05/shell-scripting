# Add docker in jenkins
# install docker cloudbees build and push plugin
# add in biuld step the docker build and push
1. add the username and password
2. create a access token in dockerhub
3. In jenkins stage docker Build and Publish step add 
    - username with image name eg.(shrinath05/dotnet-project2)
    - regeistry credentials add create username and password and add it over here
3. add a bind secret text as username and password
    # Username :- DOCKER_HUB_USER
    # Password :- DOCKER_HUB_PASSWORD
    # select your credentials that you have added
4. login to docker first via execute shell if getting error to connecting docker hub
    # echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USER --password-stdin
    Inside the Jenkins container:

    Check if you can ping Google: ping -c 3 google.com

    If it fails, edit the DNS config:

    Bash

    # Inside the container
        nano /etc/resolv.conf
        Add these lines (Google's Public DNS):

        Plaintext

        nameserver 8.8.8.8
        nameserver 8.8.4.4
        Try the docker login again.
    
    #Edit the Docker config: nano /etc/docker/daemon.json

        Add the MTU setting:

        JSON

        {
          "mtu": 1450,
          "storage-driver": "fuse-overlayfs" 
        }
        (Note: keep your storage-driver setting from the previous step if you added it).

        Restart Docker: systemctl restart docker
        
        
        Edit the Docker config: nano /etc/docker/daemon.json

        Add the MTU setting:

        JSON

        {
          "mtu": 1450,
          "storage-driver": "fuse-overlayfs" 
        }
        (Note: keep your storage-driver setting from the previous step if you added it).

        Restart Docker: systemctl restart docker
        
        
        1. Enabling Firewall/Forwarding on the Host

On Ubuntu, the firewall (UFW) sometimes blocks "forwarding" traffic, which prevents containers from reaching external sites like Docker Hub.

Run these commands on your Main Host:

Allow Forwarding in UFW: Open the UFW configuration:

Bash

sudo nano /etc/default/ufw
Change DEFAULT_FORWARD_POLICY from "DROP" to "ACCEPT":

Plaintext

DEFAULT_FORWARD_POLICY="ACCEPT"
Enable IPv4 Forwarding in the Kernel:

Bash

sudo sysctl -w net.ipv4.ip_forward=1
Reload the Firewall:

Bash

sudo ufw reload
Allow the LXC Bridge specifically: Assuming your LXC bridge is named lxdbr0 (check with ip addr), allow traffic from it:

Bash

sudo ufw allow in on lxdbr0
sudo ufw allow out on lxdbr0
2. Fixing the Docker Restart Issue
If Docker won't start after the MTU change, the daemon.json file is likely broken. Let's fix it manually.

Inside the Jenkins Container:

Check for errors: Run journalctl -u docker to see exactly why it failed. Usually, it's a "failed to parse json" error.

Rewrite the config correctly: Run this command to overwrite the file with a perfectly formatted version:

Bash

cat <<EOF > /etc/docker/daemon.json
{
  "mtu": 1400,
  "storage-driver": "fuse-overlayfs"
}
EOF
Note: Ensure there is no extra comma after the last line.

Reload and Start:

Bash

systemctl daemon-reload
systemctl restart docker
3. Verification Steps
Once the firewall is open and Docker is back up, perform these three tests in order inside the container:

DNS Check: host google.com (If this fails, it's a DNS issue).

Ping Check: ping -c 3 8.8.8.8 (If this fails, it's a routing/firewall issue).

SSL/Docker Check: curl -I https://registry-1.docker.io/v2/ (If this hangs, it's still an MTU issue).

You told Docker to use the fuse-overlayfs storage driver in the daemon.json file, but the actual software package is not installed inside your Jenkins container.

The Fix: Install the missing driver
Run these commands inside your Jenkins container:

Install the driver:

Bash

apt update
apt install fuse-overlayfs -y
Restart Docker:

Bash

systemctl restart docker
Check Status:

Bash

systemctl status docker
If it still fails (The "Alternative" Fix)
If you don't want to use fuse-overlayfs, you can revert to the standard driver, but only if you have enabled nesting on the LXC host as we discussed earlier.

Edit the config: nano /etc/docker/daemon.json

Change it to look like this:

JSON

{
  "mtu": 1400
}
(Removing the storage-driver line allows Docker to pick the best available one automatically).

Restart Docker: systemctl restart docker

Why the logs were "Repeating too quickly"
You saw the message Start request repeated too quickly. This is a safety feature of Linux (systemd). When a service crashes immediately 3 or 4 times in a row, Linux stops trying to start it to save your CPU.

Once you install fuse-overlayfs, the next systemctl restart docker will reset this counter and it should stay running.

📊 Current Status of your 12GB Host
Jenkins: Running (but Docker was crashing).

Tomcat: Running.

RAM: You are still in great shape; installing fuse-overlayfs uses almost no RAM, only a few KB of disk space.
