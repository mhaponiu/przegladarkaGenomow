from fastaData import FastaData
from gffData import GffData
from zpr.database.v4.singleton import singleton

class CombinationData():
    ''' wspolne contigi miedzy fasta i gff to wszystkie te co w gffach sa '''

    def __call__(self):
        # singleton w polaczeniu z wywolaniem po definicji klasy
        return self

    def __init__(self):
        self.fasta_data = FastaData()
        self.gff_data = GffData()

    @property
    @singleton
    def joint_ctg_id_list(self):
        ''' tyle co gffow zgodnie z przewidywaniami'''
        return sorted(list(set(self.gff_data.contigs_id_list).intersection(self.fasta_data.contigs_id_list)))

    def joint_ctgs_amount(self):
        ''' tyle co gffow zgodnie z przewidywaniami'''
        return len(self.joint_ctg_id_list)

    @property
    @singleton
    def dict_fasta_filtered_by_gff_contigs(self):
        ''' slownik jak w fasta_data.dict ale tylko dla tych co w gffach sa'''
        fasta_dict = self.fasta_data.dict
        gff_contigs_ids = self.gff_data.contigs_id_list
        return { key:value for (key, value) in fasta_dict.items() if key in gff_contigs_ids}

    @singleton
    def sum_sequences(self):
        ''' joint sequences gff and fasta'''
        return sum([len(seq) for seq in self.dict_fasta_filtered_by_gff_contigs.values()])

CombinationData = CombinationData()