# TODO wywalic ten blok importow
import sys
import os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django
django.setup()

from fastaBase import Fasta
from collections import namedtuple
from zprapp.models import Sequence

class SekwencjaFastaImpExp(Fasta):
    def __init__(self):
        super(SekwencjaFastaImpExp, self).__init__(namedtuple('SeqFasta', ['id', 'sequence']))

    def import_records_from_file_to_db(self, filename):
        for record in self._gen_record_from_file(filename):
            print record.id, record.sequence[:30], ". . . . .", record.sequence[-30:]
            #TODO zapisac record do bazy

    def _gen_record_from_db(self, lista_id):
        if lista_id == None:
            seqs = Sequence.objects.all()
        else:
            seqs = Sequence.objects.filter(scaffold_id__in = lista_id)
        for s in seqs.iterator():
            yield self.FormatRecord(s.id, s.sequence)

if __name__ == "__main__":
    a = SekwencjaFastaImpExp()

    # a.export_records_from_db_to_file("exported_data/sekwencja.fasta", line_len=80, limit=3)
    # for b in a._gen_record_from_file("exported_data/sekwencja.fasta"):
    #     print b;
    a.import_records_from_file_to_db('exported_data/sekwencja.fasta')