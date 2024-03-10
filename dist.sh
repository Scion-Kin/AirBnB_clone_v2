#!/usr/bin/bash
# distributeas an archive file to my servers

set -e

ssh ubuntu@52.91.131.105 "ln -fs /data/web_static/releases/web_static /data/web_static/current && ls -l /data/web_static/ && sudo service nginx restart"
ssh ubuntu@54.175.223.158 "ln -fs /data/web_static/releases/web_static /data/web_static/current && ls -l /data/web_static/ && sudo service nginx restart"
