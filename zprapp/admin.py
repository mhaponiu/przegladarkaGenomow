from django.contrib import admin
from zprapp.models import Organism, Chromosome, AnnotationType, Annotation, Aggregation

# Register your models here.
admin.site.register(Organism)
admin.site.register(Chromosome)
admin.site.register(AnnotationType)
admin.site.register(Annotation)
admin.site.register(Aggregation)
