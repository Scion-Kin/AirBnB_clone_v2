#!/usr/bin/python3
''' This is a fabric file that sets up a tar archive '''

from datetime import datetime


def do_pack():
    ''' This function creates an archive and stores it in versions folder '''

    now = datetime.now()
    arch_file = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(now.year, now.month, now.day,
                now.hour, now.minute, now.second)

    try:
        command = local('tar -cvzf {} web_static'.format(arch_file))

    except ImportError:
        pass

    return 'versions/{}'.format(arch_file)
