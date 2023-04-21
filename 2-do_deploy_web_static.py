#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
import fabric
from fabric.api import put, run, env
from invoke import task
from os import path

env.user = 'ubuntu'
env.hosts = ['54.144.138.53', '35.168.7.192']


@task
def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run('mkdir -p /data/web_static/releases/{}/'.format(filename))

        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename, filename))

        run('rm -rf /tmp/{}.tgz'.format(filename))

        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename, filename))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(filename))

        print("New version deployed!")
        return True
    except Exception:
        return False
