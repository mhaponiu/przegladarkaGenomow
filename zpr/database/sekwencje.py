from dbbase import DBBase
from zprapp.models import Chromosome, Scaffold
import psycopg2
import psycopg2.extras

class Sequences(DBBase):
    def glos(self):
        print 'Sekwencje! '

    def create(self):
        print "tworze sekwencje"
        self._create_sequences_from_webomics_db()

    def delete(self):
        chrs = Chromosome.objects.all()
        for ch in chrs:
            scflds = ch.scaffold_set.all()
            for scf in scflds:
                sqncs = scf.sequence_set.all()
                for sq in sqncs:
                    sq.delete()
        print "usunieto sekwencje"

    def _create_sequences_from_webomics_db(self):
        try:
            conn = psycopg2.connect(self.CONNECT_STRING)
        except:
            print "CONNECT DATABASE ERROR"
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('''select id, sequence from scaffold_scaffold''')
        rows = cur.fetchall()
        for row in rows:
            scfld = Scaffold.objects.get(id=row['id'])
            scfld.sequence_set.create(sequence=row['sequence'])
            #OperationalError: index row requires 121032 bytes, maximum size is 8191
        print "utworzono sekwencje"
        conn.close()
