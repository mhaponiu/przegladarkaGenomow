from pprint import pprint

from django.http.request import RawPostDataException
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView

from serializers import *
from django.contrib.auth.models import User, Group
from zprapp.models import Organism, Chromosome, Annotation
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin, DetailSerializerMixin
from paginations import MyPagination
from zprapp.contrib.trimmer import Trimmer
from zprapp.contrib.layerer import Layerer
import json
from zprapp.calc.calc_webomics.build import calc

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganismViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    model = Organism
    queryset = Organism.objects.all()
    # serializer_class = OrganismSerializer
    serializer_class = OrganismChromosomesSerializer

class AnnotationTypeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer


class AnnotationTypeSeqSectionViewSet(AnnotationTypeViewSet):

    def filter_queryset(self, queryset):
        return super(AnnotationTypeViewSet, self).filter_queryset(queryset=queryset).distinct().order_by('id')

    @detail_route(methods=["GET"])
    def sequence(self, request, *args, **kwargs):
        '''
        @:param start -- widok od na chromosomie
        @:param end -- widok do na chromosomie
        widok dobrze dziala przy posrednim przechodzeniu
        organism/chromosom/annotation_type/sequence
        lub
        chromosom/annotation_type/sequence'''
        params = request.query_params
        if 'parent_lookup_annotations__chromosome' in kwargs:
            chromosome = int(kwargs['parent_lookup_annotations__chromosome'])
        else:
            chromosome = None
        start = None
        end = None
        if 'start' in params: start = int(params['start'])
        if 'end' in params: end = int(params['end'])
        type = self.get_object()
        layerer = Layerer(type_priority_list=[type.id], chromosome=chromosome)
        annotations = layerer.compose()
        trimmer = Trimmer(annotations, start_chr=start, end_chr=end)
        return Response(trimmer.sequence())


class AggregationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Aggregation.objects.all()
    serializer_class = AggregationSerializer


class PaginatedAggregationViewSet(AggregationViewSet):
    pagination_class = MyPagination


class ChromosomeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    model = Chromosome
    queryset = Chromosome.objects.all()
    serializer_class = ChromosomeSerializer


class AnnotationViewSet(DetailSerializerMixin, NestedViewSetMixin, viewsets.ModelViewSet):
    model = Annotation
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    # serializer_detail_class = AnnotationDetailSerializer
    serializer_detail_class = AnnotationSerializer # uwaga, to zwykly AnnotationSerializer - nie wersja Detail

    @detail_route(methods=["GET"])
    def sequence(self, request, *args, **kwargs):
        annotation = self.get_object()
        return Response(annotation.sequence)


class PaginatedAnnotationViewSet(AnnotationViewSet):
    pagination_class = MyPagination


class AnnotationAggregationViewSet(AnnotationViewSet):
    serializer_class = AnnotationAggregationSerializer
    # serializer_detail_class = AnnotationAggregationDetailSerializer
    serializer_detail_class = AnnotationAggregationSerializer # uwaga, to zwykly Serializer - nie wersja Detail


class PaginatedAnnotationAggregationViewSet(AnnotationAggregationViewSet):
    pagination_class = MyPagination


class CalcView(APIView):
    '''
    http POST localhost:8000/api/calc/ alg_id=323 pattern=AACCTTGG alg_params:='{"w":7, "t":24}' alg_name=KMP annotations_params:='{"org_id":123, "chr_id":3, "type_id":123}'
    '''
    algoritms = {
        1: {'name': 'KMP'}, # Algorytm Knutha-Morrisa-Pratha
        2: {'name': 'Boyer'},# Algorytm Boyera-Moore'a
        3: {'name': 'BLAST'}, # Basic Local Alignment Search Tool
        4: {'name': 'SW'} # Smitha-Watermana
    }
    def post(self, request):
        try:
            # jak leci z angulara to post data jest w "data" a jak z httpie to w body, nie wiem o co chodzi
            body = json.loads(request.body)
        except RawPostDataException:
            body = request.data
        alg_id = int(body['alg_id'])
        alg_name = body['alg_name']
        alg_params = body['alg_params']
        pattern = str(body['pattern'])
        annotation_params = body['annotation_params']
        # pprint(body)

        # przygotowanie adnotacji do przeszukiwania
        annotations = Annotation.objects.filter(chromosome__organism= annotation_params['org_id'],
                                                    chromosome= annotation_params['chr_id'],
                                                    type=annotation_params['type_id'])

        results = []
        if alg_id == 1:
            print("KMP")
            kmp = calc.KMP()
            kmp.calculateTable(pattern)
            pattern_length=len(pattern)
            for a in annotations:
                ret ={"org_id": a.chromosome.organism_id, "chr_id": a.chromosome_id, "ann_id": a.id, 'ann_type': a.type_id}
                positions = kmp.compute(str(a.sequence)) # todo wolne -> zmiana z unicode na stringa sekwencji
                # korekcja pozycji o 1 w lewo (w apce od 0 a algorytm od 1)
                positions = [(p-1, p-1+pattern_length) for p in positions]
                ret['pos'] = list(positions)
                results.append(ret)

        elif alg_id == 2:
            print("BM")
            bm = calc.BM()
            bm.prepare(pattern)
            pattern_length = len(pattern)
            for a in annotations:
                ret ={"org_id": a.chromosome.organism_id, "chr_id": a.chromosome_id, "ann_id": a.id, 'ann_type': a.type_id}
                positions = bm.compute(str(a.sequence))  # todo wolne -> zmiana z unicode na stringa sekwencji
                # korekcja pozycji o 1 w lewo (w apce od 0 a algorytm od 1)
                positions = [(p-1, p-1+pattern_length) for p in positions]
                ret['pos'] = list(positions)
                results.append(ret)

        elif alg_id == 3:
            print("BLAST")
            w = 11
            t = 0.001
            c = 5
            cutoff = 10
            blast = calc.Blast(w,t,c)
            blast.prepare(pattern)
            for a in annotations:
                blast.addSequence(str(a.id), str(a.sequence))
            res_search = blast.search()
            assert res_search is True
            res_estimate = blast.estimate()
            assert res_estimate is True
            res_extend = blast.extend()
            assert res_extend is True
            res_evaluate = blast.evaluate()
            assert res_evaluate is True
            aligns = blast.getAligns(cutoff)
            aligns_len = len(aligns)
            for align in aligns:
                same = align.getSame()
                align_len = align.getAlignLength()
                seq_id = align.getSequenceId()
                a = Annotation.objects.get(id = seq_id)
                res = {
                    'identity': str((float(same) / float(align_len) * 100.00)),
                    "org_id": a.chromosome.organism_id,
                    "chr_id": a.chromosome_id,
                    "ann_id": a.id,
                    'ann_type': a.type_id,
                    'pos': [(a.start_chr + align.getSeqStart(), a.start_chr + align.getSeqEnd())],
                    'length': str(align_len)
                }
                results.append(res)
            return JsonResponse(results, safe=False)
            # return JsonResponse([{"org_id": 23, "chr_id": 55, "ann_id": 24159, "pos": [2, 5], 'ann_type':23}], safe=False)


        elif alg_id == 4:
            print("SW")
            AKCEPTOWALNE_PODOBIENSTWO = float(0.5)
            sw = calc.SW()
            match = 2
            mismach = -1
            gap_open = -3
            gap_extended = -1

            for a in annotations:
                s = sw.fastComputeWithStringsResult(match, mismach, gap_open, gap_extended, str(a.sequence), pattern)

                # score = s.getValue()  # int
                # print("score (getValue)", score)  # SCORE wartosc podobienstwa porownywanych tekstow -> suma matchy , kar itd dla tekstu
                pat_after = s.getPattern()  # std::string wspolny podobny fragment patterna
                # print("pat_after (getPattern)", pat_after)
                seq_after = s.getText()  # std::string odnaleziony fragment w szukanej sekwencji ale z  "-" tak gdzie znak sie nie zgadza (jest inny albo brakuje)
                # print("seq_after (getText)", seq_after)
                align_len = len(s.getText())
                # print("align_len (len getText)", align_len)
                gaps = 0
                same = 0
                for i, l in enumerate(seq_after):
                    if l == '-':
                        gaps += 1
                    elif l == pat_after[i]:  # takie same
                        same += 1
                # print("gaps", gaps)
                # print("same", same)
                seq_end_index = s.getPositionJ()
                aim_end_index = s.getPositionI()
                aim_start_index = aim_end_index - len(seq_after)
                seq_start_index = seq_end_index - len(str(seq_after).replace("-", ""))
                identity = float(same) / float(align_len)
                print("identity", identity)
                print("aim start_index", aim_start_index)
                print("aim end_index", aim_end_index)
                # print("seq_end_index", seq_end_index)
                # print("seq_start_index", seq_start_index)

                if identity > AKCEPTOWALNE_PODOBIENSTWO:
                    ret = {"org_id": a.chromosome.organism_id, "chr_id": a.chromosome_id, "ann_id": a.id,
                           'ann_type': a.type_id}
                    ret['identity']=identity
                    ret['pos']=[(a.start_chr + aim_start_index,  a.start_chr + aim_end_index)]
                    results.append(ret)
        return JsonResponse(results, safe=False)
        # return JsonResponse([{"org_id": 23, "chr_id": 55, "ann_id": 24159, "pos": [2, 5], 'ann_type':23}], safe=False)



