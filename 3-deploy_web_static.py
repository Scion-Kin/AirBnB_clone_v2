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

    unzipped = archive_path[0:-4]
    co0 = put(archive_path, '/tmp/')

    co1 = run('tar -xvzf /tmp/{} -C /data/web_static/releases/'.format(
        archive_path))

    co2 = run('rm -r /tmp/{}'.format(archive_path))

    co3 = run('ln -fs /data/web_static/releases/{}\
                /data/web_static/current'.format(unzipped))

    if co0.failed or co1.failed or co2.failed or co3.failed:
        return False

    else:
        return True


def deploy():
    ''' This function calls the previous methods for deployment '''
    try:
        arch_file = do_pack()

        if arch_file is None:
            return False

        return do_deploy(arch_file)

    except Exception:
        return False
