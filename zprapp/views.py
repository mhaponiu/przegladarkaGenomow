from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from zprapp.models import Organizm, Chromosom, Marker;
from django.http import QueryDict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'zprapp/index.html')

def organizmy(request):
    return render(request, 'zprapp/organizmy.html')

def chromosomy(request):
    return render(request, 'zprapp/chromosomy.html')

def markery(request):
    return render(request, 'zprapp/markery.html')

def ajaxOrganizmy(request):
    oall = Organizm.objects.all();
    oall_json = serializers.serialize("json", oall);
    print "daje wszystkie organizmy";
    #print "JSON Organizm.objects.all(): ", oall_json
    #print "ajaxOrganizm: serialize JSON Organizm.objects.all():", oall_json;
    #o1 = Organizm.objects.get( id = request.REQUEST['id']);
    #o1_json = serializers.serialize("json", o1);
    #o2 = Organizm.objects.get( id = 2);
    #print "ajaxOrganizm:",o1, o2;
    #o2_json = serializers.serialize("json", o2);
    #print "serialize JSON o2:", o2_json;
    #response = JsonResponse({'nazwa': o1.nazwa});
    response = HttpResponse(oall_json, content_type="application/json");
    return response;

def ajaxOrganizm(request):
    #print "jestem w ajaxOrganizm o org_id =  ", request.REQUEST['id'];
    o = Organizm.objects.get(id = request.REQUEST['id']);
    return JsonResponse({'nazwa': o.nazwa, 'id': o.id});

def ajaxNowyOrganizm(request):
    print "zapisuje nowy organizm: ", request.REQUEST['nazwa'];
    o = Organizm(nazwa = request.REQUEST['nazwa']);
    o.save();
    #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
    oall = Organizm.objects.all();
    oall_json = serializers.serialize("json", oall);
    #print "ajaxNowyOrganizm JSON Organizm.all():", oall_json;
    response = HttpResponse(oall_json, content_type="application/json");
    return response;

def ajaxUsunOrganizm(request):
    print "usuwam organizm o id: ", request.REQUEST['id'];
    o = Organizm.objects.get(id = request.REQUEST['id']);
    o.delete();
    #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
    oall = Organizm.objects.all();
    oall_json = serializers.serialize("json", oall);
    #print "ajaxNowyOrganizm JSON Organizm.all():", oall_json;
    response = HttpResponse(oall_json, content_type="application/json");
    return response;

def ajaxEdytujOrganizm(request):
    print "edytuje organizm o id: ", request.REQUEST['id'], " i nadaje mu nazwe ", request.REQUEST['nazwa'];
    o = Organizm.objects.get(id = request.REQUEST['id']);
    o.nazwa = request.REQUEST['nazwa'];
    o.save();
    #zwracam wszystkie organizmy zeby zaktualizowac liste wszystkich
    oall = Organizm.objects.all();
    oall_json = serializers.serialize("json", oall);
    #print "ajaxEdytujOrganizm JSON Organizm.all():", oall_json;
    response = HttpResponse(oall_json, content_type="application/json");
    return response;

def ajaxChromosomy(request):
    print "daje chromosomy organizmu", request.REQUEST['id_org'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    chrall = o.chromosom_set.all();
    chrall_json = serializers.serialize("json", chrall);
    #print chrall_json;
    response = HttpResponse(chrall_json, content_type="application/json");
    return response;

def ajaxChromosom(request):
    #print "jestem w ajaxOrganizm o org_id =  ", request.REQUEST['id'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    chr = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    return JsonResponse({'nazwa': chr.nazwa, 'dlugosc': chr.dlugosc});

def ajaxUsunChromosom(request):
    print "usuwam chromosom", request.REQUEST['id_org'], request.REQUEST['id_chr'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    chr = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    chr.delete();
    chrall = o.chromosom_set.all();
    chrall_json = serializers.serialize("json", chrall);
    response = HttpResponse(chrall_json, content_type="application/json");
    return response;

def ajaxNowyChromosom(request):
    print "nowy chromosom w org ", request.REQUEST['id_org'], request.REQUEST['nazwa'], request.REQUEST['dlugosc'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    o.chromosom_set.create(nazwa = request.REQUEST['nazwa'], dlugosc = request.REQUEST['dlugosc']);
    chrall = o.chromosom_set.all();
    chrall_json = serializers.serialize("json", chrall);
    response = HttpResponse(chrall_json, content_type="application/json");
    return response;

def ajaxEdytujChromosom(request):
    print "edytuje chromosom", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['nazwa'], request.REQUEST['dlugosc'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    ch.nazwa = request.REQUEST['nazwa'];
    ch.dlugosc = request.REQUEST['dlugosc'];
    ch.save();
    chrall = o.chromosom_set.all();
    chrall_json = serializers.serialize("json", chrall);
    response = HttpResponse(chrall_json, content_type="application/json");
    return response;

def ajaxMarkery(request):
    print "daje markery", request.REQUEST['id_org'], request.REQUEST['id_chr'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    markall = ch.marker_set.all();
    markall_json = serializers.serialize("json", markall);
    response = HttpResponse(markall_json, content_type="application/json");
    return response;

def ajaxNowyMarker(request):
    print "nowy marker", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['sekwencja'], request.REQUEST['poz_od'], request.REQUEST['poz_do'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    ch.marker_set.create(pozycja_od = request.REQUEST['poz_od'], pozycja_do = request.REQUEST['poz_do'], sekwencja = request.REQUEST['sekwencja']);
    markall = ch.marker_set.all();
    markall_json = serializers.serialize("json", markall);
    response = HttpResponse(markall_json, content_type="application/json");
    return response;

def ajaxUsunMarker(request):
    print "usuwam marker", request.REQUEST['id_org'], request.REQUEST['id_chr'], request.REQUEST['id_mark'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    ch = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    m = ch.marker_set.get(id = request.REQUEST['id_mark']);
    m.delete();
    markall = ch.marker_set.all();
    markall_json = serializers.serialize("json", markall);
    response = HttpResponse(markall_json, content_type="application/json");
    return response;

def ajaxEdytujMarker(request):
    print "Edytuje marker", request.REQUEST['o'], request.REQUEST['ch'], request.REQUEST['m'], request.REQUEST['od'], request.REQUEST['do'], request.REQUEST['s'];
    o = Organizm.objects.get(id = request.REQUEST['o']);
    ch = o.chromosom_set.get(id = request.REQUEST['ch']);
    m = ch.marker_set.get(id = request.REQUEST['m']);
    m.pozycja_od = request.REQUEST['od'];
    m.pozycja_do = request.REQUEST['do'];
    m.sekwencja = request.REQUEST['s'];
    m.save();
    markall = ch.marker_set.all();
    markall_json = serializers.serialize("json", markall);
    response = HttpResponse(markall_json, content_type="application/json");
    return response;

@csrf_exempt #dzieki temu dziala post w ogole
def ajaxPost(request):
    oall = Organizm.objects.all();
    oall_json = serializers.serialize("json", oall);
    # print "proba posta: organizmy wszystkie"
    print "request method: ";
    print request.method;
    print request.REQUEST;
    req = request.body;
    #req_des = serializers.deserialize("json", req);
    #req_json = serializers.serialize("json", req);
    req2 = unicode("["+request.body+"]");
    req2_json = json.loads(req2);

    # dziala
    req3 = unicode(request.body);
    req3_json = json.loads(req3);
    print req3_json['url'];


    #req_json = serializers.serialize("json", req2);
    #print req_json;

    #print request.REQUEST['o']
    #print oall_json;
    #response = HttpResponse(oall_json, content_type="application/json");
    #return response;
    return HttpResponse("JAKIS POST");



#pierwsza proba wymiany danych pomiedzy django a angularem przez get (udana)
def odpowiedz(request):
    liczba = request.REQUEST['id']
    #req = request.POST['id']
    if request.method == 'POST':
        print "JEST POSTEM"
        print request.POST;
    elif request.method == 'GET':
        print "JEST GETEM"
    elif request.is_ajax():
        print("JEST AJAX")
    print "slownik GET", request.GET;
    print "slownik POST", request.POST;
    print request;
    #data = json.loads(request.body);
    #print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True);

    #print request.body['TEXTDOMAIN'];
    response = JsonResponse({'klucz': liczba})
    #organizm = Organizm.objects.get(id = 2)
    #return HttpResponse(organizm.nazwa);
    return response