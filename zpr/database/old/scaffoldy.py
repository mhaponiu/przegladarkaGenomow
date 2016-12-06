import psycopg2
import psycopg2.extras

from zpr.database.dbbase import DBBase
from zprapp.models import Chromosome


class Scaffolds(DBBase):
    # def glos(self):
    #     print 'Scaffoldy! '

    def create(self):
        self._create_scaffolds_from_webomics_db()
        self._reorder_order()
        self._start_attr_gen()

    def delete(self):
        chrs = Chromosome.objects.all();
        for ch in chrs:
            scflds = ch.scaffold_set.all()
            for scf in scflds:
                scf.delete()
        print "usunieto scaffoldy"

    def _create_scaffolds_from_webomics_db(self):
        try:
            conn = psycopg2.connect(self.CONNECT_STRING)
        except:
            print "CONNECT DATABASE ERROR"
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('''select scaffold_scaffold.chromosome_id as chr_id,
                       scaffold_scaffold.id as scaff_id, scaffold_scaffoldposition.order,
                       length_bp from scaffold_scaffold, scaffold_scaffoldposition
                       where scaffold_scaffold.id = scaffold_scaffoldposition.scaff_id
                       order by chr_id, scaffold_scaffoldposition.order, scaff_id
                       ''')
        rows = cur.fetchall()
        chrms = Chromosome.objects.all()
        for row in rows:
            #chr = Chromosome.objects.get(number=row['chr_id'])
            chr = chrms[row['chr_id']-1]
            try:
                chr.scaffold_set.create(id=row['scaff_id'], length=row['length_bp'], order=row['order'], start=0)
            except:
                continue; #proba zapisania scaffolda o identycznym id ale innym order - pomijam taki
            #print row['chr_id'], row['scaff_id'], row['order'], row['length_bp'];
        print "utworzono scaffoldy"
        conn.close()

    def _reorder_order(self):
        chrs = Chromosome.objects.all();
        for chr in chrs:
            new_order = 0;
            scflds = chr.scaffold_set.all()
            scflds = sorted(scflds, key=lambda a: a.order)
            for sc in scflds:
                sc.order = new_order
                new_order = new_order + 1;
                sc.save();
        print "scaffold: przenumerowano order"

    def _start_attr_gen(self):
        for chr in Chromosome.objects.all():
            chr_len = chr.length
            scflds_suma_len = 0;
            scflds = chr.scaffold_set.all();
            for sc in scflds:
                scflds_suma_len += sc.length;
            przerwa = int((chr_len - scflds_suma_len) / (scflds.__len__() + 1))
            scflds = sorted(scflds, key=lambda a: a.order)
            start = 0;
            for sc in scflds:
                sc.start = start;
                start += sc.length + przerwa
                sc.save();
        print "scaffold: nadano atrybut start"

    def _get_data_without_bad_id(self):
        #takie scaffoldy ktore nie maja liter w id
        ID, LENGTH_BP, ASSEMB_TYPE = 0, 1, 2
        try:
            conn = psycopg2.connect(self.CONNECT_STRING)
        except:
            print "CONNECT DATABASE ERROR"
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select id, length_bp, assemb_type from scaffold_scaffold")
        data = cur.fetchall()
        scflds=[]
        for sc in data:
            try:
                scflds.append((int(sc[ID]), int(sc[LENGTH_BP]), sc[ASSEMB_TYPE]))
            except:
                continue;
        return scflds;

    def _get_data_with_bad_text_id(self):
        #sprawdza czy w id scaffolda nie ma np liter
        try:
            conn = psycopg2.connect(self.CONNECT_STRING)
        except:
            print "CONNECT DATABASE ERROR"
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select id, assemb_type from scaffold_scaffold")
        rows = cur.fetchall()
        bad_id = []
        for row in rows:
            try:
                id = row['id']
                int(id)
            except ValueError:
                bad_id.append((id, row['assemb_type']))
        return bad_id;