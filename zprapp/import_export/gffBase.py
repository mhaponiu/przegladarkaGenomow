import re
from formatInterface import FormatInterface
# from wyjatki import CheckError

class Gff(FormatInterface):

    def check(self, filename):
        for r in self._gen_record_from_file(filename):
            self._check_handle(r)

    # def _gen_record_from_file(self, filename):
    #     with open(filename, 'rt') as f:
    #         for line in f:
    #             record_tab = re.split(r'[\t\n]', line)[:-1]
    #             yield self.FormatRecord(*record_tab)

    def _gen_record_from_file(self, filename):
        # FIXME skopiowany kod dwukrotnie
        if filename.closed:
            with open(filename, 'rt') as f:
                for line in f:
                    record_tab = re.split(r'[\t\n]', line)[:-1]
                    yield self.FormatRecord(*record_tab)
        else:
            for line in filename:
                record_tab = re.split(r'[\t\n]', line)[:-1]
                yield self.FormatRecord(*record_tab)

    # w sumie nie wiem czemu to nie dziala
    # def _gen_record_from_file(self, filename):
    #     def _handle(file):
    #         for line in file:
    #             record_tab = re.split(r'[\t\n]', line)[:-1]
    #             yield self.FormatRecord(*record_tab)
    #
    #     if filename.closed:
    #         with open(filename, 'rt') as f:
    #             _handle(f)
    #     else:
    #         _handle(filename)


    def export_records_from_db_to_file(self, filename, lista_master_id = None):
        with open(filename, 'wt') as f:
            for record in self._gen_record_from_db(lista_master_id):
                for r in record:
                    f.write(unicode(r))
                    f.write('\t')
                f.seek(f.tell()-1)
                f.write('\n')
