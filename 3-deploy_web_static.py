#!/usr/bin/python3
''' comment '''


from fabric.api import run, put, env
import os
from os import path
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    ''' comment '''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except None:
        return None


env.hosts = ["35.196.242.112", "18.234.84.175"]


def do_deploy(archive_path):
    '''
    Distributes an archive to your web servers
    '''
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            filename = archive_path[9:]
            no_ext = filename[:-4]
            dir_name = '/data/web_static/releases/' + no_ext + '/'
            run('mkdir -p ' + dir_name)
            run('tar -xzf /tmp/' + filename + ' -C ' + dir_name)
            run('rm -f /tmp/' + filename)
            run('mv ' + dir_name + '/web_static/* ' + dir_name)
            run('rm -rf /data/web_static/current')
            run('ln -s ' + dir_name + ' /data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False


def deploy():
    ''' deploy function '''
    archive_path = do_pack()
    if path is None:
        return False
    return do_deploy(archive_path)
