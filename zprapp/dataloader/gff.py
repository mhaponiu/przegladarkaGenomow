from formatInterface import FormatInterface
from collections import namedtuple
# from zprapp.models import Sequence, Scaffold, Chromosome
import re, io


class Gff(FormatInterface):
    GffRecord = namedtuple('GffRecord', ['org_name',
                                         'chr_number', 'chr_length', 'chr_ordered',
                                         'type_name', 'type_short_name',
                                         'annotation_start_chr', 'annotation_length',
                                         'annotation_name', 'annotation_id',
                                         'annotation_master', 'start_on_master'])

    def __init__(self, org):
        self.org = org

    def import_records_from_file_to_db(self, filename):
        for record in self._gen_record_from_file(filename):
            print record
            #TODO zapisac record do bazy

    def _gen_record_from_file(self, filename):
        with open(filename, 'rt') as f:
            for line in f:
                record_tab = re.split(r'[\t\n]', line)[:-1]
                yield self.GffRecord(*record_tab)


    def export_records_from_db_to_file(self, filename, limit=-1):
        with open(filename, 'wt') as f:
            ORGANICZENIE = 0
            for record in self._gen_record_from_db():
                # FIXME sztuczne ograniczenie, usunc je mozna
                if ORGANICZENIE == limit: break
                ORGANICZENIE+=1

                for r in record:
                    f.write(unicode(r))
                    f.write('\t')
                f.seek(f.tell()-1)
                f.write('\n')

    def export_records_from_db_to_stream(self):
        stream = io.StringIO()
        stream.write(unicode("# org_name\tchr_number\tchr_length\tchr_ordered\ttype_name\ttype_short_name\tannotation_start_chr\tannotation_length\tannotation_name\tannotation_id\tannotation_master\tstart_on_master\n"))
        for record in self._gen_record_from_db():
            for r in record:
                stream.write(unicode(r))
                stream.write(unicode('\t'))
            stream.seek(stream.tell() - 1)
            stream.write(unicode('\n'))
        stream.seek(0)
        return stream


    def _gen_record_from_db(self):
        for chromosome in self.org.chromosomes.all():
            annotations = chromosome.annotations.all()
            for a in annotations.iterator():
                try:
                    aggregation = a.aggregated_by
                    master = aggregation.annotation_master.id
                    start_on_master = aggregation.start_local
                except:
                    master = None
                    start_on_master = None
                yield self.GffRecord(self.org.name,
                                     chromosome.number, chromosome.length, chromosome.ordered,
                                     a.type.name, a.type.short_name,
                                     a.start_chr, a.length,
                                     a.name, a.id,
                                     master, start_on_master)
                # yield self.GffRecord(s.id, int(scfld.start), int(scfld.length), scfld.order, scfld.chromosome_id)