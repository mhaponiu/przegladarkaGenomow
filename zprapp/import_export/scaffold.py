# TODO wywalic ten blok importow
import sys
import os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Scaffold, Chromosome
from wyjatki import CheckError

class ScaffoldImpExp(Gff):
    def __init__(self):
        super(ScaffoldImpExp, self).__init__(namedtuple('ScaffGff', ['id', 'length', 'order', 'start', 'chromosome_id']))

    def _check_handle(self, record):
        try:
            str(record.id)
            int(record.length)
            int(record.order)
            int(record.start)
            int(record.chromosome_id)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca scaffoldy")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None: scflds = Scaffold.objects.all()
        else: scflds = Scaffold.objects.filter(chromosome_id__in = lista_master_id)
        for s in scflds.iterator():
            yield self.FormatRecord(s.id, int(s.length), s.order, int(s.start), s.chromosome_id)


if __name__ == "__main__":
    a = ScaffoldImpExp()
    # a.export_records_from_db_to_file("exported_data/scaff.gff")
    # for b in a._gen_record_from_file("exported_data/scaff.gff"):
    #     print b
    a.check("exported_data/scaff.gff")