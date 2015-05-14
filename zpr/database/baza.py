from organizmy import *
from chromosomy import *
from scaffoldy import *
from sekwencje import *
from markery import *
from znaczenia import *

'''
    nalezy wczytac backup bazy danych '17.11.2012-cucumber_plain.backup'
    do nowo utworzonej bazy i wpisac jej dane do ponizszego CONNECT_STRING'a
    oraz lokacje pliku xls z markerami podac do MARKER_FILE_LOCATION
'''
class DBBase(object):
    MARKER_FILE_LOCATION = "Cucumber_scaffold_markers.xls"
    CONNECT_STRING = "dbname='ogorek_roboczy' user='zpr' host='localhost' password='zpr'"

class DatabaseGenome(DBBase):
    def __init__(self):
        self._organizmy = Organisms()
        self._chromosomy = Chromosomes()
        self._scaffoldy = Scaffolds()
        self._sekwencje = Sequences()
        self._markery = Markery()
        self._znaczenia = Meanings()

    def glos(self):
        print 'DataBaseGenome'
        print 'MARKER_FILE_LOCATION: ', self.MARKER_FILE_LOCATION
        print 'CONNECT_STRING: ', self.CONNECT_STRING
        self._organizmy.glos()
        self._chromosomy.glos()
        self._scaffoldy.glos()
        self._sekwencje.glos()
        self._markery.glos()
        self._znaczenia.glos()

