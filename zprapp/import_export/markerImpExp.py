# TODO wywalic ten blok importow
import sys
import os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Chromosome, Marker
from wyjatki import CheckError


class MarkerImpExp(Gff):
    def __init__(self):
        super(MarkerImpExp, self).__init__(namedtuple('MarkerGff', ['id', 'name', 'start', 'length', 'chromosome_id', 'meaning_id']))

    def _check_handle(self, record):
        try:
            int(record.id)
            str(record.name)
            int(record.start)
            int(record.length)
            int(record.chromosome_id)
            int(record.meaning_id)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca markery")




    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None:
            mrkrs = Marker.objects.all()
        else:
            mrkrs = Marker.objects.filter(chromosome_id__in = lista_master_id)
        for m in mrkrs.iterator():
            yield self.FormatRecord(m.id, m.name, int(m.start), int(m.length), m.chromosome_id, m.meaning_id)


if __name__ == "__main__":
    a = MarkerImpExp()
    # a.export_records_from_db_to_file("exported_data/marker.gff")
    # for b in a._gen_record_from_file("exported_data/marker.gff"):
    #     print b
    a.check("exported_data/marker.gff")
