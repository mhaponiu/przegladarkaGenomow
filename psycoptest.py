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

def create_chromosomes():
    try:
        conn = psycopg2.connect(CONNECT_STRING)
    except:
        print "CONNECT DATABASE ERROR"
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('''SELECT id, length_celera from chromosome_chromosome''')
    rows = cur.fetchall()
    for row in rows:
        ch = Chromosome(id=row['id'], length=row['length_celera'])
        print "zapis chromosom:  id:", ch.id,"  length: ", ch.length
        ch.save();
    conn.close()

def create_scaffolds():
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
        chr = Chromosome.objects.get(id=row['chr_id'])
        try:
            chr.scaffold_set.create(id=row['scaff_id'], length=row['length_bp'], order=row['order'])
        except:
            continue; #proba zapisania scaffolda o identycznym id ale innym order - pomijam taki
        #print row['chr_id'], row['scaff_id'], row['order'], row['length_bp'];
    print "zapisano scaffoldy"

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

def create_sequences():
    #TODO wczytać do bazy django sekwencje
    pass



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