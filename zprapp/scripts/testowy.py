from django.db import transaction
from drop_exception import drop_exception
from zpr.database.v4.parser import Fasta_454

@drop_exception(msg="\nEXCEPTION OCCURED")
@transaction.atomic
def run():
    parser = Fasta_454()
    gen = parser.generator()
    n1 = next(gen)
    print n1

    raise Exception