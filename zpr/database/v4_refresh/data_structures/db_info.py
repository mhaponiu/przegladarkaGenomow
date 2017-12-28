from zprapp.models import Annotation

class DbInfo():
    def __init__(self, organism):
        ''':param models.Organism'''
        print "DbInfo, zaciagam queryset"
        self.queryset = Annotation.objects.filter(chromosome__organism=organism)
        print "DbInfo, zaciagniete"

    def get(self, id):
        self.queryset.get(name=str(id))
