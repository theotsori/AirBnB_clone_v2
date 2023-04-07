#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api import env, run, put
import os

env.hosts = ['54.144.138.53', '35.168.7.192']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name_only = os.path.splitext(filename)[0]

    put(archive_path, '/tmp/{}'.format(filename))

    run('sudo mkdir -p /data/web_static/releases/{}/'.format(name_only))

    run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(filename, name_only))

    run('sudo rm /tmp/{}'.format(filename))

    run('sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(name_only, name_only))
    run('sudo rm -rf /data/web_static/releases/{}/web_static'
        .format(name_only))

    run('sudo rm -rf /data/web_static/current')

    run('sudo ln -s /data/web_static/releases/{}/ \
        /data/web_static/current'.format(name_only))

    print("New version deployed!")
    return True
