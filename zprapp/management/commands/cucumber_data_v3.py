from django.core.management.base import BaseCommand
from zpr.database.v3.db_inserter import Inserter

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.inserter = Inserter()

    # def add_arguments(self, parser):
        # parser.add_argument(
        #     '--no-delete',
        #     action='store_true',
        #     dest='no-delete',
        #     default=False
        # )
        # parser.add_argument(
        #     '--delete',
        #     action='store_true',
        #     dest='delete',
        #     default=False
        # )

    def handle(self, *args, **options):
        # if options['no-delete']:
        #     self.inserter.insert()
        #     return
        # if options['delete']:
        #     self.inserter.delete()
        #     return
        # self.inserter.delete()
        self.inserter.insert()