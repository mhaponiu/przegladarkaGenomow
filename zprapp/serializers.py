from rest_framework import serializers
from models import *

class OrganismSerializer(serializers.HyperlinkedModelSerializer):
    # chromosomes -> musi byc taka sama nazwa w related_name w model.py
    #teoretycznie nie trzeba uzywac tej linijki bo robi to za nas domyslnie HyperlinkedModelSerializer
    chromosomes = serializers.HyperlinkedRelatedField(many=True, queryset=Chromosome.objects.all(), view_name='chromosome-detail')

    class Meta:
        model = Organism
        fields = ('url', 'name', 'chromosomes')


class ChromosomeSerializer(serializers.HyperlinkedModelSerializer):
    #scaffolds -> musi byc taka sama nazwa w related_name w model.py
    # teoretycznie nie trzeba uzywac tej linijki bo robi to za nas domyslnie HyperlinkedModelSerializer
    scaffolds = serializers.HyperlinkedRelatedField(many=True, queryset=Scaffold.objects.all(), view_name='scaffold-detail')

    class Meta:
        model = Chromosome
        fields = ('url', 'number', 'length', 'organism', 'scaffolds')

class ScaffoldSerializer(serializers.HyperlinkedModelSerializer):
    # sequences = serializers.HyperlinkedRelatedField(many=False, queryset=Sequence.objects.all(), view_name='scaffold-rawseq')

    class Meta:
        model = Scaffold
        fields = ('url', 'pk', 'sequence', 'chromosome', 'length', 'order', 'start')


class SequenceSerializer(serializers.HyperlinkedModelSerializer):
    rawseq = serializers.HyperlinkedIdentityField(view_name='sequence-rawseq', many=False)
    class Meta:
        model = Sequence
        fields = ('url', 'scaffold', 'rawseq')