# -*- mode: Python; -*-
import os, platform

#web
WWW_BROWSER_WINDOWS='chrome'
WWW_BROWSER_LINUX='google-chrome'
WEB_SRV_HOST = '127.0.0.1'
WEB_SRV_PORT = '8000'
WEB_CLIENT_HOST = '127.0.0.1'
WEB_CLIENT_PORT = '8000'
WEB_CLIENT_START_PATH ='/zprapp'

Export('WWW_BROWSER_WINDOWS WWW_BROWSER_LINUX')
Export('WEB_SRV_HOST WEB_SRV_PORT WEB_CLIENT_HOST WEB_CLIENT_PORT')

vars = Variables('custom.py')
vars.Add(BoolVariable('run','Set to 1 to run application',0) )

env = Environment(variables=vars)

if (platform.system() == "Linux"):
    WWW_BROWSER = WWW_BROWSER_LINUX
    BROWSER_CMD = WWW_BROWSER_LINUX + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + WEB_CLIENT_START_PATH + ' &'
else:
    WWW_BROWSER = WWW_BROWSER_WINDOWS
    BROWSER_CMD = 'start "" ' + WWW_BROWSER_WINDOWS + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + WEB_CLIENT_START_PATH



if env['run'] == 1:
    os.system(BROWSER_CMD)
    os.system('python manage.py runserver')

