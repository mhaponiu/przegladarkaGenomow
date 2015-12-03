from organizm import Organizm
from chromosom import Chromosom
from scaffold import ScaffoldImpExp
from markerImpExp import MarkerImpExp
from meaningImpExp import MeaningImpExp
from zprapp.models import Chromosome, Marker, Scaffold, Organism, Meaning, Sequence
from sekwencjaGff import SekwencjaGff
from sekwencjaFasta import SekwencjaFastaImpExp
from wyjatki import CheckError
from collections import namedtuple

class DataMigrations(object):
    def __init__(self):
        self.org = Organizm()
        self.chr = Chromosom()
        self.scaff = ScaffoldImpExp()
        self.marker = MarkerImpExp()
        self.meaning = MeaningImpExp()
        self.seqGff = SekwencjaGff()
        self.seqFasta = SekwencjaFastaImpExp()
        #wazna kolejnosc dla imports bo przekazuje dalej sobie slowniki utworzone
        self.obj_list = [self.org, self.chr, self.scaff, self.seqGff, self.seqFasta, self.marker, self.meaning]

    def check(self, file_list, obj_list= None):
        if obj_list == None:
            obj_list = self.obj_list
        if file_list.__len__() != obj_list.__len__():
            raise CheckError("zla liczba plikow do check()")
        for obj in zip(obj_list, file_list):
            obj[0].check(obj[1])

    def imports(self, file_list, obj_list= None):
        if obj_list == None:
            obj_list = self.obj_list
        slownik_import = namedtuple('Slownik_import', ['org', 'chr', 'scfld', 'seq', 'mrkr', 'mean'])
        slownik = slownik_import(org={}, chr={}, scfld={}, seq={}, mrkr={}, mean={})
        for obj in zip(obj_list, file_list):
            new_slownik = obj[0].import_records_from_file_to_db(obj[1], slownik)
            slownik = new_slownik

    def _prepare_lists_id(self, lista_id_org=None):
        if lista_id_org is not None:
            lista_id_chrms = []
            chrms = Chromosome.objects.filter(organism_id__in = lista_id_org)
            for c in chrms:
                lista_id_chrms.append(c.id)

            lista_id_scflds=[]
            scflds = Scaffold.objects.filter(chromosome_id__in = lista_id_chrms)
            for s in scflds:
                lista_id_scflds.append(s.id)

            # zbieram wszystkie id meaning jakie maja chromosomy
            lista_id_meaning = set()
            lista_id_mrkrs = []
            mrkrs = Marker.objects.filter(chromosome_id__in = lista_id_chrms)
            for m in mrkrs:
                lista_id_mrkrs.append(m.id)
                lista_id_meaning.add(m.meaning_id)
            lista_id_meaning = list(lista_id_meaning)


        else:
            return None, None, None, None

        return lista_id_chrms, lista_id_scflds, lista_id_meaning, lista_id_mrkrs

    def delete_organism_full(self, lista_id_org):
        ids_chrms, ids_scflds, _, ids_mrkrs = self._prepare_lists_id(lista_id_org)
        orgs = Organism.objects.filter(id__in = lista_id_org)
        for o in orgs:
            o.delete()
        chrms = Chromosome.objects.filter(id__in = ids_chrms)
        for c in chrms:
            c.delete()
        scflds = Scaffold.objects.filter(id__in = ids_scflds)
        for s in scflds:
            s.delete()
        mrkrs = Marker.objects.filter(id__in = ids_mrkrs)
        for m in mrkrs:
            m.delete()
        seqs = Sequence.objects.filter(scaffold_id__in = ids_scflds)
        for s in seqs:
            s.delete()
        # TODO usunac te meaningi ktore naleza tylko i wylacznie do tego organizmu



    def export(self, lista_orgs_id = None):
        print "rozpoczynam generacje (export) plikow z bazy"
        self.org.export_records_from_db_to_file("exported_data/org.gff", lista_orgs_id)
        self.chr.export_records_from_db_to_file("exported_data/chr.gff", lista_orgs_id)

        lista_id_chrms, lista_id_scflds, lista_id_meanings, _ = self._prepare_lists_id(lista_orgs_id)

        self.scaff.export_records_from_db_to_file("exported_data/scaff.gff", lista_id_chrms)
        self.seqFasta.export_records_from_db_to_file("exported_data/seq.fasta", limit= -1, lista_master_id=lista_id_scflds)
        self.seqGff.export_records_from_db_to_file("exported_data/seq.gff", lista_id_scflds)
        self.marker.export_records_from_db_to_file("exported_data/marker.gff", lista_id_chrms)
        self.meaning.export_records_from_db_to_file("exported_data/mean.gff", lista_id_meanings)
        print "zakonczylem generacje (export) plikow z bazy"



if __name__ == "__main__":
    data = DataMigrations()
    # exp.export([54,55])
    data.export([92])

    # chrms, mean = exp._prepare_lists_id([54])
    # print chrms
    # print  mean