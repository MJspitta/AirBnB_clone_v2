#!/usr/bin/python3
""" distributes arcive to web servers using do_deploy """
from fabric.api import run, put, env
import os


def do_deploy(archive_path):
    """ uncompress and deploy archive into servers """
    env.hosts = ['54.162.95.23', '52.201.219.244']
    if os.path.exists(archive_path) is False:
        return False
    dpath = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = dpath + name

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('sudo rm -f /tmp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
