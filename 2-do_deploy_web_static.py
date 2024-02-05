#!/usr/bin/python3
""" distributes arcive to web servers using do_deploy """
from fabric.api import run, put, env
import os
env.hosts = ['54.162.95.23', '52.201.219.244']


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
