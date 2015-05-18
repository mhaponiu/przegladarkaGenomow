from dbbase import DBBase
from zprapp.models import Organism, Chromosome
import psycopg2
import psycopg2.extras

class Chromosomes(DBBase):
    def glos(self):
        print 'Chromosomy '

    def create(self):
        print 'utworzono chromosomy'
        self._create_data_from_webomics_db()
        self._chromosomes_length_to_bp()
        self._create_data_for_other_organisms()

    def delete(self):
        chrs = Chromosome.objects.all()
        for ch in chrs:
            ch.delete();
        print "Usunieto chromosomy"

    def _create_data_from_webomics_db(self):
        print 'create_data_from_webomics_db'
            # wszystkie chromosomy do pierwszego organizmu daje
        try:
            conn = psycopg2.connect(self.CONNECT_STRING)
        except:
            print "CONNECT DATABASE ERROR"
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('''SELECT id, length_celera from chromosome_chromosome''')
        rows = cur.fetchall()
        org = Organism.objects.all()[0]
        for row in rows:
            org.chromosome_set.create(number=row['id'], length=row['length_celera'])
            # ch = Chromosome(number=row['id'], length=row['length_celera'])
            # ch.save();
        print "utworzono chromosomy"
        conn.close()

    def _chromosomes_length_to_bp(self):
        # length_bp from: http://onlinelibrary.wiley.com/doi/10.1111/j.1365-313X.2012.05017.x/pdf
        # http://www.biomedcentral.com/content/pdf/1471-2164-14-461.pdf
        length_bp = [29100000, 23200000, 42300000, 23800000, 27400000, 28600000, 18900000]

        #sum length_bp from scaffolds where assemb_type==1
        length_bp = [28150775, 25165221, 39056285, 28601718, 29950768, 33089568, 19250815]
        #kazdy zwiekszamy o 1Mbp zeby byly przerwy miedzy scaffoldami
        for l in range(length_bp.__len__()):
            length_bp[l]+=1000000
        ###################TESTOWO length_bp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #length_bp = [40000000]*7
        ###################TESTOWO length_bp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        chrms = Chromosome.objects.all()
        for chr in chrms:
            chr.length = length_bp[chr.number - 1]
            chr.save();
        print "chromosom: zmieniono jednostki length z cM na bp"

    def _create_data_for_other_organisms(self):
        #tworze recznie chromosomy dla organizmu 2 i 3 zeby cokolwiek sie wyswietlalo
        org = Organism.objects.all()
        o = org[1]
        for num, len in zip(range(1,12), range(100,5,-9)):
            chr = Chromosome(number = num, length = len, organism = o)
            chr.save()
        o = org[2]
        for num, len in zip(range(1,5), range(10, 101, 30)):
            chr = Chromosome(number = num, length = len, organism = o)
            chr.save()



