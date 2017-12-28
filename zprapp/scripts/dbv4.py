from django.db import transaction
from drop_exception import drop_exception
from zpr.database.v4_refresh.data_structures.inserter import Inserter
from zprapp.models import Organism



# @drop_exception
@transaction.atomic
def run():
    inserter = Inserter()
    inserter.insert()
    # raise KeyError