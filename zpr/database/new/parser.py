from collections import namedtuple
from itertools import starmap

import os
import re
import xlrd

from zpr.settings import BASE_DIR


class ParserXLSX(object):
    def __init__(self, xslx_location):
        self.xslx_location = xslx_location

    def _convert_string_to_correct_namedtuple(self, text, col):
        'nazwy niektorych kolumn sa puste -> zmieniam je na unknown[nr w exelu]'
        if text == '':
            return 'unknown'+str(col)
        text = text.replace("1st", "First")
        text = text.replace(" ", "_")
        if text.startswith("if"):
            text = text.replace('if', "i_f")
        text = re.sub(r"!|@|#|$|%|^|&|\*|\(|\)|=|\+", "", text)
        return text

    def _gen_row_from_sheet_nr(self, nr):
        workbook = xlrd.open_workbook(self.xslx_location)
        sheet = workbook.sheet_by_index(nr)
        data = ([sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(1, sheet.nrows))
        return data

    def _gen_row_from_sheet_name(self, name):
        workbook = xlrd.open_workbook(self.xslx_location)
        sheet = workbook.sheet_by_name(name)
        data = ([sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(1, sheet.nrows))
        return data

    def _namedtuple_from_sheet_by_nr(self, nr, tuple_name):
        workbook = xlrd.open_workbook(self.xslx_location)
        sheet = workbook.sheet_by_index(nr)
        col_names = [self._convert_string_to_correct_namedtuple(
                    sheet.cell_value(0, col), col)
                    for col in range(sheet.ncols)]
        return namedtuple(tuple_name, col_names)

    def _namedtuple_from_sheet_by_name(self, sheet_name, tuple_name):
        workbook = xlrd.open_workbook(self.xslx_location)
        sheet = workbook.sheet_by_name(sheet_name)
        col_names = [self._convert_string_to_correct_namedtuple(
            sheet.cell_value(0, col), col)
                     for col in range(sheet.ncols)]
        return namedtuple(tuple_name, col_names)

    def _gen_record_from_sheet_by_name(self, name):
        XLSX = self._namedtuple_from_sheet_by_name(name, 'XLSX')
        row_gen = self._gen_row_from_sheet_name(name)
        for row in row_gen:
            yield XLSX(*row)

    def _gen_record_from_sheet_by_nr(self, nr):
        XLSX = self._namedtuple_from_sheet_by_nr(nr, 'XLSX')
        row_gen = self._gen_row_from_sheet_nr(nr)
        for row in row_gen:
            yield XLSX(*row)

    # def gen_record_arkusz1(self):
    #     return self._gen_record_from_sheet_by_name("Arkusz1")
    #
    # def gen_record_arkusz2(self):
    #     return self._gen_record_from_sheet_by_name("Arkusz2")
    #
    # def gen_record_arkusz3(self):
    #     return self._gen_record_from_sheet_by_name("Arkusz3")

class ParserSTC_vs_contigs1(ParserXLSX):
    def __init__(self, xslx_location=os.path.abspath(os.path.join(BASE_DIR, '../database/new/STC_vs_contigs1.xlsx'))):
        ParserXLSX.__init__(self, xslx_location)

    def gen_record_arkusz1(self):
        return self._gen_record_from_sheet_by_name("Arkusz1")

    def gen_record_arkusz2(self):
        return self._gen_record_from_sheet_by_name("Arkusz2")

    def gen_record_arkusz3(self):
        return self._gen_record_from_sheet_by_name("Arkusz3")



class ParserLinks3(ParserXLSX):
    def __init__(self, xslx_location=os.path.abspath(os.path.join(BASE_DIR, '../database/new/links3.xlsx'))):
        ParserXLSX.__init__(self, xslx_location)

    def gen_record_oryginalny(self):
        return self._gen_record_from_sheet_by_name("ORYGINALNY")



class ParserGffTxt(object):
    def __init__(self, gff_file=os.path.abspath(os.path.join(BASE_DIR, '../database/new/GFF_to_Predictions_ID.txt'))):
        self.gff_file = gff_file

    def _namedtuple(self):
        with open(self.gff_file, 'rt') as f:
            first_line = f.readline()
            lista = self._line_to_list(first_line)
            lista = [(l,) for l in lista] #konwersja do listy krotek jednoelementowych
            lista = starmap(self._convert_string_to_correct_namedtuple, lista)
            return namedtuple('GFF', lista)

    def _line_to_list(self, line):
        return filter(lambda a: a!='', re.split(r'[\t\n\r]', line))

    def _convert_string_to_correct_namedtuple(self, text):
        'nazwy niektorych kolumn sa "-" -> zmieniam je na unknown bo pole w klasie nie moze zaczynac sie od -'
        text = text.replace("-", "unknown")
        return text

    def gen_record(self):
        GFF = self._namedtuple()
        with open(self.gff_file, "rt") as f:
            f.readline() # pomijam pierwsza linijke bo nazwy pol
            for line in f:
                yield GFF(*self._line_to_list(line))


if __name__ == '__main__':
    p = ParserSTC_vs_contigs1()
    g1 = p.gen_record_arkusz1()
    print g1.next()
    print list(p.gen_record_arkusz1()).__len__() # 52524

    g2 = p.gen_record_arkusz2()
    print g2.next()
    print list(p.gen_record_arkusz2()).__len__() # 52524

    g3 = p.gen_record_arkusz3()
    print g3.next()
    print list(p.gen_record_arkusz3()).__len__() # 12087

    p2 = ParserGffTxt()
    print p2.gen_record().next()
    print list(p2.gen_record()).__len__() # 210143

    # XLSX(lp=7535.0, Read_name=u'STC1_Bam_071_J24_M13.f', Polskie_chromosomy=1.0, Chinese_chromosome=4.0,
    #       Read_Length=780.0, Ctg_ID_NCBI=138.0, Ctg_Length=30580.0, First_base_ctg=2252.0, Last_base_ctg=3031.0,
    #       strand=u'-', Read_partner_name=u'STC1_Bam_071_J24_M13.r', Partner_contig=135.0, Real_insert_length=121308.0,
    #       cM='', unknown14='', unknown15='')
    # XLSX(lp=7.0, Read_name=u'STC1_Bam_023_I14_M13.f', Chinese_chromosome=7.0, Read_Length=528.0, Ctg_ID_NCBI=1.0,
    #       Ctg_Length=23626.0, First_base_ctg=4173.0, Last_base_ctg=4700.0, strand=u'+',
    #       Read_partner_name=u'STC1_Bam_023_I14_M13.r', Partner_contig=5.0, Real_insert_length=134087.0)
    # XLSX(lp=11731.0, Ctg_ID_NCBI=1.0, chr_cel1=u'chr7', liczba_wg_china=7.0, cM_wg_cel=u'', chr_wg_ara='',
    #       cM_wg_r='', v=u'ok.')
    # GFF(ContigID='CSB10A_v1_contig_1', Model='GeneMark.hmm', Feature='stop_codon', Start='11744', Stop='11746',
    #       Strand='-', unknown='0', GFF_GeneID=' 1_g', Predictions_GeneID='gene_1#CSB10A_v1_contig_1')

    p2 = ParserLinks3()
    g4 = p2.gen_record_oryginalny()
    print g4.next()
    print list(g4.next()).__len__()