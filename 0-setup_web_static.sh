#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

#make folder

sudo mkdir -p /data/web_static/releases/test

# make another folder

sudo mkdir -p /data/web_static/shared

#html

echo "Tengo hambre" | sudo tee /data/web_static/releases/test/index.html

#Symbolic link

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#change owner

sudo chown -hR ubuntu:ubuntu /data/

# Update config

sudo sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart as always

sudo service nginx restart