import os, re
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
        new_id = int(old_fasta.id[9:-2])

        ''':param old_fasta -- gdzie id to orginalne id z pliku fasta'''
        return Fasta_454.FastaRecord_new(id_from_file=old_fasta.id, id=new_id, sequence=old_fasta.sequence)


class Gff_annotation_abinitio_ill1():
    FileGffRecord = namedtuple('FileGffRecord',
                               ['ctg', 'augustuts', 'type', 'start', 'end', 'cos3', 'direction', 'cos4', 'info'])
    GffRecord = namedtuple('GffRecord', ['ctg_id','type', 'start', 'end', 'info'])

    def generator(self):
        gen_from_file = self._gen_record_from_file(
            filename=os.path.join(BASE_DIR, '..', 'database', 'v4', 'annotation_abinitio_ill1.gff3')
        )
        for file_gff_record in gen_from_file:
            new_gff_record = self.new_GffRecord(file_gff_record)
            yield new_gff_record

    @staticmethod
    def new_GffRecord(file_gff):
        ctg_id = int(file_gff.ctg.lstrip('ctg'))
        file_info = file_gff.info.rstrip(';')
        file_info = file_info.split(';')
        info_tuples = [tuple(info.split('=')) for info in file_info]
        info_dict = dict(info_tuples)

        return Gff_annotation_abinitio_ill1.GffRecord(
            ctg_id=ctg_id,
            type=file_gff.type,
            start=int(file_gff.start),
            end=int(file_gff.end),
            info=info_dict
        )


    def _gen_record_from_file(self, filename):
        with open(filename, 'rt') as f:
            for line in f:
                record_tab = re.split(r'[\t\n]', line)[:-1]
                yield self.FileGffRecord(*record_tab)

