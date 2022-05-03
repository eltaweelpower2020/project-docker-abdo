####  # !/usr/bin/env bash
#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get -y install --reinstall make
sudo apt-get -y install curl

# curl -fsSL https://get.docker.com -o get-docker.sh
# sh get-docker.sh
# sudo usermod -a -G docker $(whoami)
# sudo service docker start

# sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose

# sudo apt-get -y install haveged
# sudo DAEMON_ARGS="-w 1024"
# sudo update-rc.d haveged defaults


sudo apt-get install git
sudo snap install core 
sudo snap refresh core
sudo apt-get remove certbot
sudo dnf remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo snap set certbot trust-plugin-with-root=ok
sudo certbot certonly --standalone

# certbot certonly \
#   --dns-digitalocean \
#   --dns-digitalocean-credentials ~/.secrets/certbot/digitalocean.ini \
#   -d flower-ghost.online \
#   -d www.flower-ghost.online

# sudo snap install "certbot-dns-flower-ghost.online"

sudo certbot renew --dry-run

# sudo git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt

# sudo cd /opt/letsencrypt
# sudo ./letsencrypt-auto certonly --standalone -d flower-ghost.online -d www.flower-ghost.online