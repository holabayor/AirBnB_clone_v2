#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local, run, put, env
from pathlib import Path

env.user = 'ubuntu'
env.hosts = ['18.206.238.207', '44.197.196.98']


def do_pack():
    """
    Method to archives generates a .tgz archive from the
    contents of the web_static folder

    Return: archive path if succesful otherwise return None
    """
    name = datetime.now()
    name = name.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + name + '.tgz'
    local("mkdir -p versions", capture=False)
    result = local("tar -cvzf {} web_static/".format(archive_path))

    if result.succeeded:
        return(archive_path)
    else:
        return


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


def deploy():
    """
        Function that creates and distributes and archive

        Return:
            False if no archive was created else
            the value of do_deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """
        Delete out of date archives
    """
    number = int(number)
    if number < 2:
        number = 1
    local('cd versions && ls | sort | head -n-{} \
            | xargs -r rm -r'.format(number))
    run('cd /data/web_static/releases/ && ls | sort \
            | head -n-{} | xargs rm -rf'.format(number))
