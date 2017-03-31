from collections import namedtuple

from data_extractor import DataExtractor
from sorter import Sorter
from parser import Fasta_B10v2_c_corr

'''DataTreeContig produkuje contigi przygotowane do zapisu
do bazy dla poszczegolnych chromosomow. Bez informacji o innych strukturach takich jak scaffold itd.'''
class DataTreeContig():
    def __init__(self):
        data_extractor = DataExtractor()
        self.sorter = Sorter(contigs= data_extractor.ctgs,
                             markers= data_extractor.mrkrs)
        self.chr_ctg = self.sorter.chr_ctg_dict()
        self.ctg_fasta = list(Fasta_B10v2_c_corr().generator())# namedtuple('FastaRecord', ['id', 'sequence'])
        self.ctg_fasta_dict = self.dict_ctg_fasta()
        self.chr_ctg_order = self.sorter.ctg_order_in_chr()
        self.Contig = namedtuple("Contig", ['id', 'start', 'length', 'seq'])

    def produce_full_dict(self):
        # {'length': int, 'contigs': [namedtuple("Contig", ['id', 'start', 'length', 'seq'])]}
        ret = {}
        for chr in range(1,8):
            contig_list = self._produce_chromosome(chr)
            chr_len = contig_list[-1].start + contig_list[-1].length
            ret[chr] = {'length': chr_len, 'contigs': contig_list}
        return ret


    def _produce_chromosome(self, chr):
        gap = self._gaps(chr)
        ctg_order = self.chr_ctg_order[chr]
        ret_list = []
        start = 0
        for ctg_id in ctg_order:
            seq = self.ctg_fasta_dict[self.convert_int_to_ctg_id(ctg_id)]
            seq_len = len(seq)
            ret_list.append(self.Contig(id=ctg_id, start=start, length=seq_len, seq=seq))
            start = start + seq_len + gap
        return ret_list

    def _gaps(self, chr):
        '''
                Suma sekwencji contigow z pliku fasta: 342288160
                Suma sekwencji contigow z pliku exel: 196309823
                zakladam ze suma contigow z pliku exel z wszystkich chromosomow wraz z gapami
                ma dac lacznie sume contigow z pliku fasta, czyli maksymalny znany nam genom.
                na kazdy chromosom rozdzielam tyle samo gapow, i daje je po rowno miedzy ctgi
                '''
        all_gaps = self.sum_ctg_fasta() - self.sum_ctg_exel() # 342288160 - 196309823
        gaps_per_chr = all_gaps / 7
        ctgs_in_chr = len(self.chr_ctg[chr])
        gaps_every_ctg = gaps_per_chr / (ctgs_in_chr - 1)
        print "gap dla chr " + str(chr) + ": " + str(gaps_every_ctg)
        return gaps_every_ctg

    def dict_ctg_fasta(self):
        return {ctg.id: ctg.sequence for ctg in self.ctg_fasta}

    def chr_sumCtgLen(self):
        ''' dict {chr: sum(ctg_len}'''
        ret = {}
        for chr in self.chr_ctg:
            ret[chr] = sum([ctg['contig_length'] for ctg in self.chr_ctg[chr]])
        return ret

    def sum_ctg_exel(self):
        chr_sumCtg = self.chr_sumCtgLen()
        return sum([chr_sumCtg[chr]for chr in chr_sumCtg.keys()])

    def sum_ctg_fasta(self):
        ''' :return sum contigs from gff file'''
        return sum([len(fasta.sequence) for fasta in self.ctg_fasta])

    def percent_known_genome(self):
        return self.sum_ctg_exel()/float(self.sum_ctg_fasta())

    @staticmethod
    def convert_int_to_ctg_id(id):
        return "ctg" + str(id)



if __name__ == "__main__":
    '''
    tree = DataTree()

    tree.sorter.ctg_order_in_chr()
    {1: [1740, 1869, 36, 1451, 1450, 1453, 1780, 1714, 29, 1057, 2390, 1808, 47, 999, 3347, 3379, 1557, 1528, 1523, 949,
         944, 211],
     2: [4, 1558, 31, 2417, 2178, 105, 440, 2699, 1055, 1522, 191, 1227, 35],
     3: [1, 2009, 2607, 1575, 2174, 1216, 1918, 304, 384, 3412, 3419, 1837, 1838, 1251],
     4: [24, 1821, 1820, 1267, 1252, 2324, 2194, 2465, 2279, 184, 1556, 1502, 1635, 907, 1798],
     5: [910, 3473, 278, 197, 205, 2923, 3408, 2231, 2864, 2100, 1190, 1173, 2572, 2246, 3475, 1445, 1675, 1228, 1546,
         1674, 1673, 1678],
     6: [1402, 1425, 1429, 10, 3345, 1299, 1592, 1544, 1456, 1778, 1269, 1449, 2203, 1170, 1672, 27, 1000, 1268, 1002],
     7: [1681, 1679, 1658, 2387, 3517, 2185, 62, 2034, 1006, 1041, 1047]}

    tree.sorter._scf_order_in_chr() # z powtorzeniami
    {1: [4713, 4713, 830, 1729, 1729, 4713, 5219, 2452, 983, 983, 830, 830, 830, 830, 830, 830, 238, 4416, 1243,
         1243, 1243, 1243],
     2: [2955, 2955, 2955, 2083, 2221, 6354, 2221, 5466, 985, 598, 3321, 598, 598],
     3: [1725, 1725, 5900, 674, 356, 4636, 3072, 1725, 968, 6731, 968, 501, 501, 501],
     4: [2972, 4555, 4555, 1186, 5252, 3165, 1735, 1186, 5489, 4285, 4285, 644, 644, 644, 644],
     5: [4442, 13, 1556, 1556, 1556, 3952, 6047, 6047, 13, 4676, 13, 13, 1084, 1084, 1084, 953, 238, 238, 238, 238,
         238, 238],
     6: [356, 356, 356, 356, 356, 3267, 4855, 7049, 474, 474, 1172, 474, 1635, 474, 474, 474, 474, 1172, 474],
     7: [3201, 3201, 880, 880, 868, 3556, 3556, 880, 3556, 5062, 5068]})

    tree.sorter.scf_order_in_chr() # bez powtorzen
    {1: [4713, 830, 1729, 5219, 2452, 983, 238, 4416, 1243],
     2: [2955, 2083, 2221, 6354, 5466, 985, 598, 3321],
     3: [1725, 5900, 674, 356, 4636, 3072, 968, 6731, 501],
     4: [2972, 4555, 1186, 5252, 3165, 1735, 5489, 4285, 644],
     5: [4442, 13, 1556, 3952, 6047, 4676, 1084, 953, 238],
     6: [356, 3267, 4855, 7049, 474, 1172, 1635],
     7: [3201, 880, 868, 3556, 5062, 5068]}
     '''

