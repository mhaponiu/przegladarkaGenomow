import os
import sys

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django

django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Chromosome
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
            chrms = Chromosome.objects.filter(organism_id__in=lista_master_id)
        for ch in chrms.iterator():
            yield self.FormatRecord(ch.id, ch.number, int(ch.length), ch.organism_id)

    def import_records_from_file_to_db(self, file, slownik):
        ret_slownik = {}
        for record in self._gen_record_from_file(file):
            chr = Chromosome(number=int(record.number), length=int(record.length),
                             organism_id=int(slownik.org[str(record.organism_id)]))
            chr.save()
            ret_slownik[str(record.id)] = chr.id
        # return ret_slownik
        return slownik._replace(chr=ret_slownik)


if __name__ == "__main__":
    a = Chromosom()
    # a.export_records_from_db_to_file("exported_data/aaa.gff")
    # for b in a._gen_record_from_file("exported_data/aaa.gff"):
    #     print b
    a.check("exported_data/chr.gff")
