import os
import random
import re

from build_tools.build import AppBuilder
from zpr.settings import BASE_DIR


class Deployer(object):
    def __init__(self, conf):
        self.conf_json = AppBuilder.JSON_NAME
        print self.conf_json

    @staticmethod
    def gen_nginx_conf_string(www_srv_port, srv_host, static_root, unix_socket):
        nginx_template_path = os.path.join(BASE_DIR, 'build_tools', 'deploy_conf_files', 'nginx_template.conf')
        with open(nginx_template_path, 'rt') as file:
            nginx_generated = file.read().format(www_srv_port=www_srv_port, srv_host=srv_host,
                                                 static_root=static_root, unix_socket=unix_socket)
        return nginx_generated

    @staticmethod
    def upstart_conf(self):
        pass

    @staticmethod
    def new_secret_key_django():
        set_path = os.path.join(BASE_DIR,'zpr','settings.py')
        with open(set_path, 'rt') as file:
            old_settings = file.read()
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        new_key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        new_settings = re.sub('(?<=SECRET_KEY = ).+', '\''+new_key+'\'', old_settings, count=1)
        with open(set_path, 'wt') as file:
            file.write(new_settings)



    @staticmethod
    def django_allowed_host_add(host=None):
        set_path = os.path.join(BASE_DIR,'zpr','settings.py')
        with open(set_path, 'rt') as file:
            old_settings = file.read()
        if host == None:
            new_settings = re.sub('(?<=ALLOWED_HOSTS = ).+', '[]', old_settings, count=1)
        else:
            new_settings = re.sub('(?<=ALLOWED_HOSTS = ).+', '[\''+host+'\']', old_settings, count=1)
        with open(set_path, 'wt') as file:
            file.write(new_settings)