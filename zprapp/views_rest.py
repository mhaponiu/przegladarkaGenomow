from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

from serializers import *
from django.contrib.auth.models import User, Group
from zprapp.models import Organism, Chromosome, Annotation
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin, DetailSerializerMixin
from paginations import MyPagination
from zprapp.contrib.cutter import Cutter
from zprapp.contrib.layerer import Layerer


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

    def filter_queryset(self, queryset):
        return super(AnnotationTypeViewSet, self).filter_queryset(queryset=queryset).distinct().order_by('id')

    @detail_route(methods=["GET"])
    def sequence(self, request, *args, **kwargs):
        print request.query_params
        params = request.query_params
        start = None
        end = None
        if 'start' in params: start = int(params['start'])
        if 'end' in params: end = int(params['end'])
        type = self.get_object()
        layerer = Layerer(type_priority_list=[type.id])
        annotations = layerer.compose()
        cutter = Cutter(annotations, start=start, end=end)
        return Response(cutter.sequence())


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


