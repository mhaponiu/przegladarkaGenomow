from django.db.models.expressions import F

class Trimmer():
    '''
    zakladam ze wszystkie adnotacje leza na jednym chromosomie
    '''
    def __init__(self, ordered_annotation_list, start_chr=None, end_chr=None):
        self.ordered_annotation_list = ordered_annotation_list
        self.start = start_chr
        self.end = end_chr
        self.chromosome = ordered_annotation_list[0].chromosome # zakladam ze wszystkie adnotacje leza na jednym chromosomie

    def sequence(self):
        annotations = self.ordered_annotation_list.annotate(end=F('start_chr') + F('length'))

        filter_args = {}
        if self.start is not None:
            filter_args['end__gt'] = self.start
        if self.end is not None: filter_args['start_chr__lt'] = \
            self.end
        if self.start is not None or self.end is not None:
            annotations = annotations.filter(**filter_args)
        annotations = annotations.order_by('start_chr')

        if self.end is None or self.end > self.chromosome.length:
            self.end = self.chromosome.length
        if self.start is None or self.start < 0 or self.start > self.end:
            self.start = 0

        ret_string = bytearray('N' * (self.end - self.start))

        for a in annotations:
            string_od = None
            string_do = None
            if self.start > a.start_chr:
                seq_od = int(self.start - a.start_chr)
            elif self.start <= a.start_chr:
                seq_od = None
                string_od = self._zeroToNone(int(abs(a.start_chr - self.start)))
            if self.end < a.end:
                seq_do = int(self.end - a.start_chr)
                string_do = None
            elif self.end >= a.end:
                seq_do = None

            write_seq = a.sequence[seq_od:seq_do]

            if self.end >= a.end:
                string_do = self._noneToZero(string_od) + len(write_seq)

            ret_string[string_od:string_do] = str(write_seq)

        return ret_string.decode()


    def _zeroToNone(self, arg):
        if arg == 0:
            return None
        else:
            return int(arg)

    def _noneToZero(self, arg):
        if arg == None:
            return 0
        else:
            return int(arg)