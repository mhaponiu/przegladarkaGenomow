from formatInterface import FormatInterface
from collections import namedtuple
from zprapp.models import Sequence, Scaffold, Chromosome
import re


class Gff(FormatInterface):
    GffRecord = namedtuple('GffRecord', ['seq_id', 'start', 'length', 'order', 'master_seq_id'])

    def import_records_from_file_to_db(self, filename):
        for record in self._gen_record_from_file(filename):
            print record
            #TODO zapisac record do bazy

    def _gen_record_from_file(self, filename):
        with open(filename, 'rt') as f:
            for line in f:
                record_tab = re.split(r'[\t\n]', line)[:-1]
                yield self.GffRecord(*record_tab)


    def export_records_from_db_to_file(self, filename, limit=-1):
        with open(filename, 'wt') as f:
            ORGANICZENIE = 0
            for record in self._gen_record_from_db():
                #FIXME sztuczne ograniczenie, usunac je mozna
                if ORGANICZENIE == limit: break
                ORGANICZENIE+=1

                for r in record:
                    f.write(unicode(r))
                    f.write('\t')
                f.seek(f.tell()-1)
                f.write('\n')


    def _gen_record_from_db(self):
        seqs = Sequence.objects.all()
        for s in seqs.iterator():
            scfld = Scaffold.objects.get(id = s.scaffold_id)
            yield self.GffRecord(s.id, int(scfld.start), int(scfld.length), scfld.order, scfld.chromosome_id)