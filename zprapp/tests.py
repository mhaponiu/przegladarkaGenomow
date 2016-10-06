from itertools import chain

from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.test import TestCase

from zprapp.models import *
from zprapp.views import *


# Create your tests here.
class GetSequenceSectionScaffCanvasTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #                 0 1 2 3 4 5       0  1  2  3  4  5  6  7
        # chromosom  # # # A G T C A # #  #  G  T  C  A  G  T  C  #  #  #
        # index     0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
        o = Organism(name="organizm_testowy1", id=1)
        chr = Chromosome(organism=o, number=1, length=21, id=1)
        cls.chr_id = chr.id
        sc1 = Scaffold(chromosome=chr, length=5, order=0, start=3, id=1)
        seq1 = Sequence(scaffold=sc1, sequence="AGTCA", id=1)
        sc2 = Scaffold(chromosome=chr, length=7, order=1, start=11, id=2)
        seq2 = Sequence(scaffold=sc2, sequence="GTCAGTC", id=2)
        for obj in chain([o, chr, sc1, sc2, seq1, seq2]):
            obj.save()

    def test_view_ajaxSeqSection_1(self):
        # _[seq)
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '1'
        request.GET['widok_do'] = '4'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'NNA')

    def test_view_ajaxSeqSection_2(self):
        # (seq)
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '4'
        request.GET['widok_do'] = '7'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'GTC')

    def test_view_ajaxSeqSection_3(self):
        # [seq)
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '3'
        request.GET['widok_do'] = '6'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'AGT')

    def test_view_ajaxSeqSection_4(self):
        # [seq]
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '3'
        request.GET['widok_do'] = '8'
        response=ajaxSeqSection(request)
        # self.assertContains(response, 'AGTCA')
        self.assertEqual(response.content.decode(), 'AGTCA')

    def test_view_ajaxSeqSection_5(self):
        # [seq]_
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '3'
        request.GET['widok_do'] = '10'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'AGTCANN')

    def test_view_ajaxSeqSection_6(self):
        # _[seq]_
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '1'
        request.GET['widok_do'] = '10'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'NNAGTCANN')

    def test_view_ajaxSeqSection_7(self):
        # (seq]_
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '5'
        request.GET['widok_do'] = '10'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'TCANN')

    def test_view_ajaxSeqSection_8(self):
        # (seq]
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '5'
        request.GET['widok_do'] = '8'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'TCA')

    def test_view_ajaxSeqSection_9(self):
        # (seq]__[seq)
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '6'
        request.GET['widok_do'] = '13'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'CANNNGT')

    def test_view_ajaxSeqSection_10(self):
        # __[seq]__[seq)
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '2'
        request.GET['widok_do'] = '13'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'NAGTCANNNGT')

    def test_view_ajaxSeqSection_11(self):
        # __[seq]__[seq]__
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '2'
        request.GET['widok_do'] = '20'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'NAGTCANNNGTCAGTCNN')

    def test_view_ajaxSeqSection_12(self):
        # begin__[seq]__[seq]__end
        request=HttpRequest()
        request.GET['id_chr'] = self.chr_id
        request.GET['widok_od'] = '0'
        request.GET['widok_do'] = '21'
        response=ajaxSeqSection(request)
        self.assertEqual(response.content.decode(), 'NNNAGTCANNNGTCAGTCNNN')

class TestUrlResolver(TestCase):
    def test_url_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_url_ajax_organizmy(self):
        found = resolve('/ajax_orgs')
        self.assertEqual(found.func, ajaxOrganizmy)

    def test_url_ajax_chromosomy(self):
        found = resolve('/ajax_chrmy')
        self.assertEqual(found.func, ajaxChromosomy)

    def test_url_ajax_skafoldy(self):
        found = resolve('/ajax_scfldy')
        self.assertEqual(found.func, ajaxScaffoldy)

    def test_url_ajax_sekwencje(self):
        found = resolve('/ajax_scs')
        self.assertEqual(found.func, ajaxSekwencja)

    def test_url_ajax_meanings(self):
        found = resolve('/ajax_meanings')
        self.assertEqual(found.func, ajaxMeanings)

    def test_url_ajax_markery(self):
        found = resolve('/ajax_markers')
        self.assertEqual(found.func, ajaxMarkers)

    def test_url_ajax_nowy_org(self):
        found = resolve('/ajax_newOrganism')
        self.assertEqual(found.func, ajaxNewOrganism)

    def test_url_ajax_usun_organizm(self):
        found = resolve('/ajax_deleteOrganism')
        self.assertEqual(found.func, ajaxDeleteOrganism)

    def test_url_resolver_to_get_sequence_section(self):
        found = resolve('/ajax_seqSection')
        self.assertEqual(found.func, ajaxSeqSection)


class TestModel(TestCase):
    def test_save_and_read_organizm(self):
        org = Organism(name="org1", id=1)
        org.save()
        o = Organism.objects.get(id=1)
        self.assertEqual(o.name, org.name)

    def test_save_and_read_chromosom(self):
        org = Organism(name="org1", id=1)
        chr = Chromosome(number=3, id=1, organism=org, length=34)
        chr.save()
        ch = Chromosome.objects.get(id=1)
        self.assertEqual(chr.number, ch.number)
        self.assertEqual(chr.length, ch.length)

    def test_save_and_read_skafold(self):
        org = Organism(name="org1", id=1)
        chr = Chromosome(number=3, id=1, organism=org, length=34)
        scfld = Scaffold(chromosome=chr, length=243, order=3, start=5, id=4)
        scfld.save()
        sc = Scaffold.objects.get(id=4)
        self.assertEqual(scfld.start, sc.start)
        self.assertEqual(scfld.order, sc.order)

    def test_save_and_read_marker(self):
        org = Organism(name="org1", id=1)
        chr = Chromosome(number=3, id=1, organism=org, length=34)
        mean = Meaning(mean="dasf", id=8)
        marker = Marker(chromosome=chr, id=3, length=342, name="fdas", start=34, meaning=mean)
        marker.save()
        m = Marker.objects.get(id=3)
        self.assertEqual(marker.start, m.start)
        self.assertEqual(marker.length, m.length)








