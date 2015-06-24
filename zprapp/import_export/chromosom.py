# TODO wywalic ten blok importow
import sys
import os

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Organism, Chromosome
from wyjatki import CheckError

class Chromosom(Gff):
    def __init__(self):
        super(Chromosom, self).__init__(namedtuple('ChrGff', ['id', 'number', 'length', 'organism_id']))

    def _check_handle(self, record):
        try:
            int(record.id)
            int(record.number)
            int(record.length)
            int(record.organism_id)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca chromosomy")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None:
            chrms = Chromosome.objects.all()
        else:
            chrms = Chromosome.objects.filter(organism_id__in = lista_master_id)
        for ch in chrms.iterator():
            yield self.FormatRecord(ch.id, ch.number, int(ch.length), ch.organism_id)


if __name__ == "__main__":
    a = Chromosom()
    # a.export_records_from_db_to_file("exported_data/aaa.gff")
    # for b in a._gen_record_from_file("exported_data/aaa.gff"):
    #     print b
    a.check("exported_data/chr.gff")