from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

from serializers import *
from django.contrib.auth.models import User, Group
from zprapp.models import Organism, Chromosome, Annotation
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.mixins import NestedViewSetMixin, DetailSerializerMixin
from paginations import MyPagination
import json


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


class AnnotationTypeViewSet(viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer


class ChromosomeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    model = Chromosome
    queryset = Chromosome.objects.all()
    serializer_class = ChromosomeSerializer


class AnnotationViewSet(DetailSerializerMixin, NestedViewSetMixin, viewsets.ModelViewSet):
    model = Annotation
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    serializer_detail_class = AnnotationDetailSerializer

    @detail_route(methods=["GET"])
    def sequence(self, request, *args, **kwargs):
        annotation = self.get_object()
        return Response(annotation.sequence)


class PaginatedAnnotationViewSet(AnnotationViewSet):
    pagination_class = MyPagination


