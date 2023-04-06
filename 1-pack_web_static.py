#!/usr/bin/env python3
"""
This module contains a Fabric script that generates a .tgz archive from
the contents web_static of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo.
    """
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "versions/web_static_{}.tgz".format(current_time)
    local("mkdir -p versions")
    try:
        local("tar -cvzf {} web_static".format(archive_name))
        print("web_static packed: {} -> {}Bytes"
              .format(archive_name, os.path.getsize(archive_name)))
        return archive_name
    except Exception as e:
        print("An error occurred:", e)
        return None
