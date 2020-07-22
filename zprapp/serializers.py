from django.contrib.auth.models import User, Group
from rest_framework import serializers
from zprapp.models import Organism, Chromosome, Annotation, AnnotationType, Aggregation

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'id')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')


class AnnotationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationType
        fields = ("name", "short_name", "id")


class OrganismChromosomesSerializer(serializers.ModelSerializer):
    chromosomes = serializers.PrimaryKeyRelatedField(many=True,
                                                     #queryset=Chromosome.objects.all(),
                                                     read_only=True)
    class Meta:
        model = Organism
        fields = ('name', 'id', "chromosomes")


class ChromosomeSerializer(serializers.ModelSerializer):
    # organism_id = serializers.ReadOnlyField(source='organism.pk')
    class Meta:
        model = Chromosome
        fields = ("number", "length", "organism", "ordered", 'id')


class ChromosomeAnnotationSerializer(serializers.ModelSerializer):
    organism_id = serializers.ReadOnlyField(source='organism.pk')
    annotations = serializers.PrimaryKeyRelatedField(many=True,
                                                     queryset=Annotation.objects.all(),
                                                     read_only=False)
    class Meta:
        model = Chromosome
        fields = ("number", "length", "organism", "ordered", 'id',
                  'organism_id', 'annotations')


class AnnotationSerializer(serializers.ModelSerializer):
    # type = AnnotationTypeSerializer()
    type = serializers.ReadOnlyField(source='type.name')
    annotation_main = serializers.ReadOnlyField(source='aggregated_by.annotation_main.id')

    class Meta:
        model = Annotation
        fields = ("start_chr", "length", "name",
                  "chromosome", "id", "type", "annotation_main")


class AnnotationDetailSerializer(AnnotationSerializer):
    class Meta(AnnotationSerializer.Meta):
        fields = AnnotationSerializer.Meta.fields + ("sequence",)


class AnnotationAggregationSerializer(AnnotationSerializer):
    start_local = serializers.ReadOnlyField(source='aggregated_by.start_local')

    class Meta(AnnotationSerializer.Meta):
        fields = AnnotationSerializer.Meta.fields + ('start_local',)


class AnnotationAggregationDetailSerializer(AnnotationDetailSerializer, AnnotationAggregationSerializer):
    class Meta(AnnotationDetailSerializer.Meta, AnnotationAggregationSerializer.Meta):
        fields = tuple(set(AnnotationDetailSerializer.Meta.fields + AnnotationAggregationSerializer.Meta.fields))


class AggregationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Aggregation
        fields = ("id", "start_local", "annotation_main", "annotation_subordinate")