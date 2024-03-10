#!/usr/bin/env bash
# This script sets up a new nginx server to deploy a static file

apt-get update -y
apt-get install nginx -y

mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
#automatically created directories '/data/', '/data/web_static/' and '/data/web_static/releases'

echo "Holberton School" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
    # symbolic link removed if it exits
fi

ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

conf=\
"
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
"

sed -i "47i$conf" /etc/nginx/sites-enabled/default

service nginx restart
