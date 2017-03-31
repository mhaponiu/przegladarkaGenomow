from collections import defaultdict, OrderedDict

from data_extractor import DataExtractor
'''
    DataExtractor dostarcza do Sortera:
    { scaffold_no: (scaffold_length, chromosome) }
    { contig_no: (contig_length, ctg_pos_on_scf, chromosome, scaffold) }
    { marker_name: (marker_in_chr, chromosome, ctg_no, pos_1_on_ctg, pos_2_on_ctg) }
'''

'''
Sorter tworzy odpowiednie pomocnicze struktury danych ustawiajace w kolejnosci contigi, scaffoldy
'''
class Sorter():
    def __init__(self, contigs, markers):
        # parametry z wyjscia DataExtractora
        self.contigs = contigs # { contig_no: (contig_length, ctg_pos_on_scf, chromosome, scaffold) }
        self.markers = markers # { marker_name: (marker_in_chr, chromosome, ctg_no, pos_1_on_ctg, pos_2_on_ctg) }

    def chr_ctg_dict(self):
        # e.g.('1780', Contig(contig_length=1086173, ctg_pos_on_scf=1, chromosome=1, scaffold=5219)
        contig_list = list(self.contigs.items())
        chr_ctg_dict = defaultdict(list)
        for id, ctg in contig_list:
            chr_ctg_dict[ctg.chromosome].append({
                "ctg_no": id,
                'contig_length': ctg.contig_length,
                'ctg_pos_on_scf': ctg.ctg_pos_on_scf,
                'chromosome': ctg.chromosome,
                'scaffold': ctg.scaffold
            })

        ''' e.g. chr_ctg_dict[2] == [{
        'ctg_no': '2699',
        'ctg_pos_on_scf': 1,
        'chromosome': 2,
        'contig_length': 442389,
        'scaffold': 5466
        }, ... ] '''
        return chr_ctg_dict

    def chr_mrkr_dict(self):
        # e.g. (u'SSR07269', Marker(marker_in_chr=136, chromosome=4, ctg_no=1556,
        #       pos_1_on_ctg=1120252, pos_2_on_ctg=1120056))
        mrkrs_list = list(self.markers.items())
        chr_mrkr_dict = defaultdict(list)
        for id, mrkr in mrkrs_list:
            chr_mrkr_dict[mrkr.chromosome].append({
                'marker_name': id,
                'marker_in_chr': mrkr.marker_in_chr,
                'chromosome': mrkr.chromosome,
                'ctg_no': mrkr.ctg_no,
                'pos_1_on_ctg': mrkr.pos_1_on_ctg,
                'pos_2_on_ctg': mrkr.pos_2_on_ctg
            })
        return chr_mrkr_dict

    def chr_mrkr_dict_sorted_via_marker_in_chr(self):
        # sort marker -> chromosome: markers -> markers_in_chr -> ctg_no
        chr_mrkr_dict = self.chr_mrkr_dict()
        sorted_chr_mrkr_dict = {}
        for chr in chr_mrkr_dict.keys():
            sorted_chr_mrkr_dict[chr] = sorted(chr_mrkr_dict[chr], key=lambda m: m['marker_in_chr'])
        return sorted_chr_mrkr_dict

    def ctg_order_in_chr(self):
        sorted_mrkrs = self.chr_mrkr_dict_sorted_via_marker_in_chr()
        chr_ctg_order = {}
        for chr in sorted_mrkrs.keys():
            chr_ctg_order[chr] = [ m['ctg_no'] for m in sorted_mrkrs[chr] ]

        ''' { chr: [ctg_no, ...] }'''
        return chr_ctg_order

    def _scf_order_in_chr(self):
        ctg_order_in_chr = self.ctg_order_in_chr()
        chr_scf_order = defaultdict(list)
        for chr in ctg_order_in_chr:
            for ctg_no in ctg_order_in_chr[chr]:
                chr_scf_order[chr].append(self.contigs[str(ctg_no)].scaffold)

        ''' { chr: [scaffold, ...] } - lista scaffoldow w odpowiedniej kolejnosci ale
         zawiera powtorzenia; zeby je usunac -> list(OrderedDict.fromkeys(lista_powtorzen))
        '''
        return chr_scf_order

    def scf_order_in_chr(self):
        powtorzenia = self._scf_order_in_chr()
        ret = {}
        for chr in powtorzenia.keys():
            ret[chr] = list(OrderedDict.fromkeys(powtorzenia[chr]))
        return ret





