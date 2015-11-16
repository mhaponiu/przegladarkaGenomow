# -*- mode: Python; -*-
import sys, os, platform
from zpr.settings import BASE_DIR

#web
WWW_BROWSER_WINDOWS='chrome'
WWW_BROWSER_LINUX='google-chrome'
WEB_SRV_HOST = '127.0.0.1'
WEB_SRV_PORT = '8000'
WEB_CLIENT_HOST = '127.0.0.1'
WEB_CLIENT_PORT = '8000'
WEB_CLIENT_START_PATH ='/zprapp/'

#database files, backups
DATABASE_ROOT_FILES = os.path.abspath(os.path.join(BASE_DIR, '../database'))

Export('WWW_BROWSER_WINDOWS WWW_BROWSER_LINUX')
Export('WEB_CLIENT_HOST WEB_CLIENT_PORT')
Export('DATABASE_ROOT_FILES')

# mozliwosci uruchomienia
vars = Variables('custom.py')
vars.Add(BoolVariable('run','Ustaw na 1 aby uruchomic serwer', False) )
vars.Add(BoolVariable('build_db','Ustaw na 1 aby zbudowac baze od zera',False) )
vars.Add(BoolVariable('clear_db','Ustaw na 1 aby usunac dane ze wszystkich tabel',False) )
vars.Add(BoolVariable('restore_ogorek_roboczy','Ustaw na 1 aby wczytac backup bazy ogorek_roboczy',False) )
vars.Add(BoolVariable('test','Ustaw na 1 aby odpalic jakas testowa operacje',False) )

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


elif ( 1 in [ env['build_db'], env['clear_db'], env['test'], env['restore_ogorek_roboczy'] ]):

    if env['build_db'] == 1 or env['clear_db'] == 1:
        os.system('python manage.py migrate')

    # import ustawien django zeby mozna uzywac orm django do bazy danych
    # bez wywolywania django shell, tylko z poziomu np terminala
    sys.path.append([os.path.abspath('')])
    os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
    from django.conf import settings
    import django
    django.setup() #bez tego AppRegistryNotReady: Models aren't loaded yet.

    SConscript(['zpr/database/SConscript'], exports=['env']);

else:
    print "NIC NIE ROBIE!"