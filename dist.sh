#!/usr/bin/bash
# distributeas an archive file to my servers

set -e

scp -i ~/.ssh/id_rsa web_static.tgz "ubuntu@52.91.146.189:/tmp/"
ssh ubuntu@52.91.146.189 "tar -xzf /tmp/web_static.tgz -C /data/web_static/releases/"
ssh ubuntu@52.91.146.189 "ln -fs /data/web_static/releases/web_static /data/web_static/current && ls -l /data/web_static/ && sudo service nginx restart"
