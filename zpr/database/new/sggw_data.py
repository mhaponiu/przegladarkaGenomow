# coding=latin-1

from zpr.database.new.parser import ParserLinks3
import pickle
import cPickle


class Links3(object):
    '''super_id to id scaffolda'''

    def __init__(self):
        self.lista_links3 = list(ParserLinks3().gen_record_oryginalny())
        '''XLSX(ncbi_ctg_id=1.0, lp_oryg=1.0, super_id=0.0, num_bases_in_super=2496462.0, num_contigs_in_super=46.0,
        ordinal_num_of_contig_in_super=1.0, contig_id=0.0,length_of_contig=23626.0, estimated_gap_before_contig=0.0,
        estimated_gap_after_contig=-299.0, i_f='', start=0.0, stop=23626.0, j=2496462.0)'''

    def print_all_stats(self):
        liczba_contigow = self.max_ncbi_ctg_id() - self.min_ncbi_ctg_id() + 1
        print 'liczba contigow: ', liczba_contigow
        print 'min_ncbi_ctg_id: ', self.min_ncbi_ctg_id()
        print 'max_ncbi_ctg_id: ', self.max_ncbi_ctg_id()
        liczba_scaffoldow = self.max_scaffold_id() - self.min_scaffold_id() + 1
        print 'liczba scaffoldow: ', liczba_scaffoldow
        print 'min_scaffold_id: ', self.min_scaffold_id()
        print 'max_scaffold_id: ', self.max_scaffold_id()
        print 'amount_of_contigs_in_scaffold (dict[scaffold_id]=amount_ctgs): ', \
            self.amount_of_contigs_in_scaffold()
        print 'scflds_with_only_one_ctg: ', self._scflds_with_only_one_ctg()
        amount_scfldy_one_ctg = self.amount_of_scfld_with_only_one_ctg()
        print 'amount_of_scfld_with_only_one_ctg: ', \
            amount_scfldy_one_ctg
        num_contigs_in_super_true = self.check_amount_of_contigs_in_scaffold_with_col_num_contigs_in_super()
        print 'kolumna num_contigs_in_super jest prawidlowa: ', \
            num_contigs_in_super_true
        print 'sum_len_of_contigs_without_gaps_between (dict[scfld]=sum_ctgs_len): ', \
            self.sum_len_of_contigs_without_gaps_between()
        incorrect_num_bases_in_super = self.check_col_num_bases_in_super_with_sum_length_of_contig()
        print 'kolumna num_bases_in_super jest nieprawidlowa w tylu scaffoldach: ', \
            incorrect_num_bases_in_super
        print 'liczba scfldow - liczba scfldow z 1 contigiem == liczba nieprawidlowych num_bases_in_super: ', \
            liczba_scaffoldow - amount_scfldy_one_ctg == incorrect_num_bases_in_super, \
            "=> wniosek: wszystkie scaffoldy co maja >1 ctg maja nieprawidlowa 'kolumne num_bases_in_super'"
        # TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print 'hipoteza: num_bases_in_super zawierają GAPY => sprawdzic dla bezwzglednych wartosci GAPow'

    def max_ncbi_ctg_id(self):
        return int(max(self.lista_links3, key=lambda a: a.ncbi_ctg_id).ncbi_ctg_id)

    def min_ncbi_ctg_id(self):
        return int(min(self.lista_links3, key=lambda a: a.ncbi_ctg_id).ncbi_ctg_id)

    def min_scaffold_id(self):
        '''#super_id to scaffold'''
        return int(min(self.lista_links3, key=lambda a: a.super_id).super_id)

    def max_scaffold_id(self):
        '''#super_id to scaffold'''
        return int(max(self.lista_links3, key=lambda a: a.super_id).super_id)

    def _dict_scafld_ctgs(self):
        '''return dict[scaffold_id]=rows'''
        d = {}
        for scf in range(int(self.min_scaffold_id()), int(self.max_scaffold_id()) + 1):
            d[scf] = []
        for row in self.lista_links3:
            d[int(row.super_id)].append(row)
        return d

    def amount_of_contigs_in_scaffold(self):
        '''return dict[scaffold_id]=amount_ctgs'''
        d = {}
        for scf in range(int(self.min_scaffold_id()), int(self.max_scaffold_id()) + 1):
            d[scf] = 0
        for row in self.lista_links3:
            d[int(row.super_id)] = d[int(row.super_id)] + 1
        return d

    def check_amount_of_contigs_in_scaffold_with_col_num_contigs_in_super(self):
        amount = self.amount_of_contigs_in_scaffold()
        for scf_id, rows in self._dict_scafld_ctgs().items():
            for row in rows:
                if int(row.num_contigs_in_super) != amount[scf_id]:
                    return False
        return True

    def _scflds_with_only_one_ctg(self):
        d = self.amount_of_contigs_in_scaffold()
        return [a[0] for a in d.items() if a[1] == 1]

    def amount_of_scfld_with_only_one_ctg(self):
        return len(self._scflds_with_only_one_ctg())

    def sum_len_of_contigs_without_gaps_between(self):
        '''return dict[scfld] = sum_ctgs_len
        suma jest obliczona przeze mnie'''
        d = {}
        for scf in range(int(self.min_scaffold_id()), int(self.max_scaffold_id()) + 1):
            d[scf] = 0
        for row in self.lista_links3:
            d[int(row.super_id)] = d[int(row.super_id)] + int(row.length_of_contig)
        return d

    def check_col_num_bases_in_super_with_sum_length_of_contig(self):
        '''zwraca liczbe scaffoldow gdzie nie zgadza sie ta kolumna z obliczona wartoscia'''
        zle = 0
        obliczony_dict = self.sum_len_of_contigs_without_gaps_between()  # dict[scfld] = sum_ctgs_len
        for scf_id, rows in self._dict_scafld_ctgs().items():
            if obliczony_dict[scf_id] != rows[0].num_bases_in_super:
                zle = zle + 1
        return zle


if __name__ == "__main__":
    links3 = Links3()
    links3.print_all_stats()
