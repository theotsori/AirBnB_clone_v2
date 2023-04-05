#!/usr/bin/env bash
# Install nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html><head><title>Testing nginx configuration</title></head><body><p>Success!</p></body></html>" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the directories to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update nginx configuration
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart nginx
service nginx restart
