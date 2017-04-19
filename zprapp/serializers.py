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


class OrganismChromosomesSerializer(serializers.HyperlinkedModelSerializer):
    chromosomes = serializers.PrimaryKeyRelatedField(many=True,
                                                     #queryset=Chromosome.objects.all(),
                                                     read_only=True)
    class Meta:
        model = Organism
        fields = ('url', 'name', 'id', "chromosomes")


class ChromosomeSerializer(serializers.HyperlinkedModelSerializer):
    organism_id = serializers.ReadOnlyField(source='organism.pk')
    class Meta:
        model = Chromosome
        fields = ("url", "number", "length", "organism", "ordered", 'id',
                  'organism_id')


class ChromosomeAnnotationSerializer(serializers.HyperlinkedModelSerializer):
    organism_id = serializers.ReadOnlyField(source='organism.pk')
    annotations = serializers.PrimaryKeyRelatedField(many=True,
                                                     read_only=True)
    class Meta:
        model = Chromosome
        fields = ("url", "number", "length", "organism", "ordered", 'id',
                  'organism_id', 'annotations')


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Annotation
        fields = ("url", "start_chr", "length", "name",
                  "chromosome", "id")