#!/usr/bin/env bash
# This script sets up a new nginx server to deploy a static file

apt-get update -y
apt-get install nginx -y

mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
#automatically created directories '/data/', '/data/web_static/' and '/data/web_static/releases'

echo "Holberton School" > /data/web_static/releases/test/index.html

# symbolic link removed if it exits and create new
rm -r /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-enabled/default
service nginx restart
