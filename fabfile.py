#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import env

env.hosts = ['54.144.138.53', '35.168.7.192']


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.

    Args:
      archive_path: The path to the archive to deploy.

    Returns:
      True if the deployment was successful, False otherwise.
    """
    if archive_path:
        """ Upload archive to /tmp/ """

        put(archive_path, '/tmp/')

        run('tar -xzf /tmp/{} -C /data/web_static/releases/'.format(archive_path))

        run('rm /tmp/{}'.format(archive_path))

        run('rm -rf /data/web_static/current')

        run(f'ln -s /data/web_static/releases/{archive_path} /data/web_static/current')

        return True
    else:
        return False
