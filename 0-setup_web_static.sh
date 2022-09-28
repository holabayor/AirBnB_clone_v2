#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Create folders
mkdir -p data/web_static/releases/shared/
mkdir -p data/web_static/releases/test/

# Create a fake HTML file
sudo echo "Hello World" | sudo tee data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/current /data/web_static/releases/test/

# Give ownership of the folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve content of a dir
sed -i '44 a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
