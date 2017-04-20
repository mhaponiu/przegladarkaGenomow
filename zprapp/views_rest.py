from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.parsers import JSONParser

from serializers import *
from django.contrib.auth.models import User, Group
from zprapp.models import Organism, Chromosome, Annotation
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganismViewSet(viewsets.ModelViewSet):
    queryset = Organism.objects.all()
    # serializer_class = OrganismSerializer
    serializer_class = OrganismChromosomesSerializer


class AnnotationTypeViewSet(viewsets.ModelViewSet):
    queryset = AnnotationType.objects.all()
    serializer_class = AnnotationTypeSerializer


# class ChromosomeViewSet(viewsets.ModelViewSet):
#     queryset = Chromosome.objects.all()
#     serializer_class = ChromosomeSerializer
#
#     @detail_route(methods=["GET"])
#     def annotations(self, request, *args, **kwargs):
#         chromosome = self.get_object()
#         annotations = chromosome.annotations.all()
#         ret = [a.id for a in annotations]
#         return Response(ret)


class ChromosomeList(generics.ListCreateAPIView):
    queryset = Chromosome.objects.all()
    serializer_class = ChromosomeSerializer


class ChromosomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chromosome.objects.all()
    serializer_class = ChromosomeAnnotationSerializer


class AnnotationList(APIView):
    def post(self, request, format=None):
        print request.data
        id_list = json.loads(request.data['id']) # list of annotations ids
        annotations = Annotation.objects.filter(id__in=id_list)
        serializer = AnnotationSerializer(annotations, many=True)
        return Response(serializer.data)



class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

    @detail_route(methods=["GET"])
    def sequence(self, request, *args, **kwargs):
        ''' /annotations/3/sequence/ da sama sekwencje'''
        annotation = self.get_object()
        return Response(annotation.sequence)

