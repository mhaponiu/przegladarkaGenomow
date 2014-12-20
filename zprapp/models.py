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
