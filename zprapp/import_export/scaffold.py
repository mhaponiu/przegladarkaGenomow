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

class ScaffoldImpExp(Gff):
    def __init__(self):
        super(ScaffoldImpExp, self).__init__(namedtuple('ScaffGff', ['id', 'length', 'order', 'start', 'chromosome_id']))

    def _gen_record_from_db(self, lista_id):
        if lista_id == None: scflds = Scaffold.objects.all()
        else: scflds = Scaffold.objects.filter(chromosome_id__in = lista_id)
        for s in scflds.iterator():
            yield self.FormatRecord(s.id, int(s.length), s.order, int(s.start), s.chromosome_id)


if __name__ == "__main__":
    a = ScaffoldImpExp()
    # for  bbb in a._gen_record_from_db():
    #     print bbb
    a.export_records_from_db_to_file("exported_data/scaff.gff")
    for b in a._gen_record_from_file("exported_data/scaff.gff"):
        print b