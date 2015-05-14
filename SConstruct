# -*- mode: Python; -*-
import os, platform

#web
WWW_BROWSER_WINDOWS='chrome'
WWW_BROWSER_LINUX='google-chrome'
WEB_SRV_HOST = '127.0.0.1'
WEB_SRV_PORT = '8000'
WEB_CLIENT_HOST = '127.0.0.1'
WEB_CLIENT_PORT = '8000'
WEB_CLIENT_START_PATH ='/zprapp/'

Export('WWW_BROWSER_WINDOWS WWW_BROWSER_LINUX')
Export('WEB_CLIENT_HOST WEB_CLIENT_PORT')

# mozliwosci uruchomienia
vars = Variables('custom.py')
vars.Add(BoolVariable('run','Ustaw na 1 aby uruchomic serwer', False) )
vars.Add(BoolVariable('build_db','Ustaw na 1 aby zbudowac baze od zera',False) )
vars.Add(BoolVariable('earse_db','Ustaw na 1 usunac wszystkie tabele',False) )
vars.Add(BoolVariable('backup_restore','Ustaw na 1 wczytac backup bazy',False) )

# srodowisko
env = Environment(variables=vars)

# pomoc
Help(vars.GenerateHelpText(env))

if (platform.system() == "Linux"):
    WWW_BROWSER = WWW_BROWSER_LINUX
    BROWSER_CMD = WWW_BROWSER_LINUX + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + WEB_CLIENT_START_PATH + ' &'
else:
    WWW_BROWSER = WWW_BROWSER_WINDOWS
    BROWSER_CMD = 'start "" ' + WWW_BROWSER_WINDOWS + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + WEB_CLIENT_START_PATH

if env['run'] == 1:
    os.system(BROWSER_CMD)
    os.system('python manage.py runserver')

elif (env['build_db'] == 1 or
      env['earse_db'] == 1 or
      env['backup_restore'] == 1):
    SConscript(['zpr/database/SConscript'], exports=['env']);

else:
    print "NIC NIE ROBIE!"