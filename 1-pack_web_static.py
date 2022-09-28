#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local


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
