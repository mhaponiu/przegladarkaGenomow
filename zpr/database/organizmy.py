# TODO class organizmy
from dbbase import *
from zprapp.models import Organism
import psycopg2
import psycopg2.extras

class Organisms(DBBase):
    def glos(self):
        print 'Organizmy! '

    def create(self):
        for i in range(1, 4):
            o = Organism(name = "organizm " + str(i))
            o.save();
        print "utworzono organizmy"


    def delete(self):
        orgs = Organism.objects.all();
        for o in orgs:
            o.delete()
        print "usunieto organizmy"
