#!/usr/bin/env bash
# Install nginx and create folders
# check nginx existence and install if it does not exist

nginx_check=$(whereis nginx | cut -d ":" -f 2| wc -w) > /dev/null
if [ "${nginx_check}" -le 1 ];
then
	sudo apt update
	sudo apt install -y nginx
	sudo service nginx start
else
	[ -d /data/web_static/releases/test ] || mkdir -p /data/web_static/releases/test
	[ -d /data/web_static/shared ] || mkdir -p /data/web_static/shared
	if [ -L /data/web_static/current ]; 
	then 
		rm /data/web_static/current
		ln -s /data/web_static/releases/test /data/web_static/current
	else
		ln -s /data/web_static/releases/test /data/web_static/current
	fi
	echo "Holberton School" > /data/web_static/releases/test/index.html
	chown -R ubuntu:ubuntu /data/
fi

# update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
# create a backup of config file
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

# add the location /hbnb_static/ { } block to the default Nginx configuration
sed -ie 's/^\tlocation \//\tlocation \/hbnb_static {\n\talias /data/web_static/current/' /etc/nginx/sites-available/default
	
