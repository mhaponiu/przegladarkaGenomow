from django.contrib.auth.models import User, Group
from rest_framework import serializers
from zprapp.models import Organism, Chromosome, Annotation

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'id')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class OrganismSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organism
        fields = ('url', 'name', 'id')


class ChromosomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chromosome
        fields = ("url", "number", "length", "organism", "order", 'id')


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Annotation
        fields = ("url", "start_chr", "length", "name",
                  "chromosome", "id")