from django.contrib import admin
from zprapp.models import Organism, Chromosome, AnnotationType, Annotation, Aggregation

# Register your models here.
class AnnotationAdmin(admin.ModelAdmin):
    model = Annotation
    list_per_page = 100

admin.site.register(Organism)
admin.site.register(Chromosome)
admin.site.register(AnnotationType)
admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Aggregation)
