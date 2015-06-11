from organizm import Organizm
from chromosom import Chromosom
from scaffold import ImpExpScaffold
from zprapp.models import Chromosome

class Export(object):
    def __init__(self):
        self.org = Organizm()
        self.chr = Chromosom()
        self.scaff = ImpExpScaffold()

    def export(self, lista_id = None):
        self.org.export_records_from_db_to_file("exported_data/org.gff", lista_id)
        self.chr.export_records_from_db_to_file("exported_data/chr.gff", lista_id)
        if(lista_id == None): lista_id_chrms = None
        else:
            lista_id_chrms = []
            chrms = Chromosome.objects.filter(organism_id__in = lista_id)
            for c in chrms:
                lista_id_chrms.append(c.id)
            print lista_id_chrms
        self.scaff.export_records_from_db_to_file("exported_data/scaff.gff", lista_id_chrms)

if __name__ == "__main__":
    exp = Export()
    exp.export([54])
