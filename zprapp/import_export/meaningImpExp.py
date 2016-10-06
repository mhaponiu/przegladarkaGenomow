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
from wyjatki import CheckError

class MeaningImpExp(Gff):
    def __init__(self):
        super(MeaningImpExp, self).__init__(namedtuple('MeanGff', ['id', 'mean']))

    def _check_handle(self, record):
        try:
            int(record.id)
            str(record.mean)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca meaningi")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None:
            means = Meaning.objects.all()
        else:
            means = Meaning.objects.filter(id__in = lista_master_id)
        for m in means.iterator():
            yield self.FormatRecord(m.id, m.mean)


if __name__ == "__main__":
    a = MeaningImpExp()
    # a.export_records_from_db_to_file("exported_data/mean.gff")
    # for b in a._gen_record_from_file("exported_data/mean.gff"):
    #     print b
    a.check("exported_data/mean.gff")