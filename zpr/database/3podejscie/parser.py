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

class Parser_besSeq_besOldName_B10v2_yang13(ParserXLSX):
    def __init__(self, xslx_location= os.path.join(BASE_DIR, '..', 'database', '3podejscie',
                                                   'besSeq_besOldName_B10v2_yang13.xlsx')):
        ParserXLSX.__init__(self, xslx_location)

    def gen_record_arkusz1(self):
        return self._gen_record_from_sheet_by_name("Arkusz1")





if __name__ == '__main__':
    p = Parser_besSeq_besOldName_B10v2_yang13()
    g1 = p.gen_record_arkusz1()
    print next(g1)
    # print len(list(p.gen_record_arkusz1()))# 52524
