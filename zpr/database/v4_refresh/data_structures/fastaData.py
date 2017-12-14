from zpr.database.v4_refresh import parser
from zpr.database.v4.singleton import singleton


class FastaData():
    def __call__(self):
        # singleton w polaczeniu z wywolaniem po definicji klasy
        return self

    def __init__(self):
        print('wczytywanie fasta...')
        generator =  parser.Fasta_B10v2_c_corr().generator()
        self.record_list = list(generator) #fasta records from file
        ''' FastaRecord, ["id_from_file", "id", "sequence"] '''
        print('...koniec wczytywania fasta')

    def __len__(self):
        return len(self.records)

    @property
    @singleton
    def dict(self):
        return {record.id: record.sequence for record in self.records}

    @property
    @singleton
    def contigs_id_list(self):
        return [record.id for record in self.records]

    @property
    def records(self):
        return self.record_list

    @singleton
    def sum_all_sequences(self):
        return sum([len(r.sequence) for r in self.records])

FastaData = FastaData()