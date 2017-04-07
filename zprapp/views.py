import json

from django.core import serializers
from django.db.models.expressions import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from zprapp.calc.calc import kmp
from zprapp.models import Chromosome, Organism;

@never_cache
@ensure_csrf_cookie
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


def ajaxContig(request):
    print "daje scaffoldy chromosomu ", request.GET['id_chr'];
    o = Organism.objects.get(id=request.GET['id_org']);
    ch = o.chromosome_set.get(id=request.GET['id_chr']);
    # ctgs = ch.annotation_set.values("start_chr", "length", "name")
    ctgs = ch.annotation_set.only("start_chr", "length", "name")
    #ch = Chromosome.objects.get(id=request.REQUEST['id_chr']);
    # scflds = ch.scaffold_set.all();
    print "liczba contigow to ", len(ctgs);
    ctg_json = serializers.serialize("json", ctgs);
    return HttpResponse(ctg_json, content_type="application/json");


def ajaxSekwencja(request):
    print "daje sekwencje chr:", request.GET['id_chr']," scaff: ", request.GET['id_sc'];
    o = Organism.objects.get(id=request.GET['id_org'])
    ch = o.chromosome_set.get(id=request.GET['id_chr'])
    ctg = ch.annotation_set.get(id=request.GET['id_sc'])
    return HttpResponse(ctg.sequence);
    # return HttpResponse(seq_json, content_type="application/json");

def ajaxOrganizmy(request):
    print "daje organizmy"
    orgs = Organism.objects.all();
    orgs_json = serializers.serialize("json", orgs);
    return HttpResponse(orgs_json, content_type="application/json");

def ajaxMeanings(request):
    return HttpResponse({"todo": "usun mnie"}, content_type="application/json");

def ajaxMarkers(request):
    print "daje markery"
    o = Organism.objects.get(id=request.GET['id_org'])
    ch = o.chromosome_set.get(id=request.GET['id_chr'])
    # mrkrs = ch.marker_set.all()
    # mrkrs_json = serializers.serialize("json", mrkrs)
    # return HttpResponse(mrkrs_json, content_type="application/json");
    return HttpResponse({"todo": "usun mnie"}, content_type="application/json");

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

    # return HttpResponse("DSFADS")

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

# @csrf_exempt
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

# @csrf_exempt #nie zawsze angular dodaje ciasteczko do responsa z tokenem - cos dziwnego
def ajaxDeleteOrganism(request):
    print "proba usuniecia"
    if request.method == "DELETE":
        print "usuwanie organizmu ",
        body = json.loads(request.body)
        print body['id_org']
        org_name = Organism.objects.get(id=body['id_org']).name

        # print 'odkomentuj mnie to usune organizm ', org_name
        # TODO odkomentowac to bedzie usuwanie
        DataMigrations().delete_organism_full([body['id_org']])

        return HttpResponse(org_name)
    else:
        return HttpResponse(status=405)

# @csrf_exempt
def ajaxSearchSeq(request):
    if request.method == "POST":
        body = json.loads(request.body);
        wzorzec = str(body['wzorzec']);
        # cel = str(body['cel'])
        # wynik = kmp(cel, wzorzec)

        ret = []
        org = Organism.objects.get(id=body['org'])
        chrms = org.chromosome_set.all()

        for chr in chrms:
            scflds = chr.scaffold_set.all()
            for scf in scflds:
                seq = str(scf.sequence_set.all()[0].sequence)
                pozycje = kmp(seq, wzorzec)
                # pozycje = []
                if pozycje == []:
                    continue
                ret_item={'org_id': org.id,
                          'chr_id': chr.id, 'scf_id': scf.id,
                          'pos': pozycje}
                ret.append(ret_item)

        # print wzorzec, cel;
        return JsonResponse(ret, safe=False)


# @csrf_exempt
#do celow testowych
def ajaxPost(request):
    print "request method: ", request.method;
    print "is_ajax: ", request.is_ajax();
    print "request.POST: ", request.POST;
    print "request.body: ", request.body;
    body = json.loads(request.body);
    print "body['data1']: ", body['data1'];
    print "request.GET['param1']: ", request.GET['param1'];
    return HttpResponse("JAKIS POST");
# var ajaxRequest = function(){
#         var request = {
#             method: 'POST',
#             url: 'ajax_post',
#             params: {param1: "p1p1p1", param2: "p2p2p2"}, //query string parametr
#             data: {data1: "d1d1d1", data2: "d2d2d2"} //ukryte data w poscie
#             //headers: {'Content-Type': 'application/x-www-form-urlencoded', //musi tak byc zeby posta dobrze odebralo, wiekszosc bibliotek JS tak robi
#             //            'X-Requested-With': 'XMLHttpRequest'} //zeby w django request.is_ajax dawalo true
#         };
#         $http(request)
#             .success(function (data) {
#                 console.log(data)
#             });
#     }


