# -*- mode: Python; -*-
import sys, os, platform
from zpr.settings import BASE_DIR, STATIC_ROOT
from build_tools.build import AppBuilder
from build_tools.deploy import Deployer

# web
WWW_BROWSER_WINDOWS='chrome'
WWW_BROWSER_LINUX='google-chrome'

WEB_CLIENT_START_PATH =''

PROJECT_NAME = 'przegladarkaGenomow'

# nginx
WWW_SRV_HOST='192.168.0.16'
WWW_SRV_PORT='80'

WEB_CLIENT_PROD_HOST = WWW_SRV_HOST
WEB_CLIENT_PORT_PROD = '80'

WEB_SRV_PORT_LOCAL = '8000'

WEB_CLIENT_LOCAL_HOST = '127.0.0.1'
WEB_CLIENT_PORT_LOCAL = WEB_SRV_PORT_LOCAL

UNIX_SOCKET = 'unix:/tmp/{name}.socket'.format(name=PROJECT_NAME)


# database files, backups
DATABASE_ROOT_FILES = os.path.abspath(os.path.join(BASE_DIR, '../database'))
DB_FILES_URL = 'https://www.dropbox.com/sh/wuyvtb58okw91hy/AAAEbLbhVnTPceFBg-q0fNARa?raw=1'

VIRTUALENV_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../virtualenv'))
VIRTUALENV_PYTHON = os.path.join(VIRTUALENV_ROOT, 'bin', 'python')

#Export('WEB_CLIENT_HOST WEB_CLIENT_PORT')
Export('DATABASE_ROOT_FILES')

# mozliwosci uruchomienia
vars = Variables('custom.py')
vars.Add(EnumVariable('run','Uruchom serwer, l: lokalny, p: produkcyjny', 'no', allowed_values = ('l', 'p', 'no'), map={}, ignorecase=2) )
vars.Add(BoolVariable('build_db','Ustaw na 1 aby zbudowac baze od zera',False) )
vars.Add(BoolVariable('clear_db','Ustaw na 1 aby usunac dane ze wszystkich tabel',False) )
vars.Add(BoolVariable('restore_ogorek_roboczy','Ustaw na 1 aby wczytac backup bazy ogorek_roboczy',False) )
vars.Add(BoolVariable('build_deploy','[SUDO potrzebne] Ustaw na 1 aby skonfigurowac serwer www (nginx) i django do wdrozenia',False) )
vars.Add(BoolVariable('new_secret_key','Ustaw na 1 aby wygenerowac nowy klucz',False) )
vars.Add(EnumVariable('test','Uruchom testy, a: wszystkie, f: funkcjonalne, u: jednostkowe, c: calc_module', 'no', allowed_values = ('a', 'f', 'u', 'c', 'no'), map={}, ignorecase=2) )
help_clean = "\n'-c' aby wyczyscic zbudowane pliki c++"

# srodowisko
env = Environment(variables=vars)

# pomoc
Help(vars.GenerateHelpText(env) + help_clean + '\n')

if (platform.system() == "Linux"):
    WWW_BROWSER = WWW_BROWSER_LINUX
    if env['run'] == 'l':
        BROWSER_CMD = WWW_BROWSER_LINUX + ' http://' + WEB_CLIENT_LOCAL_HOST + ':' + WEB_CLIENT_PORT_LOCAL + WEB_CLIENT_START_PATH + ' &'
    elif env['run'] == 'p':
        BROWSER_CMD = WWW_BROWSER_LINUX + ' http://' + WEB_CLIENT_PROD_HOST + ':' + WEB_CLIENT_PORT_PROD + WEB_CLIENT_START_PATH + ' &'
else:
    WWW_BROWSER = WWW_BROWSER_WINDOWS
    BROWSER_CMD = 'start "" ' + WWW_BROWSER_WINDOWS + ' http://' + WEB_CLIENT_HOST + ':' + WEB_CLIENT_PORT + WEB_CLIENT_START_PATH

if env['run'] == 'l':
    os.system(BROWSER_CMD)
    os.system('{python} manage.py runserver {port}'.format(python=VIRTUALENV_PYTHON, port=WEB_SRV_PORT_LOCAL))

elif env['run'] == 'p':
    #os.system(BROWSER_CMD)
    os.system('{gunicorn} --bind {unix_socket} zpr.wsgi:application'.format(gunicorn= os.path.join(VIRTUALENV_ROOT, 'bin', 'gunicorn'), unix_socket=UNIX_SOCKET))

elif env['test'] == 'a':
    os.system('{python} manage.py test'.format(python=VIRTUALENV_PYTHON))

elif env['test'] == 'f':
    os.system('{python} manage.py test functional_tests'.format(python=VIRTUALENV_PYTHON))

elif env['test'] == 'u':
    os.system('{python} manage.py test zprapp'.format(python=VIRTUALENV_PYTHON))

elif env['test'] == 'c':
    from subprocess import call

    print "\n---------------------------------------------"
    print "Testy algorytmu BLAST\n"
    call('zprapp/calc/calc_webomics/build/tests/BLAST_Tests')
    print "\n---------------------------------------------"
    print "Testy algorytmu SW\n"
    call('zprapp/calc/calc_webomics/build/tests/SW_Tests')
    print "\n---------------------------------------------"
    print "Testy algorytmu KMP\n"
    call('zprapp/calc/calc_webomics/build/tests/KMP_Tests')
    print "\n---------------------------------------------"
    print "Testy algorytmu BM\n"
    call('zprapp/calc/calc_webomics/build/tests/BM_Tests')

elif ( 1 in [ env['build_db'], env['clear_db'], env['restore_ogorek_roboczy'] ]):

    if env['build_db'] == 1 or env['clear_db'] == 1:
        os.system('{python} manage.py makemigrations zprapp'.format(python= VIRTUALENV_PYTHON))
        os.system('{python} manage.py migrate zprapp'.format(python= VIRTUALENV_PYTHON))

    # import ustawien django zeby mozna uzywac orm django do bazy danych
    # bez wywolywania django shell, tylko z poziomu np terminala
    sys.path.append([os.path.abspath('')])
    os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
    sys.path.extend([os.path.join(VIRTUALENV_ROOT,'lib', 'python2.7', 'site-packages')])
    import django
    django.setup() #bez tego AppRegistryNotReady: Models aren't loaded yet.
    SConscript(['zpr/database/SConscript'], exports=['env']);

elif env['build_deploy'] == 1:
    if not os.path.exists(os.path.join(AppBuilder.JSON_DIR, AppBuilder.JSON_NAME)):
        print "Najpierw wykonaj budowanie programu poleceniem 'scons'"
    else:
        AppBuilder.django_debug(bool=False)
        Deployer.django_allowed_host_add(WWW_SRV_HOST)
        nginx_conf =  Deployer.gen_nginx_conf_string(WWW_SRV_PORT, WWW_SRV_HOST, STATIC_ROOT, UNIX_SOCKET)
        nginx_conf_target_path = '/etc/nginx/sites-available/{name}'.format(name=PROJECT_NAME)

        conf_json = AppBuilder.load_conf()
        if conf_json['deploy']['nginx_configurated'] == 0:
            os.system("echo '{conf}' > {target}".format(conf=nginx_conf, target=nginx_conf_target_path))
            os.system("ln -s {} /etc/nginx/sites-enabled".format(nginx_conf_target_path))
            os.system('service nginx reload')
            conf_json['deploy']['nginx_configurated'] = 1
            AppBuilder.save_conf(conf_json)
        else:
            print 'build_conf.json: Nginx juz zostal wczesniej skonfigurowany'

elif env['new_secret_key'] == 1:
    Deployer.new_secret_key_django()


else:
    print "\n******* Podstawowe budowanie aplikacji: *******"
    builder = AppBuilder(db_files_dir=DATABASE_ROOT_FILES,
                         virtenv_root=VIRTUALENV_ROOT,
                         static_root=STATIC_ROOT)
    builder.create_dir_structure()
    builder.download_and_unzip_db_files(url=DB_FILES_URL)
    builder.create_virtualenv()
    builder.install_pip_req()

    AppBuilder.django_debug(bool=True)
    Deployer.django_allowed_host_add()

    os.system('{python} manage.py collectstatic --noinput'.format(python=VIRTUALENV_PYTHON))

    print "\n******* Budowanie biblioteki C++ : *******"
    SConscript(['zprapp/calc/SConscript'], exports=['env']);

    print "\n******* Koniec podstawowego budowania aplikacji: *******"


