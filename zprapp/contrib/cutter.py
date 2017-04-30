from django.db.models.expressions import F

class Cutter():
    def __init__(self, ordered_annotation_list, start=None, end=None):
        self.ordered_annotation_list = ordered_annotation_list
        self.start = start
        self.end = end

    def sequence(self):
        ret = ""
        for a in self.ordered_annotation_list:
            ret += a.sequence
        return ret

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


    # def ajaxSeqSection(request):
    #     id_chr = request.GET['id_chr']
    #     widok_od = int(request.GET['widok_od'])
    #     widok_do = int(request.GET['widok_do'])
    #     chr = Chromosome.objects.get(id=id_chr)
    #     chr_len = chr.length
    #     selected_scflds = chr.scaffold_set.annotate(end=F('start') + F('length')) \
    #         .filter(start__lt=widok_do, end__gt=widok_od) \
    #         .order_by('order')
    #
    #     ret_string = bytearray('N' * (widok_do - widok_od))
    #     # print "empty_ret_string", ret_string
    #
    #     if selected_scflds.__len__() == 0:
    #         return ret_string.decode()
    #
    #     def zeroToNone(arg):
    #         if arg == 0:
    #             return None
    #         else:
    #             return int(arg)
    #
    #     def noneToZero(arg):
    #         if arg == None:
    #             return 0
    #         else:
    #             return int(arg)
    #
    #     for sc in selected_scflds:
    #         string_od = None
    #         string_do = None
    #         if widok_od > sc.start:
    #             seq_od = int(widok_od - sc.start)
    #             string_od = None
    #         elif widok_od <= sc.start:
    #             seq_od = None
    #             string_od = zeroToNone(int(abs(sc.start - widok_od)))
    #         if widok_do < sc.end:
    #             seq_do = int(widok_do - sc.start)
    #             string_do = None
    #         elif widok_do >= sc.end:
    #             seq_do = None
    #             # string_do zdefiniowany pozniej -> musze znac dlugosc_write_seq
    #
    #         write_seq = sc.sequence_set.first().sequence[seq_od:seq_do]
    #
    #         if widok_do >= sc.end:
    #             string_do = noneToZero(string_od) + write_seq.__len__()
    #
    #         ret_string[string_od:string_do] = str(write_seq)
    #         # print "seq_od", seq_od
    #         # print "seq_do", seq_do
    #         # print "write_seq", write_seq
    #         # print "write_seq_len", write_seq.__len__()
    #         # print "string_od ",string_od
    #         # print "string_do ",string_do
    #         # print "ret_string", ret_string
    #     return ret_string.decode()