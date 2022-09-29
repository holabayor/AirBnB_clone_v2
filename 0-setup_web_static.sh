#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install nginx
sudo apt update
sudo apt install -y nginx

# Create folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
sudo echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve content of a dir
sudo sed -i '44 a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
