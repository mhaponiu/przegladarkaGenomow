from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from zprapp.models import Organizm, Chromosom
from django.http import QueryDict
from django.core import serializers
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
    print "JSON Organizm.objects.all(): ", oall_json
    #print "dupa", request.REQUEST['id'];
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
    print "wypluje chromosomy organizmu", request.REQUEST['id_org'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    chrall = o.chromosom_set.all();
    chrall_json = serializers.serialize("json", chrall);
    print chrall_json;
    response = HttpResponse(chrall_json, content_type="application/json");
    return response;

def ajaxUsunChromosom(request):
    print "usuwam chromosom", request.REQUEST['id_org'], request.REQUEST['id_chr'];
    o = Organizm.objects.get(id = request.REQUEST['id_org']);
    chr = o.chromosom_set.get(id = request.REQUEST['id_chr']);
    chr.delete();
    print chr;
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

#pierwsza proba wymiany danych pomiedzy django a angularem przez get
def organizm(request, org_id):
    response = "Organizm o id: %s"
    #o = Organizm.objects.get(id = org_id)
    #o = get_object_or_404(Organizm, id = org_id)
    #return HttpResponse(o)
    organizm = Organizm.objects.get(id = org_id)
    context = {'organizm': organizm}
    return render(request, 'zprapp/index2.html', context)

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