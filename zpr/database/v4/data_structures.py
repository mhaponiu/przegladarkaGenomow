from zpr.database.v4 import parser

''' 
tutaj powinny byc jedyne klasy ktore korzystaja z parserow do danych - raz tylko powinnismy je z pliku pobrac
przygotowuja rozne slowniki z roznych perspektyw
'''
from functools import wraps

def singleton(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        func_name = func.__name__
        _func_name = '_' + func_name
        if getattr(self, _func_name, None):
            return getattr(self, _func_name)
        else:
            setattr(self, _func_name, func(*args, **kwargs))
            return getattr(self, _func_name)
    return wrapper


class FastaData():
    def __init__(self):
        generator = parser.Fasta_454().generator()
        self.record_list = list(generator) #fasta records from file
        ''' FastaRecord, ["id_from_file", "id", "sequence"] '''

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
        return sum([len(seq) for seq in self.records])


class GffData():

    def __init__(self):
        generator = parser.Gff_annotation_abinitio_ill1().generator()
        self.record_list = list(generator)  # gff records from file
        ''' GffRecord, ['ctg_id','type', 'start', 'end', 'info'] '''

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

    def types_amount(self):
        # todo
        pass



class CombinationData():
    ''' wspolne contigi miedzy fasta i gff to wszystkie te co w gffach sa '''
    def __init__(self):
        self.fasta_data = FastaData()
        self.gff_data = GffData()


    def joint_ctg_id_list(self):
        ''' tyle co gffow zgodnie z przewidywaniami'''
        return sorted(list(set(self.gff_data.contigs_id_list).intersection(self.fasta_data.contigs_id_list)))

    def joint_ctgs_amount(self):
        ''' tyle co gffow zgodnie z przewidywaniami'''
        return len(self.joint_ctg_id_list())

    def dict_fasta_filtered_by_gff_contigs(self):
        ''' slownik jak w fasta_data.dict ale tylko dla tych co w gffach sa'''
        fasta_dict = self.fasta_data.dict
        gff_contigs_ids = self.gff_data.contigs_id_list
        d = { key:value for (key, value) in fasta_dict.items() if key in gff_contigs_ids}
        return d



    def sum_sequences(self):
        ''' joint sequences gff and fasta'''
        di = { key:value for (key, value) in self.fasta_data.dict.items() if key in self.gff_data.contigs_id_list()}
