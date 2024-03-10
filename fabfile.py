#!/usr/bin/python3
''' This is a fabric file that deploys versions to remote servers'''

from datetime import datetime
from fabric.api import *
import os


def do_deploy(archive_path):
    env.hosts = ['54.175.223.158', '52.91.131.105']

    if not os.path.exists(archive_path):
        return False

    co0 = put(archive_path, '/tmp/')

    co1 = sudo('tar -xvzf /tmp/{} -C /data/web_static/releases/'.format(
        archive_path))

    # remove archive from server
    co2 = sudo('rm -r /tmp/{}'.format(archive_path))

    # delete symlink, make new
    co4 = sudo('rm -r /data/web_static/current')
    co4 = sudo('ln -s /data/web_static/current\
                /data/web_static/releases/')

    if co0.failed or co1.failed or co2.failed or co4.failed or co4.failed:
        return False

    else:
        return True
