from contigs import ChromosomesContigFactory
import sys, os
# from Sconstruct import VIRTUALENV_ROOT
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
# sys.path.extend([os.path.join(VIRTUALENV_ROOT,'lib', 'python2.7', 'site-packages')])
import django
django.setup() #bez tego AppRegistryNotReady: Models aren't loaded yet.

from zprapp.models import *

class Inserter():
    def __init__(self):
        contigs_factory = ChromosomesContigFactory()
        self.chr_contig = contigs_factory.produce_chromosomes()

    def insert(self):
        orgs = self._organisms()
        self._save_elements(orgs)
        chrs = self._chromosomes(orgs[0])
        self._save_elements(chrs)
        types = self._annotation_types()
        self._save_elements(types)
        for chr in range(0,8):
            ctgs = self._contigs(chrs[chr], types[0])
            self._save_elements(ctgs)

    def _save_elements(self, elements):
        ''':param elements -- list'''
        for e in elements:
            e.save()

    def _organisms(self):
        return [Organism(name="Cucumber_v3")]

    def _chromosomes(self, org):
        zero = Chromosome(number= 0, ordered= False, organism= org,
                          length= self.chr_contig[0]['length'])
        ret_chrs = [zero]
        for n in range(1,8):
            ret_chrs.append(Chromosome(number= n, ordered= True, organism= org,
                                       length= self.chr_contig[n]['length']))
        return ret_chrs

    def _annotation_types(self):
        return [AnnotationType(name="contig", short_name='ctg')]

    def _contigs(self, chr, type):
        if chr.number == 0:
            return [Annotation(length= ctg.length,
                              name= str(ctg.id),
                              sequence= ctg.seq,
                              type= type,
                              chromosome= chr) for ctg in self.chr_contig[0]['contigs']]
        else:
            return [Annotation(start_chr= ctg.start,
                        length= ctg.length,
                        name= str(ctg.id),
                        sequence= ctg.seq,
                        type=type,
                        chromosome= chr) for ctg in self.chr_contig[chr.number]['contigs']]

    def clear_db(self):
        pass



if __name__ == "__main__":
    inserter = Inserter()
    inserter.clear_db()
    inserter.insert()