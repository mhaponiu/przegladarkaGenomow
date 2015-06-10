# TODO wywalic ten blok importow
import sys,os
sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
from django.conf import settings
import django
django.setup()

from formatInterface import FormatInterface
from collections import namedtuple
from zprapp.models import Organism

class ImportOrganizm(FormatInterface):
    def __init__(self):
        super(ImportOrganizm, self).__init__(namedtuple('OrgGff', ['id', 'name']))

    def _gen_record_from_db(self):
        orgs = Organism.objects.all()
        for o in orgs.iterator():
            yield self.FormatRecord(o.id, o.name)

if __name__ == "__main__":
    a = ImportOrganizm()
    r = a.FormatRecord("777", "ogranizmmmmm")
    for  bbb in a._gen_record_from_db():
        print bbb