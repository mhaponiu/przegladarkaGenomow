# TODO wywalic ten blok importow
import sys
import os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Meaning

class MeaningImpExp(Gff):
    def __init__(self):
        super(MeaningImpExp, self).__init__(namedtuple('MeanGff', ['id', 'mean']))

    def _gen_record_from_db(self, lista_id):
        if lista_id == None:
            means = Meaning.objects.all()
        else:
            means = Meaning.objects.filter(id__in = lista_id)
        for m in means.iterator():
            yield self.FormatRecord(m.id, m.mean)


if __name__ == "__main__":
    a = MeaningImpExp()
    # for  bbb in a._gen_record_from_db():
    #     print bbb
    a.export_records_from_db_to_file("exported_data/mean.gff")
    for b in a._gen_record_from_file("exported_data/mean.gff"):
        print b