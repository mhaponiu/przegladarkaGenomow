from django.contrib import admin
from zprapp.models import Organism, Chromosome, Marker, Scaffold, Meaning, Sequence

# Register your models here.
admin.site.register(Organism)
admin.site.register(Chromosome)
admin.site.register(Marker)
admin.site.register(Scaffold)
admin.site.register(Meaning)
admin.site.register(Sequence)