from organizm import Organizm
from chromosom import Chromosom
from scaffold import ScaffoldImpExp
from markerImpExp import MarkerImpExp
from meaningImpExp import MeaningImpExp
from zprapp.models import Chromosome, Marker

class Export(object):
    def __init__(self):
        self.org = Organizm()
        self.chr = Chromosom()
        self.scaff = ScaffoldImpExp()
        self.marker = MarkerImpExp()
        self.meaning = MeaningImpExp()

    def _prepare_lists_id(self, lista_id_org=None):
        # zwraca lista_id_chrms, lista_id_meaning
        if lista_id_org is not None:
            lista_id_chrms = []
            chrms = Chromosome.objects.filter(organism_id__in = lista_id_org)
            for c in chrms:
                lista_id_chrms.append(c.id)

            # zbieram wszystkie id meaning jakie maja chromosomy
            lista_id_meaning = set()
            mrkrs = Marker.objects.filter(chromosome_id__in = lista_id_chrms)
            for m in mrkrs:
                lista_id_meaning.add(m.meaning_id)
            lista_id_meaning = list(lista_id_meaning)


        else:
            return None, None

        return lista_id_chrms, lista_id_meaning

    def export(self, lista_id = None):
        self.org.export_records_from_db_to_file("exported_data/org.gff", lista_id)
        self.chr.export_records_from_db_to_file("exported_data/chr.gff", lista_id)

        lista_id_chrms, lista_id_meanings = self._prepare_lists_id(lista_id)

        self.scaff.export_records_from_db_to_file("exported_data/scaff.gff", lista_id_chrms)
        self.marker.export_records_from_db_to_file("exported_data/marker.gff", lista_id_chrms)
        self.meaning.export_records_from_db_to_file("exported_data/mean.gff", lista_id_meanings)



if __name__ == "__main__":
    exp = Export()
    # exp.export([54,55])
    exp.export([54])

    # chrms, mean = exp._prepare_lists_id([54])
    # print chrms
    # print  mean