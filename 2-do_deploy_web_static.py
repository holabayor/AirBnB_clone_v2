#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import run, put, env
from pathlib import Path

env.user = 'ubuntu'
env.hosts = ['18.206.238.207', '44.197.196.98']


def do_deploy(archive_path):
    """
        Functon that distributes an archive to web servers

    Return:
            False if the file at the path archive_path doesn’t exist
    """
    if not Path(archive_path).exists():
        return False
    folder = Path(archive_path).stem
    filename = archive_path.split('/')[-1]
    if put(archive_path, '/tmp/{}'.format(filename)).failed is True:
        return False
    if run('mkdir -p /data/web_static/releases/{}\
            '.format(folder)).failed is True:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/\
            '.format(filename, folder)).failed is True:
        return False
    if run('rm /tmp/{}'.format(filename)).failed is True:
        return False
    if run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/\
            '.format(folder, folder)).failed is True:
        return False
    if run('rm -rf /data/web_static/current').failed is True:
        return False
    if run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(folder)).failed is True:
        return False
    print('New version deployed!')
    return True
