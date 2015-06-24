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
from wyjatki import CheckError

class Organizm(Gff):
    def __init__(self):
        super(Organizm, self).__init__(namedtuple('OrgGff', ['id', 'name']))

    def _check_handle(self, record):
        try:
            int(record.id)
            str(record.name)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca organizmy")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None: orgs = Organism.objects.all()
        else: orgs = Organism.objects.filter(id__in = lista_master_id)
        for o in orgs.iterator():
            yield self.FormatRecord(o.id, o.name)


if __name__ == "__main__":
    a = Organizm()
    # r = a.FormatRecord("777", "ogranizmmmmm")
    # a.export_records_from_db_to_file("exported_data/aaa.gff")
    # for b in a._gen_record_from_file("exported_data/aaa.gff"):
    #     print b
    a.check("exported_data/org.gff")