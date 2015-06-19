# TODO wywalic ten blok importow
import sys
import os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Sequence

class SekwencjaGff(Gff):
    def __init__(self):
        super(SekwencjaGff, self).__init__(namedtuple('SeqGff', ['id', 'scaffold_id']))

    def _gen_record_from_db(self, lista_id):
        if lista_id == None:
            seqs = Sequence.objects.all()
        else:
            seqs = Sequence.objects.filter(scaffold_id__in = lista_id)
        for s in seqs.iterator():
            yield self.FormatRecord(s.id, s.scaffold_id)


if __name__ == "__main__":
    a = SekwencjaGff()
    # for  bbb in a._gen_record_from_db():
    #     print bbb
    a.export_records_from_db_to_file("exported_data/sekwencja.gff")
    for b in a._gen_record_from_file("exported_data/sekwencja.gff"):
        print b