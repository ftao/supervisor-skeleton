"""
Fabfile to install supervisor on debian 
"""
from __future__ import with_statement
from fabric.api import env, run,require, sudo, run, put, local, settings, cd
from fabric.contrib.files import upload_template, exists

def install():
    """
    install supervisor , make required folders
    """
    sudo('aptitude install -y python-setuptools')
    #simplejson speedup need these two
    sudo('easy_install pip')
    sudo('pip install supervisor')
    put("etc/supervisord.conf", "/etc/supervisord.conf", use_sudo=True)
    sudo("mkdir -p /etc/supervisor.d")
    put("etc/init.d/supervisord", "/etc/init.d/supervisord", use_sudo=True)
    sudo("chmod +x /etc/init.d/supervisord")
    sudo("update-rc.d supervisord defaults")

    sudo("mkdir -p /var/log/supervisor")
    sudo("mkdir -p /var/run/supervisor")

def start():
    sudo("/etc/init.d/supervisord start")

def stop():
    sudo("/etc/init.d/supervisord stop")

def restart():
    sudo("/etc/init.d/supervisord restart")
