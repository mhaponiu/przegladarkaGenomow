from zpr.database.v4_refresh import parser
from zpr.database.v4.singleton import singleton

class GffData():
    def __call__(self):
        # singleton w polaczeniu z wywolaniem po definicji klasy
        return self

    def __init__(self):
        print('wczytywanie gff...')
        generator = parser.Gff_annotation().generator()
        self.record_list = list(generator)  # gff records from file
        ''' GffRecord, ['ctg_id','type', 'start', 'end', 'info'] '''
        print('...koniec wczytywania gff')

    def __len__(self):
        return len(self.records)

    @property
    def records(self):
        return self.record_list

    @property
    @singleton
    def contigs_id_list(self):
        s = set()
        for r in self.records:
            s.add(r.ctg_id)
        return sorted(list(s))

    def contigs_amount(self):
        return len(self.contigs_id_list)

    @property
    @singleton
    def types(self):
        s = set()
        for r in self.records:
            s.add(r.type)
        return list(s)


GffData = GffData()