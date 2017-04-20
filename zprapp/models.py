from django.db import models

# Create your models here.

class Organism(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Chromosome(models.Model):
    number = models.IntegerField()
    length = models.IntegerField()
    organism = models.ForeignKey(Organism, related_name="chromosomes", on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False) # if chromosom has annotation mapped in order

    def __unicode__(self):
        return str(self.number)

class AnnotationType(models.Model):
    name = models.TextField(unique=True)
    short_name = models.TextField(null=True)

    def __unicode__(self):
        return self.name

class Annotation(models.Model):
    start_chr = models.IntegerField(null=True)
    length = models.IntegerField()
    name = models.TextField()
    sequence = models.TextField(null=True)
    aggregated_by = models.OneToOneField('Aggregation', related_name='annotation_slaves',
                                         null=True)
    type = models.ForeignKey(AnnotationType)
    chromosome = models.ForeignKey(Chromosome, related_name="annotations", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Aggregation(models.Model):
    start_local = models.IntegerField(null=True)
    annotation_master = models.ForeignKey(Annotation, related_name='aggregation_slaves')
