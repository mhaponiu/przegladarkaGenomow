from contigs import ContigsCompleteData

class GenomeGeneratorContig():
    ''' generuje pliki z genomem dla poszczegolnych chromosomow
    na podstawie contigow'''

    def __init__(self):
        data_tree = ContigsCompleteData()
        self.ctg_order_in_chr = data_tree.sorter.ctg_order_in_chr()
        self.dict_ctg_fasta = data_tree.dict_ctg_fasta()
        self.chr_ctg_dict = data_tree.sorter.chr_ctg_dict()
        self.chr_sumCtgLen = data_tree.chr_sumCtgLen()

    def generate_files(self):
        for chr in self.ctg_order_in_chr:
            genome = self._generate_genome(chr)
            self._generate_file(chr, genome)

    def gaps(self, chr):
        '''
        Suma sekwencji contigow z pliku fasta: 342288160
        Suma sekwencji contigow z pliku exel: 196309823
        zakladam ze suma contigow z pliku exel z wszystkich chromosomow wraz z gapami
        ma dac lacznie sume contigow z pliku fasta, czyli maksymalny znany nam genom.
        na kazdy chromosom rozdzielam tyle samo gapow, i daje je po rowno miedzy ctgi
        '''
        all_gaps = 342288160 - 196309823
        gaps_per_chr = all_gaps / 7
        ctgs_in_chr = len(self.chr_ctg_dict[chr])
        gaps_every_ctg = gaps_per_chr / (ctgs_in_chr - 1)
        print "gap dla chr " + str(chr) + ": " + str(gaps_every_ctg)
        return gaps_every_ctg

    def _generate_file(self, chr_number, genome):
        with open("genomes/chromosome_"+str(chr_number), 'wt') as f:
            f.write(genome)

    def _generate_genome(self, chr_number):
        genome = []
        ctgs = self.ctg_order_in_chr[chr_number]
        for ctg in ctgs:
            ctg_id_str = self.convert_int_to_ctg_id(ctg)
            genome.append(self.dict_ctg_fasta[ctg_id_str])
        return (self.gaps(chr_number) * "N").join(genome)

    @staticmethod
    def convert_int_to_ctg_id(id):
        return "ctg"+str(id)


if __name__ == "__main__":
    print("start generating genomes")
    g = GenomeGeneratorContig()
    g.generate_files()
    print("end generating genomes")