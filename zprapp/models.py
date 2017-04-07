from django.db import models

# Create your models here.

class Organism(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Chromosome(models.Model):
    number = models.IntegerField()
    length = models.IntegerField()
    organism = models.ForeignKey(Organism)
    ordered = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.number)

class AnnotationType(models.Model):
    name = models.TextField()
    short_name = models.TextField(null=True)

    def __unicode__(self):
        return self.name

class Annotation(models.Model):
    start_chr = models.IntegerField(null=True)
    length = models.IntegerField()
    name = models.TextField()
    sequence = models.TextField(null=True)
    aggregated_by = models.ForeignKey('Aggregation', null=True)
    type = models.ForeignKey(AnnotationType)
    chromosome = models.ForeignKey(Chromosome)

    def __unicode__(self):
        return self.name

class Aggregation(models.Model):
    start_local = models.IntegerField(null=True)
    annotation_master = models.ForeignKey(Annotation)
