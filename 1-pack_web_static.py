#!/usr/bin/python3
''' This is a fabric file that sets up a tar archive '''

from datetime import datetime
from fabric.api import local
import os


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
