from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, OrganismSerializer\
    , ChromosomeSerializer, AnnotationSerializer
from django.contrib.auth.models import User, Group
from zprapp.models import Organism, Chromosome, Annotation

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganismViewSet(viewsets.ModelViewSet):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer


class ChromosomeViewSet(viewsets.ModelViewSet):
    queryset = Chromosome.objects.all()
    serializer_class = ChromosomeSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer