

from django.db import transaction

from tree import Tree
from zprapp.models import Annotation, Organism
from zpr.database.v3.db_inserter import Inserter as V3_Inserter


class Inserter(V3_Inserter):
    def __init__(self, organism=Organism.objects.first()):
        super(Inserter, self).__init__()
        self.tree = Tree()
        self.tree.create()

    def tree_preorder(self):
        return self.tree.preorder_iter()

    def _organisms(self):
        return [Organism(name="Cucumber_v4_refresh")]

