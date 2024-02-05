#!/usr/bin/python3
""" fabric script that generates .tgz archive """
from datetime import datetime
from fabric.api import *


def do_pack():
    """ make archive on web_static """
    format_time = "%Y%m%d%H%M%S"
    time_now = datetime.now()
    archive = "web_static_" + time_now.strftime(format_time) + ".tgz"
    archive_path = "versions/" + archive
    local('mkdir -p versions')
    create = local('tar -cvzf {} web_static'.format(archive_path))
    if create is not None:
        return archive
    else:
        return None
