# przegladarkaGenomow
<hr>
<h2>Wymagania:</h2>
<ul>
    <li><b>libpq-dev python-dev</b><br>
    </li>
    <li>
        <b>pip + virtualenv</b><br>
    </li>
    <li>
        <b>scons</b>
    </li>
    <li>
        <b>postgresql</b>
    </li>
    <li>
        <b>nginx</b>
    </li>
    <br>
    sudo apt-get install libpq-dev python-dev python-pip scons postgresql nginx <br>
    sudo pip2 install virtualenv
    <br><br>
    <li>
    używane narzędzia, biblioteki (zostaną doinstalowane przy pierwszym budowaniu):<br>
    <i>django, gunicorn, psycopg2</i> <br>
    </li>
</ul>

<h2>Inicjalizacja:</h2>
<ul>
    <li>
        postgres: utworzenie uzytkownika <i><b>zpr</b></i>
        o haśle <i><b>zpr</b></i> <br>
        sudo -u postgres createuser --no-superuser --createdb --no-createrole zpr <br>
        sudo -u postgres psql -c "alter user zpr with encrypted password 'zpr';"        
    </li>
    <li>
        utworzenie baz danych <i><b>zpr</b></i> oraz <i><b>ogorek_roboczy</b></i> <br>
        sudo -u postgres createdb -O zpr zpr <br>
        sudo -u postgres createdb -O zpr ogorek_roboczy
    </li>
    <li>
        przetestuj połączenie <i>psql zpr -U zpr <i/><br>
        <i>
            jeśli error "psql: FATAL:  Peer authentication failed for user "zpr""<br>
            zedytuj plik /etc/postgresql/9.1/main/pg_hba.conf <br>
            w linijce "local all all peer" zmień 'peer' na 'md5'. <br>
            zrestartuj serwer:  #/etc/init.d/postgresql restart
        </i>
    </li>
    <li>
        wczytaj baze danych ogorek_roboczy poleceniem <b><i>scons restore_ogorek_roboczy=1</i></b>
    </li>
    <li>
        zbuduj baze od zera poleceniem <b><i>scons build_db=1</i></b>
    </li>
</ul>

<h2>Polecenia:</h2>
Aby uzyskać pomoc w budowaniu:  <b><i>scons -h</i></b>