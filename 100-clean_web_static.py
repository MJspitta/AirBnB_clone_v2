#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that
deletes out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *
env.hosts = ['54.162.95.23', '52.201.219.244']


def do_clean(number=0):
    """ delete out-of-date archives """
    number = 1 if int(number) == 0 else int(number)
    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archive]

    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [a for a in archive if "web_static_" in a]
        [archive.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archive]
