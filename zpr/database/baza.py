# from dbbase import DBBase
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
    (zajrzyj do klasy bazowej DBBase w dbbase.py)
'''

class DatabaseGenome(DBBase):
    def __init__(self, connect_string = None, marker_xls = None):
        if None not in [connect_string, marker_xls]:
            self.CONNECT_STRING = connect_string
            self.MARKER_FILE_LOCATION = marker_xls
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

    def create(self):
        print "trwa tworzenie danych..."
        self._organizmy.create()
        self._znaczenia.create()
        self._chromosomy.create()
        self._markery.create()
        self._scaffoldy.create()
        self._sekwencje.create()
        print "zakonczono tworzenie danych"

    def delete(self):
        print "trwa usuwanie danych..."
        self._sekwencje.delete()
        self._scaffoldy.delete()
        self._markery.delete()
        self._chromosomy.delete()
        self._znaczenia.delete()
        self._organizmy.delete()
        print "zakonczono usuwanie danych"