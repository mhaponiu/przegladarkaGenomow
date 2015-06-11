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

class MarkerImpExp(Gff):
    def __init__(self):
        super(MarkerImpExp, self).__init__(namedtuple('MarkerGff', ['id', 'name', 'start', 'length', 'chromosome_id', 'meaning_id']))

    def _gen_record_from_db(self, lista_id):
        if lista_id == None:
            mrkrs = Marker.objects.all()
        else:
            mrkrs = Marker.objects.filter(chromosome_id__in = lista_id)
        for m in mrkrs.iterator():
            yield self.FormatRecord(m.id, m.name, int(m.start), int(m.length), m.chromosome_id, m.meaning_id)


if __name__ == "__main__":
    a = MarkerImpExp()
    # for  bbb in a._gen_record_from_db():
    #     print bbb
    a.export_records_from_db_to_file("exported_data/marker.gff")
    for b in a._gen_record_from_file("exported_data/marker.gff"):
        print b