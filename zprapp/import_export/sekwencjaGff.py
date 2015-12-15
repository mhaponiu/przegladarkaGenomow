import os
import sys

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from gffBase import Gff
from collections import namedtuple
from zprapp.models import Sequence
from wyjatki import CheckError

class SekwencjaGff(Gff):
    def __init__(self):
        super(SekwencjaGff, self).__init__(namedtuple('SeqGff', ['id', 'scaffold_id']))

    def _check_handle(self, record):
        try:
            int(record.id)
            str(record.scaffold_id)
        except ValueError:
            raise CheckError("niepoprawna struktura pliku GFF opisujaca sekwencje")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None:
            seqs = Sequence.objects.all()
        else:
            seqs = Sequence.objects.filter(scaffold_id__in = lista_master_id)
        for s in seqs.iterator():
            yield self.FormatRecord(s.id, s.scaffold_id)

    def import_records_from_file_to_db(self, file, slownik):
        ret_slownik={}
        for record in self._gen_record_from_file(file):
            ret_slownik[str(record.id)] = slownik.scfld[str(record.scaffold_id)]
        return slownik._replace(seq=ret_slownik)

if __name__ == "__main__":
    a = SekwencjaGff()
    # a.export_records_from_db_to_file("exported_data/sekwencja.gff")
    # for b in a._gen_record_from_file("exported_data/sekwencja.gff"):
    #     print b
    a.check("exported_data/seq.gff")
