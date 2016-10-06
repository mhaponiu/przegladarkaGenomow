from zpr.database.new.parser import ParserSTC_vs_contigs1, ParserLinks3
# from zprapp.models import Chromosome
class Importer(object):
    def __init__(self
                 # , chromosom_id
                 ):
        # TODO odkomentowac i dopisac do markery do konkretnego chromosomu
        # self.chromosom = Chromosome.objects.get(id=chromosom_id)
        self.parserSTC = ParserSTC_vs_contigs1()
        self.parserLinks3 = ParserLinks3()


    def contig_dict(self):
        contig_dict = {}
        for row in self.parserLinks3.gen_record_oryginalny():
            contig_dict[int(row.ncbi_ctg_id)] = {'length': int(row.length_of_contig)
                                                 , 'start': int(row.start)
                                                 , 'stop' : int(row.stop)}

        return contig_dict

if __name__ == "__main__":
    imp = Importer()
    print imp.contig_dict().__len__()