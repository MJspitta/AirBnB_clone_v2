#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
import os
from fabric.api import env, local, put, run
from datetime import datetime
env.hosts = ['54.162.95.23', '52.201.219.244']

def do_pack():
    """ generate tgz archive """
    try:
        format_time = "%Y%m%d%H%M%S"
        date_now = datetime.now().strftime(format_time)
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        archive_n = "versions/web_static_{}.tgz".format(date_now)
        local("tar -cvzf {} web_static".format(archive_n))
        return archive_n
    except:
        return None

def do_deploy(archive_path):
    """ distributes archive to web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_n = archive_path.split("/")[-1]
        archive_f = "/data/web_static/releases/" + archive_n.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}/'.format(archive_f))
        run('tar -xzf /tmp/{} -C {}/'.format(archive_n, archive_f))
        run('rm /tmp/{}'.format(archive_n))
        run('mv {}/web_static/* {}/'.format(archive_f))
        run('rm -rf {}/web_static'.format(archive_f))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(archive_f))
        return True
    except:
        return False

def deploy():
    """ creates and distributes archive to web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
