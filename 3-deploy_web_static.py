#!/usr/bin/python3
""" distribute archive to web servers using deploy """
import os
from datetime import datetime
from fabric.api import local, runs_once, put, env, run


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


def deploy():
    """compress and upload files to remote server """
    path = do_pack()
    print(path)
    if path is None:
        return False
    else:
        return do_deploy(path)


deploy()
