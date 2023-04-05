from fabric.api import *
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo.
    """
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None
