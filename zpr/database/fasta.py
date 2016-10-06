from formatInterface import FormatInterface
from collections import namedtuple
import io
from zprapp.models import Sequence
from functools import partial

class Fasta(FormatInterface):
    FastaRecord = namedtuple('FastaRecord', ['id', 'sequence'])

    def import_records_from_file_to_db(self, filename):
        for record in self._gen_record_from_file(filename):
            print record.id, record.sequence[:30], ". . . . .", record.sequence[-30:]
            #TODO zapisac record do bazy

    #generator zwracajacy krotke (id, sequence)
    def _gen_record_from_file(self, filename):
        #FastaRecord = namedtuple('FastaRecord', ['id', 'sequence'])
        with open(filename, 'rt') as f:
            line = f.readline()
            while True:
                try:
                    if line[0] == '>':
                        id = line[1:-1]
                        s = io.StringIO()
                        while True:
                            line = f.readline()
                            if line == '' or line[0] == '>': break
                            s.write(unicode(line[:-1]))
                        yield self.FastaRecord(id, s.getvalue())
                    if line == '': break
                except IndexError:
                    raise StopIteration

    def export_records_from_db_to_file(self, filename, line_len = 80, limit = -1):
        with open(filename, 'wt') as f:
            OGRANICZENIE = 0
            for seq in self._gen_record_from_db():
                #FIXME sztuczne ograniczenie, usunac je
                if OGRANICZENIE == limit: break
                OGRANICZENIE+=1

                sequence = io.StringIO(unicode(seq.sequence))
                f.write('>')
                f.write(str(seq.id))
                f.write('\n')
                seq_part = iter(partial(sequence.read, line_len), b'')
                for s in seq_part:
                    f.write(s)
                    f.write('\n')

    def _gen_record_from_db(self):
        seqs = Sequence.objects.all()
        for s in seqs.iterator():
            #FastaRecord = namedtuple('FastaRecord', ['id', 'sequence'])
            yield self.FastaRecord(s.id, s.sequence)
