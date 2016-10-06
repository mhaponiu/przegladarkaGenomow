import os
import sys

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
import django

django.setup()

from fastaBase import Fasta
from collections import namedtuple
from zprapp.models import Sequence
from wyjatki import CheckError
import re


class SekwencjaFastaImpExp(Fasta):
    def __init__(self):
        super(SekwencjaFastaImpExp, self).__init__(namedtuple('SeqFasta', ['id', 'sequence']))
        self.regex = re.compile('[ATGCN]*$')

    # def import_records_from_file_to_db(self, file, slownik):
    #     for record in self._gen_record_from_file(file):
    #         print record.id, record.sequence[:30], ". . . . .", record.sequence[-30:]
    #         return slownik
    #         #TODO zapisac record do bazy

    def import_records_from_file_to_db(self, file, slownik):
        ret_slownik = {}
        for record in self._gen_record_from_file(file):
            seq = Sequence(sequence=record.sequence, scaffold_id=slownik.seq[str(record.id)])
            seq.save()
            # nigdzie nie przekazuje tego slownika tak naprawde!
            ret_slownik[str(record.id)] = seq.id
        return slownik

    def _check_handle(self, record):
        try:
            int(record.id)
            # str(record.sequence)
            # if re.match('[ATGCN]*$', record.sequence) == None: raise ValueError
            if self.regex.match(record.sequence) == None: raise ValueError
            # regex = re.finditer(r'(?![ATGCN]).', record.sequence)
            # try:
            #     if regex.next().group() is None: pass
            #     else: raise ValueError
            # except StopIteration:
            #     # trzeba ostatni znak sprawdzic dodatkowo bo regex go nie lapie
            #     pass
        except ValueError:
            raise CheckError("niepoprawna struktura pliku FASTA opisujaca sekwencje")

    def _gen_record_from_db(self, lista_master_id):
        if lista_master_id == None:
            seqs = Sequence.objects.all()
        else:
            seqs = Sequence.objects.filter(scaffold_id__in=lista_master_id)
        for s in seqs.iterator():
            yield self.FormatRecord(s.id, s.sequence)


if __name__ == "__main__":
    a = SekwencjaFastaImpExp()

    # a.export_records_from_db_to_file("exported_data/sekwencja.fasta", line_len=80, limit=3)
    # for b in a._gen_record_from_file("exported_data/sekwencja.fasta"):
    #     print b;
    # a.import_records_from_file_to_db('exported_data/seq.fasta')
    a.check("exported_data/seq.fasta")
    # for record in a._gen_record_from_file('exported_data/seq.fasta'):
    #     print record.id, record.sequence[:30], ". . . . .", record.sequence[-30:]
