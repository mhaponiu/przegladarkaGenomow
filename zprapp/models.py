from django.db import models

# Create your models here.

# class Organizm(models.Model):
#     nazwa = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.nazwa
#
# class Chromosom(models.Model):
#     organizm = models.ForeignKey(Organizm)
#     nazwa = models.CharField(max_length=50)
#     dlugosc = models.BigIntegerField()
#
#     def __unicode__(self):
#         return self.nazwa
#
# class Marker(models.Model):
#     chromosom = models.ForeignKey(Chromosom)
#     pozycja_od = models.BigIntegerField()
#     pozycja_do = models.BigIntegerField()
#     sekwencja = models.TextField()
#
#     def __unicode__(self):
#         return self.sekwencja
#OLD
##########################################################################
#NEW
class Organism(models.Model):
    name = models.TextField()

class Chromosome(models.Model):
    number = models.IntegerField()
    length = models.FloatField()
    organism = models.ForeignKey(Organism)

class Scaffold(models.Model):
    id = models.TextField(primary_key=True, null=False, unique=True)
    chromosome = models.ForeignKey(Chromosome)
    length = models.FloatField()
    order = models.IntegerField()
    start = models.FloatField()
    #start = models.FloatField()
    #end = models.FloatField()

class Meaning(models.Model):
    mean = models.TextField()

class Marker(models.Model):
    name = models.TextField()
    start = models.FloatField()
    length = models.FloatField()
    meaning = models.ForeignKey(Meaning)
    chromosome = models.ForeignKey(Chromosome)

class Sequence(models.Model):
    scaffold = models.ForeignKey(Scaffold)
    sequence = models.TextField()
