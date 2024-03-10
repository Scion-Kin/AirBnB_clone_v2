#!/usr/bin/python3
''' This is a fabric file that deploys versions to remote servers'''

from datetime import datetime
from fabric.api import run, put, env
import os
env.hosts = ['54.175.223.158', '52.91.131.105']
env.usr = 'ubuntu'


def do_deploy(archive_path):
    ''' Deploys a version to the web servers '''

    if not os.path.exists(archive_path):
        return False

    unzipped = archive_path[0:-4]
    co0 = put(archive_path, '/tmp/')

    co1 = run('tar -xvzf /tmp/{} -C /data/web_static/releases/'.format(
        archive_path))

    co2 = run('rm -r /tmp/{}'.format(archive_path))

    co4 = run('rm -r /data/web_static/current')
    co4 = run('ln -fs /data/web_static/current\
                /data/web_static/releases/{}'.format(unzipped))

    if co0.failed or co1.failed or co2.failed or co4.failed or co4.failed:
        return False

    else:
        return True
