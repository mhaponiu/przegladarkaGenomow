from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from zprapp.models import Organizm, Chromosom
import json

def index(request):
    return render(request, 'zprapp/index.html')

def ajaxOrganizm(request):
    o = Organizm.objects.get( id = request.REQUEST['id']);
    print "ajaxOrganizm:",o;
    #response = JsonResponse(json.dumps(o));
    response = JsonResponse({'organizm': o.nazwa});
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