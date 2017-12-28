import os, re, io
from collections import namedtuple
from zpr.settings import BASE_DIR


# lekko zmodyfikowana kopia zpr.database.v4.parser.Gff_annotation_abinitio_ill1
class Gff_annotation():
    FileGffRecord = namedtuple('FileGffRecord',
                               ['ctg', 'pasa', 'type', 'start', 'end', 'cos3', 'direction', 'cos4', 'info'])
    GffRecord = namedtuple('GffRecord', ['ctg_id','type', 'start', 'end', 'info'])

    def generator(self):
        print "Gff_annotation.generator start"
        # filename = os.path.join(BASE_DIR, '..', 'database', 'v4_refresh', 'annotation.gff3')  # todo uncomment me !
        filename = os.path.join(BASE_DIR, '..', 'database', 'v4_refresh', 'h30k_annotation.gff3') #todo it's for test
        # filename = os.path.join(BASE_DIR, '..', 'database', 'v4_refresh', 'h100_annotation.gff3')  # todo it's for test
        print filename

        gen_from_file = self._gen_record_from_file(filename=filename)
        for file_gff_record in gen_from_file:
            new_gff_record = self.new_GffRecord(file_gff_record)
            yield new_gff_record
        print "Gff_annotation.generator end"

    @staticmethod
    def new_GffRecord(file_gff):
        ctg_id = int(file_gff.ctg.lstrip('ctg'))
        file_info = file_gff.info.rstrip(';')
        file_info = file_info.split(';')
        info_tuples = [tuple(info.split('=')) for info in file_info]
        info_dict = dict(info_tuples)

        return Gff_annotation.GffRecord(
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



# lekko zmodyfikowany zpr.database.v3.parser.Fasta_B10v2_c_corr
class Fasta():
    FastaRecord = namedtuple('FastaRecord', ['ctg_id', 'id_from_file', 'sequence'])

    def gen_record_from_file(self, filename):
        with open(filename, 'rt') as f:
            line = f.readline()
            while True:
                try:
                    if line[0] == '>':
                        id_from_file = line[1:-1]
                        ctg_id = id_from_file.strip('ctg')
                        s = io.StringIO()
                        while True:
                            line = f.readline()
                            if line == '' or line[0] == '>': break
                            s.write(unicode(line[:-1]))
                        yield self.FastaRecord(int(ctg_id), id_from_file, s.getvalue())
                    if line == '': break
                except IndexError:
                    raise StopIteration

class Fasta_B10v2_c_corr(Fasta):
    def generator(self):
        return self.gen_record_from_file(filename=os.path.join(BASE_DIR, '..', 'database', 'v3',
                                                                    'B10v2_c_corr.fsa'))