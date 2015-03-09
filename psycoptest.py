import sys, django;
sys.path.extend(['/home/mhaponiu/workspace/Pycharm workspace/zpr', '/home/mhaponiu/pycharm-4.0/helpers/pycharm', '/home/mhaponiu/pycharm-4.0/helpers/pydev'])
try:
    django.setup()
except:
    print "error django.setup(), ale w sumie to nic nie zmienia chyba"
import django_manage_shell;
django_manage_shell.run("/home/mhaponiu/workspace/Pycharm workspace/zpr")
from zprapp.models import Chromosome, Scaffold, Sequence;
import psycopg2
import psycopg2.extras;

'''
    nalezy wczytac backup bazy danych '17.11.2012-cucumber_plain.backup'
    do nowo utworzonej bazy i wpisac jej dane do ponizszego CONNECT_STRING'a
'''
CONNECT_STRING = "dbname='ogorek_roboczy' user='zpr' host='localhost' password='zpr'"

def delete_chromosomes():
    chrs = Chromosome.objects.all()
    for ch in chrs:
        ch.delete();
    print "Usunieto chromosomy"

def create_chromosomes_from_webomics_db():
    try:
        conn = psycopg2.connect(CONNECT_STRING)
    except:
        print "CONNECT DATABASE ERROR"
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('''SELECT id, length_celera from chromosome_chromosome''')
    rows = cur.fetchall()
    for row in rows:
        ch = Chromosome(number=row['id'], length=row['length_celera'])
        # print "zapis chromosom:  id:", ch.id,"  length: ", ch.length
        ch.save();
    print "zapisano chromosomy"
    conn.close()

def chromosomes_lenght_to_bp():
    # length_bp from: http://onlinelibrary.wiley.com/doi/10.1111/j.1365-313X.2012.05017.x/pdf
    # http://www.biomedcentral.com/content/pdf/1471-2164-14-461.pdf
    length_bp = [29100000, 23200000, 42300000, 23800000, 27400000, 28600000, 18900000]

    ###################TESTOWO length_bp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    length_bp = [40000000]*7
    ###################TESTOWO length_bp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    chrms = Chromosome.objects.all()
    for chr in chrms:
        chr.length = length_bp[chr.number - 1]
        chr.save();
    print "chromosom: zmieniono jednostki length z cM na bp"

def create_scaffolds_from_webomics_db():
    try:
        conn = psycopg2.connect(CONNECT_STRING)
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
    for row in rows:
        chr = Chromosome.objects.get(number=row['chr_id'])
        try:
            chr.scaffold_set.create(id=row['scaff_id'], length=row['length_bp'], order=row['order'], start=0)
        except:
            continue; #proba zapisania scaffolda o identycznym id ale innym order - pomijam taki
        #print row['chr_id'], row['scaff_id'], row['order'], row['length_bp'];
    print "zapisano scaffoldy"
    conn.close()

def scaffolds_reorder_order():
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

def scaffolds_start_attr_gen():
    for chr in Chromosome.objects.all():
        chr_len = chr.length
        scflds_suma_len = 0;
        scflds = chr.scaffold_set.all();
        for sc in scflds:
            scflds_suma_len += sc.length;
        przerwa = (chr_len - scflds_suma_len) / (scflds.__len__() + 1)
        scflds = sorted(scflds, key=lambda a: a.order)
        start = 0;
        for sc in scflds:
            sc.start = start;
            start += sc.length + przerwa
            sc.save();
    print "scaffold: nadano atrybut start"


def delete_scaffolds():
    chrs = Chromosome.objects.all();
    for ch in chrs:
        scflds = ch.scaffold_set.all()
        for scf in scflds:
            scf.delete()
    print "usunieto scaffoldy"

def delete_sequences():
    chrs = Chromosome.objects.all();
    for ch in chrs:
        scflds = ch.scaffold_set.all()
        for scf in scflds:
            sqncs = scf.sequence_set.all()
            for sq in sqncs:
                sq.delete()
    print "usunieto sekwencje"

def create_sequences_from_webomics_db():
    try:
        conn = psycopg2.connect(CONNECT_STRING)
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

def delete_all():
    print "trwa usuwanie..."
    delete_sequences();
    delete_scaffolds();
    delete_chromosomes();

def create_all():
    print "trwa tworzenie danych..."
    create_chromosomes_from_webomics_db()
    chromosomes_lenght_to_bp()
    create_scaffolds_from_webomics_db()
    scaffolds_reorder_order()
    scaffolds_start_attr_gen()
    create_sequences_from_webomics_db()
    print "zakonczono tworzenie danych"

# try:
#     conn = psycopg2.connect(CONNECT_STRING)
# except:
#     print "CONNECT DATABASE ERROR"
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


# try:
#     conn = psycopg2.connect("dbname='ogorek_roboczy' user='zpr' host='localhost' password='zpr'")
# except:
#     print "CONNECT DATABASE ERROR"
# cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
#
# # cur.execute(''' SELECT * FROM scaffold_scaffold LIMIT 10''')
# # rows = cur.fetchall()
#
# #dodanie chromosomow
# cur.execute('''SELECT id, length_celera from chromosome_chromosome''')
# rows = cur.fetchall()
# for row in rows:
#     ch = Chromosome(id = row['id'], length = row['length_celera'])
#     print "zapis lewy chromosom: ", ch.id, ch.length
#     #ch.save();
#
#
# print Chromosome.objects.all();

# print rows[0]['id'];
# print rows[0]['length_bp'];
# for r in range(5):
#     print rows[0][r];

#print type(rows[0][0]);
# for row in rows:
#     print row;
# conn.close()
# print "koniec"