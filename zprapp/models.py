from django.db import models

# Create your models here.

class Organizm(models.Model):
    nazwa = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nazwa

class Chromosom(models.Model):
    organizm = models.ForeignKey(Organizm)
    nazwa = models.CharField(max_length=50)
    dlugosc = models.BigIntegerField()

    def __unicode__(self):
        return self.nazwa

class Marker(models.Model):
    chromosom = models.ForeignKey(Chromosom)
    pozycja_od = models.BigIntegerField()
    pozycja_do = models.BigIntegerField()
    sekwencja = models.TextField()

    def __unicode__(self):
        return self.sekwencja
#OLD
##########################################################################
#NEW

class Chromosome(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    length = models.FloatField()

class Scaffold(models.Model):
    id = models.TextField(primary_key=True, null=False, unique=True)
    chromosome = models.ForeignKey(Chromosome)
    length = models.FloatField()
    order = models.IntegerField()
    #start = models.FloatField()
    #end = models.FloatField()


class Sequence(models.Model):
    scaffold = models.ForeignKey(Scaffold)
    sequence = models.TextField()
