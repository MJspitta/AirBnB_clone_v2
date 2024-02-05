#!/usr/bin/python3
""" fabric script that generates .tgz archive """
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """ archives static files """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    timedate = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            timedate.year,
            timedate.month,
            timedate.day,
            timedate.hour,
            timedate.minute,
            timedate.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
