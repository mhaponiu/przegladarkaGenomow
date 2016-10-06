class CheckError(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.n_record = None;
    def __str__(self):
        return repr(self.msg)

class ImportFileError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)