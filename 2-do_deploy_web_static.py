#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import env, put, run
import os

env.hosts = ['54.144.138.53', '35.168.7.192']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_filename = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + archive_filename.split(".")[0]
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(archive_filename, folder_name))

        run("sudo rm /tmp/{}".format(archive_filename))

        run("sudo rm -rf /data/web_static/current")

        run("sudo ln -s {} /data/web_static/current".format(folder_name))
        return True
    except:
        return False
