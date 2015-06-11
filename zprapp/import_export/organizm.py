# TODO wywalic ten blok importow
import sys
import os

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Organism

class Organizm(Gff):
    def __init__(self):
        super(Organizm, self).__init__(namedtuple('OrgGff', ['id', 'name']))

    def _gen_record_from_db(self, lista_id):
        if lista_id == None: orgs = Organism.objects.all()
        else: orgs = Organism.objects.filter(id__in = lista_id)
        for o in orgs.iterator():
            yield self.FormatRecord(o.id, o.name)


if __name__ == "__main__":
    a = Organizm()
    r = a.FormatRecord("777", "ogranizmmmmm")
    # for  bbb in a._gen_record_from_db():
    #     print bbb
    a.export_records_from_db_to_file("exported_data/aaa.gff")
    for b in a._gen_record_from_file("exported_data/aaa.gff"):
        print b