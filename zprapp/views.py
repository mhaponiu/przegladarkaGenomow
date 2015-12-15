import json

from django.core import serializers
from django.db.models.expressions import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from zprapp.import_export.chromosom import Chromosom
from zprapp.import_export.dataMigrations import DataMigrations
from zprapp.import_export.organizm import Organizm
from zprapp.import_export.scaffold import ScaffoldImpExp
from zprapp.import_export.sekwencjaFasta import SekwencjaFastaImpExp
from zprapp.import_export.sekwencjaGff import SekwencjaGff
from zprapp.import_export.wyjatki import CheckError
from zprapp.models import Chromosome, Organism, Meaning;


def index(request):
    return render(request, 'zprapp/index.html')

# def organizmy(request):
#     return render(request, 'zprapp/organizmy.html')
# def chromosomy(request):
#     return render(request, 'zprapp/chromosomy.html')
# def sekwencja(request):
#     return render(request, 'zprapp/sekwencja.html')
# def scaffoldy(request):
#     return render(request, 'zprapp/scaffoldy.html')

def ajaxChromosomy(request):
    print "daje chromosomy"
    if 'id_chr_len' in request.GET:
        chall = [Chromosome.objects.get(id = request.GET['id_chr_len'])]
    else:
        o = Organism.objects.get(id=request.GET['id_org'])
        #chall = Chromosome.objects.all();
        chall = o.chromosome_set.all();
    chall_json = serializers.serialize("json", chall);
    # print chall_json;
    return HttpResponse(chall_json, content_type="application/json");

# def ajaxChromLength(request):
#     print "daje chr_len"
#     ch = Chromosome.objects.get(id=request.REQUEST['id'])


def ajaxScaffoldy(request):
    print "daje scaffoldy chromosomu ", request.GET['id_chr'];
    o = Organism.objects.get(id=request.GET['id_org']);
    ch = o.chromosome_set.get(id=request.GET['id_chr']);
    scflds = ch.scaffold_set.all();
    #ch = Chromosome.objects.get(id=request.REQUEST['id_chr']);
    # scflds = ch.scaffold_set.all();
    print "liczba scaffoldow to ", len(scflds);
    scflds_json = serializers.serialize("json", scflds);
    return HttpResponse(scflds_json, content_type="application/json");


def ajaxSekwencja(request):
    print "daje sekwencje chr:", request.GET['id_chr']," scaff: ", request.GET['id_sc'];
    o = Organism.objects.get(id=request.GET['id_org'])
    ch = o.chromosome_set.get(id=request.GET['id_chr'])
    scfld = ch.scaffold_set.get(id=request.GET['id_sc'])
    # ch = Chromosome.objects.get(id=request.REQUEST['id_chr']);
    # scfld = ch.scaffold_set.get(id=request.REQUEST['id_sc']);
    seq = scfld.sequence_set.all()[0];# liscie sekwencji i tak jest jedna tylko
    print seq;
    #seq_json = serializers.serialize("json", seq)
    #print seq_json;
    return HttpResponse(seq.sequence);
    # return HttpResponse(seq_json, content_type="application/json");

def ajaxOrganizmy(request):
    print "daje organizmy"
    orgs = Organism.objects.all();
    orgs_json = serializers.serialize("json", orgs);
    return HttpResponse(orgs_json, content_type="application/json");

def ajaxMeanings(request):
    print "daje meanings"
    means = Meaning.objects.all();
    means_json = serializers.serialize("json", means);
    return HttpResponse(means_json, content_type="application/json");

def ajaxMarkers(request):
    print "daje markery"
    o = Organism.objects.get(id=request.GET['id_org'])
    ch = o.chromosome_set.get(id=request.GET['id_chr'])
    mrkrs = ch.marker_set.all()
    mrkrs_json = serializers.serialize("json", mrkrs)
    return HttpResponse(mrkrs_json, content_type="application/json");

def ajaxSeqSection(request):
    # print request.GET['id_chr'], request.GET['widok_od'],request.GET['widok_do']
    # TODO odeslac poprawny wycinek
    id_chr = request.GET['id_chr']
    widok_od = int(request.GET['widok_od'])
    widok_do = int(request.GET['widok_do'])
    chr = Chromosome.objects.get(id=id_chr)
    chr_len = chr.length
    selected_scflds = chr.scaffold_set.annotate(end=F('start')+F('length')) \
        .filter(start__lt=widok_do, end__gt=widok_od) \
        .order_by('order')

    ret_string = bytearray('N'*(widok_do-widok_od))
    # print "empty_ret_string", ret_string

    if selected_scflds.__len__() == 0:
        return HttpResponse(ret_string.decode())

    def zeroToNone(arg):
        if arg == 0:
            return None
        else:
            return int(arg)

    def noneToZero(arg):
        if arg == None:
            return 0
        else:
            return int(arg)

    for sc in selected_scflds:
        string_od = None
        string_do = None
        if widok_od > sc.start:
            seq_od = int(widok_od - sc.start)
            string_od = None
        elif widok_od <= sc.start:
            seq_od = None
            string_od = zeroToNone(int(abs(sc.start - widok_od)))
        if widok_do < sc.end:
            seq_do = int(widok_do - sc.start)
            string_do = None
        elif widok_do >= sc.end:
            seq_do = None
            # string_do zdefiniowany pozniej -> musze znac dlugosc_write_seq

        write_seq = sc.sequence_set.first().sequence[seq_od:seq_do]

        if widok_do >= sc.end:
            string_do = noneToZero(string_od) + write_seq.__len__()

        ret_string[string_od:string_do] = str(write_seq)
        # print "seq_od", seq_od
        # print "seq_do", seq_do
        # print "write_seq", write_seq
        # print "write_seq_len", write_seq.__len__()
        # print "string_od ",string_od
        # print "string_do ",string_do
        # print "ret_string", ret_string
    return HttpResponse(ret_string.decode())



    # if selected_scflds.__len__() == 0:
    #     # raise Exception("PUSTA TABLICA SCAFFOLDOW")
    #     return HttpResponse("ERROR")
    #
    # elif selected_scflds.__len__() == 1 :
    #     sc_one = selected_scflds[0]
    #     # od___####___do
    #     if sc_one.start > widok_od and sc_one.end < widok_do:
    #         # TODO wypelnic luka
    #         seq_list.append(sc_one.sequence_set.first().sequence)
    #         # TODO wypelnic luka
    #         return HttpResponse(seq_list)
    #     # ###OD###___DO
    #     elif sc_one.start <= widok_od and sc_one.end < widok_do:
    #         seq_list.append(sc_one.sequence_set.first().sequence[widok_od:])
    #         # TODO luka
    #     # ###OD###DO###
    #     elif sc_one.start <= widok_od and sc_one.end >= widok_do:
    #         seq_list.append(sc_one.sequence_set.first().sequence[widok_od:widok_do])
    #     # OD__###DO###
    #     elif sc_one.start > widok_od and sc_one.end >= widok_do:
    #         # TODO luka
    #         seq_list.append(sc_one.sequence_set.first().sequence[:widok_do])
    #
    #
    # # TODO  pierwsza ucieta sekwencja
    # # poczatek wyswietlanego widoku jest w luce przed pierwszym scaffoldem
    # if selected_scflds[0].start > widok_od:
    #     seq_list.append(selected_scflds[0].sequence_set.first().sequence)
    # else:
    #     seq_list.append(selected_scflds[0].sequence_set.first().sequence[widok_od:])
    #
    # if selected_scflds.__len__() >= 2:
    #     # TODO srodek sekwencji
    #     for sc in selected_scflds[1:-1]:
    #         seq_list.append(sc.sequence_set.first().sequence)
    #
    # # TODO ostatnia ucieta sekwencja
    # # koniec wyswietlanego widoku jest w luce za ostatnim scaffoldem
    # if selected_scflds[-1].end < widok_do:
    #     seq_list.append(selected_scflds[-1].sequence_set.first().sequence)
    # else:
    #     seq_list.append(selected_scflds[-1].sequence_set.first().sequence[:widok_do])

    return HttpResponse("DSFADS")

def test(request):
    #TODO zrobic tak zeby post'a przyjmowal i byl w ajaxSekwencja
    # print "TEST widok_od:", request.REQUEST['widok_od']," widok_do: ", request.REQUEST['widok_do'];
    # return HttpResponse("TEST OD SERWERA");
    ch = Chromosome.objects.all()[0];
    scfld = ch.scaffold_set.all()[0];
    seq = scfld.sequence_set.all()[0];# liscie sekwencji i tak jest jedna tylko
    #seq_json = serializers.serialize("json", seq)
    #print seq_json;
    return HttpResponse(seq.sequence[:1000]);

def ajaxNewOrganism(request):
    wynik = True;
    wiadomosc = "wiadomosc z serwera po odebraniu plikow"

    if request.method == 'POST':
        try:
            files = request.FILES.getlist('file') #lista plikow w kolejnosci jak wysylalismy
            obj_list = None # domyslna lista obj_list -> DataMigrations.obj_list
            obj_list = [Organizm(), Chromosom(), ScaffoldImpExp(), SekwencjaGff(), SekwencjaFastaImpExp()]
            # for f in files:
            #     print "plik: ", f, " zawartosc: ", f.read()
            # print "plik: ", files[0], " zawartosc: ", files[0].read()

            # obj_list = [SekwencjaFastaImpExp()]

            data_migr = DataMigrations()
            # obj_list domyslnie w data_migr => musi byc zgodne z pozycjami przeslanymi od klienta
            data_migr.check(file_list=files, obj_list=obj_list) #sprawdza poprawnosc struktur plikow

            # zapisuje dane do bazy
            data_migr.imports(file_list=files, obj_list=obj_list)

        except CheckError as error:
            wynik = False
            wiadomosc = error.msg + ". Blad w rekordzie " + str(error.n_record)
            # wiadomosc = error.msg
        except:
            wynik = False
            wiadomosc = "SERWER ERROR, blad przetwarzania plikow"
    else:
        wynik = False
        wiadomosc = "SERVER ERROR, blad uploadu"


    return JsonResponse({'success': wynik, 'message': wiadomosc});

def ajaxDeleteOrganism(request):
    print "usuwanie organizmu ",
    body = json.loads(request.body)
    print body['id_org']
    org_name = Organism.objects.get(id=body['id_org']).name

    print 'odkomentuj mnie to usune organizm ', org_name
    # TODO odkomentowac to bedzie usuwanie
    # DataMigrations().delete_organism_full([body['id_org']])

    return HttpResponse(org_name)

# @csrf_exempt
#do celow testowych
def ajaxPost(request):
    print "request method: ", request.method;
    print "is_ajax: ", request.is_ajax();
    print "request.REQUEST: ", request.POST;
    print "request.body: ", request.body;
    body = json.loads(request.body);
    print "body['data1']: ", body['data1'];
    print "request.REQUEST['param1']: ", request.REQUEST['param1'];
    return HttpResponse("JAKIS POST");


######################################### STARE ################################
#
# def organizmy(request):
#     return render(request, 'zprapp/old/organizmy.html')
#
# def markery(request):
#     return render(request, 'zprapp/old/markery.html')
#
# def ajaxOrganizmy(request):
#     oall = Organizm.objects.all();
#     oall_json = serializers.serialize("json", oall);
#     print "daje wszystkie organizmy";
#     #print "JSON Organizm.objects.all(): ", oall_json
#     #print "ajaxOrganizm: serialize JSON Organizm.objects.all():", oall_json;
#     #o1 = Organizm.objects.get( id = request.REQUEST['id']);
#     #o1_json = serializers.serialize("json", o1);
#     #o2 = Organizm.objects.get( id = 2);
#     #print "ajaxOrganizm:",o1, o2;
#     #o2_json = serializers.serialize("json", o2);
#     #print "serialize JSON o2:", o2_json;
#     #response = JsonResponse({'nazwa': o1.nazwa});
#     response = HttpResponse(oall_json, content_type="application/json");
#     return response;
#
# def ajaxOrganizm(request):
#     #print "jestem w ajaxOrganizm o org_id =  ", request.REQUEST['id'];
#     o = Organizm.objects.get(id = request.REQUEST['id']);
#     return JsonResponse({'nazwa': o.nazwa, 'id': o.id});
#
# def ajaxNowyOrganizm(request):
#     print "zapisuje nowy organizm: ", request.REQUEST['nazwa'];
#     o = Organizm(nazwa = request.REQUEST['nazwa']);
#     o.save();
#     #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
#     oall = Organizm.objects.all();
#     oall_json = serializers.serialize("json", oall);
#     #print "ajaxNowyOrganizm JSON Organizm.all():", oall_json;
#     response = HttpResponse(oall_json, content_type="application/json");
#     return response;
#
# def ajaxUsunOrganizm(request):
#     print "usuwam organizm o id: ", request.REQUEST['id'];
#     o = Organizm.objects.get(id = request.REQUEST['id']);
#     o.delete();
#     #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
#     oall = Organizm.objects.all();
#     oall_json = serializers.serialize("json", oall);
#     #print "ajaxNowyOrganizm JSON Organizm.all():", oall_json;
#     response = HttpResponse(oall_json, content_type="application/json");
#     return response;
#
# def ajaxEdytujOrganizm(request):
#     print "edytuje organizm o id: ", request.REQUEST['id'], " i nadaje mu nazwe ", request.REQUEST['nazwa'];
#     o = Organizm.objects.get(id = request.REQUEST['id']);
#     o.nazwa = request.REQUEST['nazwa'];
#     o.save();
#     #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
#     oall = Organizm.objects.all();
#     oall_json = serializers.serialize("json", oall);
#     #print "ajaxEdytujOrganizm JSON Organizm.all():", oall_json;
#     response = HttpResponse(oall_json, content_type="application/json");
#     return response;
#
# def ajaxChromosomy(request):
#     print "daje chromosomy organizmu", request.REQUEST['id_org'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     chrall = o.chromosom_set.all();
#     chrall_json = serializers.serialize("json", chrall);
#     #print chrall_json;
#     response = HttpResponse(chrall_json, content_type="application/json");
#     return response;
#
# def ajaxChromosom(request):
#     #print "jestem w ajaxOrganizm o org_id =  ", request.REQUEST['id'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     chr = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     return JsonResponse({'nazwa': chr.nazwa, 'dlugosc': chr.dlugosc});
#
# def ajaxUsunChromosom(request):
#     print "usuwam chromosom", request.REQUEST['id_org'], request.REQUEST['id_chr'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     chr = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     chr.delete();
#     chrall = o.chromosom_set.all();
#     chrall_json = serializers.serialize("json", chrall);
#     response = HttpResponse(chrall_json, content_type="application/json");
#     return response;
#
# def ajaxNowyChromosom(request):
#     print "nowy chromosom w org ", request.REQUEST['id_org'], request.REQUEST['nazwa'], request.REQUEST['dlugosc'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     o.chromosom_set.create(nazwa = request.REQUEST['nazwa'], dlugosc = request.REQUEST['dlugosc']);
#     chrall = o.chromosom_set.all();
#     chrall_json = serializers.serialize("json", chrall);
#     response = HttpResponse(chrall_json, content_type="application/json");
#     return response;
#
# def ajaxEdytujChromosom(request):
#     print "edytuje chromosom", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['nazwa'], request.REQUEST['dlugosc'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     ch.nazwa = request.REQUEST['nazwa'];
#     ch.dlugosc = request.REQUEST['dlugosc'];
#     ch.save();
#     chrall = o.chromosom_set.all();
#     chrall_json = serializers.serialize("json", chrall);
#     response = HttpResponse(chrall_json, content_type="application/json");
#     return response;
#
# def ajaxMarkery(request):
#     print "daje markery", request.REQUEST['id_org'], request.REQUEST['id_chr'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     markall = ch.marker_set.all();
#     markall_json = serializers.serialize("json", markall);
#     response = HttpResponse(markall_json, content_type="application/json");
#     return response;
#
# def ajaxNowyMarker(request):
#     print "nowy marker", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['sekwencja'], request.REQUEST['poz_od'], request.REQUEST['poz_do'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     ch.marker_set.create(pozycja_od = request.REQUEST['poz_od'], pozycja_do = request.REQUEST['poz_do'], sekwencja = request.REQUEST['sekwencja']);
#     markall = ch.marker_set.all();
#     markall_json = serializers.serialize("json", markall);
#     response = HttpResponse(markall_json, content_type="application/json");
#     return response;
#
# def ajaxUsunMarker(request):
#     print "usuwam marker", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['id_mark'];
#     o = Organizm.objects.get(id = request.REQUEST['id_org']);
#     ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
#     m = ch.marker_set.get(id = request.REQUEST['id_mark']);
#     m.delete();
#     markall = ch.marker_set.all();
#     markall_json = serializers.serialize("json", markall);
#     response = HttpResponse(markall_json, content_type="application/json");
#     return response;
#
# def ajaxEdytujMarker(request):
#     print "Edytuje marker", request.REQUEST['o'], request.REQUEST['ch'], request.REQUEST['m'], request.REQUEST['od'], request.REQUEST['do'], request.REQUEST['s'];
#     o = Organizm.objects.get(id = request.REQUEST['o']);
#     ch = o.chromosom_set.get(id = request.REQUEST['ch']);
#     m = ch.marker_set.get(id = request.REQUEST['m']);
#     m.pozycja_od = request.REQUEST['od'];
#     m.pozycja_do = request.REQUEST['do'];
#     m.sekwencja = request.REQUEST['s'];
#     m.save();
#     markall = ch.marker_set.all();
#     markall_json = serializers.serialize("json", markall);
#     response = HttpResponse(markall_json, content_type="application/json");
#     return response;
#
# @csrf_exempt #dzieki temu dziala post w ogole
# def ajaxPost(request):
#     oall = Organizm.objects.all();
#     oall_json = serializers.serialize("json", oall);
#     # print "proba posta: organizmy wszystkie"
#     print "request method: ";
#     print request.method;
#     print request.REQUEST;
#     req = request.body;
#     #req_des = serializers.deserialize("json", req);
#     #req_json = serializers.serialize("json", req);
#     req2 = unicode("["+request.body+"]");
#     req2_json = json.loads(req2);
#
#     # dziala
#     req3 = unicode(request.body);
#     req3_json = json.loads(req3);
#     print req3_json['params']['o'];
#
#
#     #req_json = serializers.serialize("json", req2);
#     #print req_json;
#
#     #print request.REQUEST['o']
#     #print oall_json;
#     #response = HttpResponse(oall_json, content_type="application/json");
#     #return response;
#     return HttpResponse("JAKIS POST");
#
#
#
# #pierwsza proba wymiany danych pomiedzy django a angularem przez get (udana)
# def odpowiedz(request):
#     liczba = request.REQUEST['id']
#     #req = request.POST['id']
#     if request.method == 'POST':
#         print "JEST POSTEM"
#         print request.POST;
#     elif request.method == 'GET':
#         print "JEST GETEM"
#     elif request.is_ajax():
#         print("JEST AJAX")
#     print "slownik GET", request.GET;
#     print "slownik POST", request.POST;
#     print request;
#     #data = json.loads(request.body);
#     #print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True);
#
#     #print request.body['TEXTDOMAIN'];
#     response = JsonResponse({'klucz': liczba})
#     #organizm = Organizm.objects.get(id = 2)
#     #return HttpResponse(organizm.nazwa);
#     return response