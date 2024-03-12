#!/usr/bin/python3
''' This is a fabric file that deploys versions to remote servers'''

from datetime import datetime
from fabric.api import run, put, env, local
import os

env.hosts = ['54.175.223.158', '52.91.131.105']
env.usr = 'ubuntu'


def do_pack():
    ''' This function creates an archive and stores it in versions folder '''

    if not os.path.exists('versions'):
        local('mkdir versions')

    now = datetime.now()
    arch_file = 'versions/web_static{}.tgz'.format(
        now.strftime("%Y%m%d%H%M%S")
    )

    command = local("tar -cvzf {} web_static".format(arch_file))
    if not command.failed:
        return arch_file


def do_deploy(archive_path):
    ''' Deploys a version to the web servers '''

    if not os.path.exists(archive_path):
        return False

    try:
        unzipped = archive_path[0:-4]
        put(archive_path, '/tmp/')

        run("mkdir /data/web_static/releases/new && tar -xvzf\
        /tmp/{} -C /data/web_static/releases/new/".format(
            archive_path))

        run("mv /data/web_static/releases/new/* /data/web_static/releases/{}"
            .format(unzipped))

        run('rm -r /tmp/{} && rm -r /data/web_static/releases/new/'
            .format(archive_path))
        run('rm -r /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
                    /data/web_static/current'.format(unzipped))

    except Exception:
        return False

    return True
