import pickle

from parser import Parser_besSeq_besOldName_B10v2_yang13
from collections import namedtuple, OrderedDict

# import os, django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
# django.setup()
# from zprapp.models import Organism


''' DataExtractor parsuje plik besSeq_besOldName_B10v2_yang13.xslx
    i wyciaga z niego informacje o scaffoldach, contigach i markerach'''
class DataExtractor():
    '''
    { scaffold_no: (scaffold_length, chromosome) }
    { contig_no: (contig_length, ctg_pos_on_scf, chromosome, 'scaffold') }
    { marker_name: (marker_in_chr, chromosome, ctg_no, pos_1_on_ctg, pos_2_on_ctg) }
    '''
    def __init__(self):
        parser = Parser_besSeq_besOldName_B10v2_yang13()
        self.exel_rows = list(parser.gen_record_arkusz1())
        self.mrkrs = DataExtractor.markers(self.exel_rows)
        self.scflds = DataExtractor.scafolds(self.exel_rows)
        self.ctgs = DataExtractor.contigs(self.exel_rows)

    @staticmethod
    def get_chr(row):
        try:
            return row.marker_chr.split("CHR")[1]
        except IndexError:
            return None


    @staticmethod
    def markers(exel_rows):
        ''' raw markers from exel table without any processing
        :return OrderedDict -- { marker_name: (marker_in_chr, chromosome, ctg_no, pos_1_on_ctg, pos_2_on_ctg) }'''
        markers = OrderedDict()
        marker = namedtuple("Marker", ['marker_in_chr', 'chromosome', 'ctg_no', 'pos_1_on_ctg', 'pos_2_on_ctg'])
        for row in exel_rows:
            if row.marker_name == "":
                continue
            chr_num = DataExtractor.get_chr(row)
            markers[row.marker_name] = marker(marker_in_chr=int(row.marker_inChr), chromosome=int(chr_num), ctg_no=int(row.ctg_no),
                                              pos_1_on_ctg=int(row.marker_pos), pos_2_on_ctg=int(row.marker2_pos))
        return markers

    @staticmethod
    def scafolds(exel_rows):
        ''':return OrderedDict -- { scaffold_no: (scaffold_length, chromosome) }'''
        scafolds = OrderedDict()
        scafold = namedtuple('Scafold', ['scaffold_length', 'chromosome'])
        for row in exel_rows:
            if row.marker_name == "":
                continue
            chr_num = DataExtractor.get_chr(row)
            scafolds[str(int(row.scf_no))] = scafold(scaffold_length=int(row.scaf_length), chromosome=int(chr_num))
        return scafolds

    @staticmethod
    def contigs(exel_rows):
        ''':return OrderedDict -- { contig_no: (contig_length, ctg_pos_on_scf, chromosome, 'scaffold') }'''
        contigs = OrderedDict()
        contig = namedtuple('Contig', ['contig_length', 'ctg_pos_on_scf', 'chromosome', 'scaffold'])
        for row in exel_rows:
            if row.marker_name == "":
                continue
            chr_num = DataExtractor.get_chr(row)
            contigs[str(int(row.ctg_no))] = contig(contig_length=int(row.ctg_length), ctg_pos_on_scf=int(row.ctg_pos),
                                         chromosome=int(chr_num), scaffold=int(row.scf_no))
        return contigs

    @staticmethod
    def bacs(exel_rows):
        ''':return OrderedDict -- { bes_name: BAC) }'''
        # TODO
        return exel_rows

    # def dump_data(self):
    #     with open("dataExtractor.pickle", 'wb') as f:
    #         pickle.dump(self, f)
    #
    # @staticmethod
    # def load_data(file):
    #     with open("dataExtractor.pickle", 'rb') as f:
    #         dataExtractor = pickle.load(f)
    #     return dataExtractor


class Bac(object):
    def __init__(self, name, length_from_exel, contig, marker=None):
        self.bes = namedtuple('Bes', ['sequence', 'bes_1_pos', 'bes_2_pos'])
        self.name = name
        self.length_from_exel = length_from_exel
        self.contig = contig
        self.marker = marker
        self.__foreward = None
        self.__backward = None

    @property
    def foreward(self):
        return self.__foreward

    @foreward.setter
    def foreward(self, value):
        ''':arg value -- tuple (sequence, bes_1_pos, bes_2_pos)'''
        self.__foreward = self.bes(*value)

    @property
    def backward(self):
        return self.__backward

    @backward.setter
    def backward(self, value):
        ''':arg value -- tuple (sequence, bes_1_pos, bes_2_pos)'''
        self.__backward = self.bes(*value)



if __name__ == "__main__":
    print("<<< START >>>")
    # dataExtractor = DataExtractor()
    # markers = dataExtractor.unique_markers()

    # b = Bac("SSR", 324, 234)
    # print(b.foreward)
    # b.foreward = ("AAA", 32421, 234321)
    # b.backward = ("BBB", 32421, 234321)
    # print(b.backward)

    data_extractor = DataExtractor()

    print("<<< KONIEC >>>")