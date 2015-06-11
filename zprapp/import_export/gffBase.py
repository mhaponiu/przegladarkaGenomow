import re
from formatInterface import FormatInterface

class Gff(FormatInterface):
    def _gen_record_from_file(self, filename):
        with open(filename, 'rt') as f:
            for line in f:
                record_tab = re.split(r'[\t\n]', line)[:-1]
                yield self.FormatRecord(*record_tab)


    def export_records_from_db_to_file(self, filename, lista_id = None):
        with open(filename, 'wt') as f:
            for record in self._gen_record_from_db(lista_id):
                for r in record:
                    f.write(unicode(r))
                    f.write('\t')
                f.seek(f.tell()-1)
                f.write('\n')
