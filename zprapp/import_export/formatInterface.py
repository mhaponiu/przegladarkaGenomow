class FormatInterface(object):
    def __init__(self, namedtuple):
        self.FormatRecord = namedtuple

    def import_records_from_file_to_db(self):
        pass;

    def _gen_record_from_file(self):
        pass

    def export_records_from_db_to_file(self, filename, lista):
        pass

    def _gen_record_from_db(self, lista):
        pass