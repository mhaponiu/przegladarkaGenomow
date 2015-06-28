from formatInterface import FormatInterface
from functools import partial
import io
from zprapp.import_export.wyjatki import CheckError

class Fasta(FormatInterface):

    def check(self, filename):
        # for r in self._gen_record_from_file(filename):
        #     self._check_handle(r)
        n_record = 1;
        for r in self._gen_record_from_file(filename):
            try:
                self._check_handle(r)
            except CheckError as error:
                error.n_record = n_record
                raise error
            n_record+=1

    def _gen_record_from_file(self, filename):
        #FastaRecord = namedtuple('FastaRecord', ['id', 'sequence'])
        # FIXME skopiowany kod dwukrotnie
        if filename.closed:
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
                            yield self.FormatRecord(id, s.getvalue())
                        if line == '': break
                    except IndexError:
                        raise StopIteration
        else:
            filename.seek(0)
            line = filename.readline()
            while True:
                try:
                    if line[0] == '>':
                        id = line[1:-1]
                        s = io.StringIO()
                        while True:
                            line = filename.readline()
                            if line == '' or line[0] == '>': break
                            s.write(unicode(line[:-1]))
                        yield self.FormatRecord(id, s.getvalue())
                    if line == '': break
                except IndexError:
                    raise StopIteration

    def export_records_from_db_to_file(self, filename, line_len = 80, limit = -1, lista_master_id = None):
        with open(filename, 'wt') as f:
            OGRANICZENIE = 0
            for seq in self._gen_record_from_db(lista_master_id):
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
