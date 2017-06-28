import sys, os
# from Sconstruct import VIRTUALENV_ROOT
from zprapp.dataloader.gff import Gff

sys.path.append([os.path.abspath('')])
os.environ['DJANGO_SETTINGS_MODULE'] = 'zpr.settings'
# sys.path.extend([os.path.join(VIRTUALENV_ROOT,'lib', 'python2.7', 'site-packages')])
import django
django.setup() #bez tego AppRegistryNotReady: Models aren't loaded yet.


from zprapp.dataloader.fasta import Fasta
from zprapp.models import Organism

class Exporter():
    def __init__(self, org):
        self.org = org

    def export_fasta_to_stream(self):
        fasta = Fasta(self.org)
        # fasta.export_records_from_db_to_file("dupa")
        stream = fasta.export_records_from_db_to_stream()
        return stream

    def export_fasta_to_file(self, filename):
        stream = self.export_fasta_to_stream()
        with open(filename, 'wt') as f:
            f.write(stream.read())

    def export_gff_to_stream(self):
        gff = Gff(self.org)
        stream = gff.export_records_from_db_to_stream()
        return stream

    def export_gff_to_file(self, filename):
        stream = self.export_gff_to_stream()
        with open(filename, 'wt') as f:
            f.write(stream.read())

    def export_exel(self):
        pass

    def export_zip_to_stream(self):
        pass

    def export_zip_to_file(self, filename):
        stream = self.export_zip_to_stream()
        with open(filename, 'wb') as f:
            f.write(stream.read())


if __name__ == "__main__":
    exp = Exporter(Organism.objects.all()[1])
    exp.export_gff_to_file("gff.gff")