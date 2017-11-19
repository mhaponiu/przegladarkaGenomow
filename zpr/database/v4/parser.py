import os
from collections import namedtuple

from zpr.database.v3.parser import Fasta
from zpr.settings import BASE_DIR


class Fasta_454(Fasta):
    FastaRecord_new = namedtuple('FastaRecord', ['id_from_file', 'id', 'sequence'])

    def generator(self):
        gen = self.gen_record_from_file(
            filename=os.path.join(BASE_DIR, '..', 'database', 'v4', '454.fasta')
        )
        for fasta_record in gen:
            new_fasta_record = self.new_FastaRecord(fasta_record)
            yield new_fasta_record
        # return ret

    @staticmethod
    def new_FastaRecord(old_fasta):
        new_id = int(old_fasta.id.lstrip('454contig').rstrip('.u'))
        ''':param old_fasta -- gdzie id to orginalne id z pliku fasta'''
        return Fasta_454.FastaRecord_new(id_from_file=old_fasta.id, id=new_id, sequence=old_fasta.sequence)