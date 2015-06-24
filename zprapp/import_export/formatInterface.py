from wyjatki import CheckError

class FormatInterface(object):
    def __init__(self, namedtuple):
        self.FormatRecord = namedtuple

    def check(self, filename):
        raise CheckError("nienadpisana metoda check")

    def _check_handle(self, record):
        raise CheckError("nienadpisana metoda check_handle")

    def import_records_from_file_to_db(self):
        pass;

    def _gen_record_from_file(self, filename):
        pass

    def export_records_from_db_to_file(self, filename, lista_master_id):
        pass

    def _gen_record_from_db(self, lista_master_id):
        pass