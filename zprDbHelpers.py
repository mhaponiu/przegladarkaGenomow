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
    oraz lokacje pliku xls z markerami podac do MARKER_FILE_LOCATION
'''
MARKER_FILE_LOCATION = "Cucumber_scaffold_markers.xls"
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
        przerwa = int((chr_len - scflds_suma_len) / (scflds.__len__() + 1))
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

def get_markers_from_xls():
    import xlrd;
    workbook = xlrd.open_workbook(MARKER_FILE_LOCATION);
    sheet = workbook.sheet_by_index(1);
    # for row in range(2, sheet.nrows):
    #     print sheet.cell_value(0, row)
    data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(2, sheet.nrows)]
    #data = [(int(d[0]), d[1], d[2], int(d[3]), int(d[4]), int(d[5]), int(d[6]), int(d[7]), int(d[8])) for d in data]
    return data

def get_scaffolds_with_bad_text_id():
    #sprawdza czy w id scaffolda nie ma np liter
    try:
        conn = psycopg2.connect(CONNECT_STRING)
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

def check_undef_sc_id_and_start_stop_markers():
    #UWAGA: czyta dane z bazy django a nie tej z backupu!
    #lepiej korzystac z get_good_bad_undef_markers():
    NAME, SC_ID, START, STOP = 1, 6, 7, 8;
    markers = get_markers_from_xls();
    undef_scfld_id=[]
    bad_start_stop_marker=[]
    for marker in markers:
        try:
            sc=Scaffold.objects.get(id=int(marker[SC_ID]))
            if sc.length < marker[START] or sc.length < marker[STOP]:
                bad_start_stop_marker.append((marker[NAME], marker[SC_ID]))
        except:
            undef_scfld_id.append((marker[NAME], marker[SC_ID]))
            continue;
    return undef_scfld_id, bad_start_stop_marker;

def check_undef_start_stop_markers(assemb_type=-1):
    #nie do konca dziala tak jak intuicja by nakazala ale jest teoretycznie dobrze
    #lepiej korzystac z get_good_bad_undef_markers():
    NAME, SC_ID, START, STOP = 1, 6, 7, 8;
    markers = get_markers_from_xls();
    bad_start_stop_marker=[];
    try:
        conn = psycopg2.connect(CONNECT_STRING)
    except:
        print "CONNECT DATABASE ERROR"
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if assemb_type == 0 or assemb_type == 1:
        cur.execute("select id, length_bp from scaffold_scaffold where assemb_type=%s", str(assemb_type))
    else:
        cur.execute("select id, length_bp from scaffold_scaffold")
    data = cur.fetchall()
    scflds_id = []
    scflds_len = []
    for sc in data:
        try:
            scflds_id.append(int(sc[0]))
            scflds_len.append(sc[1])
        except:
            continue;
    #scflds = zip(scflds_id, scflds_len)
    undef_scfld_id =[]
    cur.execute("select id, length_bp from scaffold_scaffold")
    #scflds_all = [sc[0] for sc in cur.fetchall()]
    scflds_all=[]
    for sc in cur.fetchall():
        try:
            scflds_all.append(int(sc[0]))
        except:
            continue;
    for marker in markers:
        if int(marker[SC_ID]) in scflds_id:
            index = scflds_id.index(marker[SC_ID],)
            sc_len = scflds_len[index]
            if sc_len < marker[START] or sc_len < marker[STOP]:
                bad_start_stop_marker.append((marker[NAME], marker[SC_ID]))
        else:
            if int(marker[SC_ID]) not in scflds_all:
                undef_scfld_id.append((marker[NAME], marker[SC_ID]))
    return undef_scfld_id, bad_start_stop_marker;

def get_scaffolds_all_without_bad_id():
    ID, LENGTH_BP, ASSEMB_TYPE = 0, 1, 2
    try:
        conn = psycopg2.connect(CONNECT_STRING)
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

def get_good_bad_undef_markers():
    markers = get_markers_from_xls();
    NAME, SC_ID, START, STOP = 1, 6, 7, 8;
    markers = [(int(d[0]), d[NAME], d[2], int(d[3]), int(d[4]), int(d[5]), int(d[SC_ID]), int(d[START]), int(d[STOP])) for d in markers]
    scflds = get_scaffolds_all_without_bad_id()
    ID, LENGTH_BP, ASSEMB_TYPE = 0, 1, 2;
    scflds_id = [sc[ID] for sc in scflds]
    scflds_length = [sc[LENGTH_BP] for sc in scflds]
    scflds_assemb_type = [sc[ASSEMB_TYPE] for sc in scflds]
    good_markers=[]
    bad_markers=[]
    undef_markers=[]
    for marker in markers:
        if marker[SC_ID] not in scflds_id:
            undef_markers.append((marker[NAME], marker[SC_ID]))
            continue;
        else:
            index = scflds_id.index(marker[SC_ID],)
            sc_len = scflds_length[index]
            sc_assemb_type = scflds_assemb_type[index]
            if sc_len < marker[START] or sc_len < marker[STOP]:
                bad_markers.append({'name':marker[NAME], 'sc_id':marker[SC_ID], 'sc_len':sc_len, 'start':marker[START], 'stop':marker[STOP] ,'assemb_type':sc_assemb_type})
            else:
                good_markers.append({'name':marker[NAME], 'sc_id':marker[SC_ID], 'sc_len':sc_len, 'start':marker[START], 'stop':marker[STOP] ,'assemb_type':sc_assemb_type})
    return good_markers, bad_markers, undef_markers









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