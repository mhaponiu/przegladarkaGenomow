from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from zprapp.models import Organizm, Chromosom

def index(request):
    return HttpResponse("Hello word")

def organizm(request, org_id):
    response = "Organizm o id: %s"
    #o = Organizm.objects.get(id = org_id)
    #o = get_object_or_404(Organizm, id = org_id)
    #return HttpResponse(o)
    organizm = Organizm.objects.get(id = org_id)
    context = {'organizm': organizm}
    return render(request, 'zprapp/index.html', context)

#todo get response
def odpowiedz(request, org_id):
    organizm = Organizm.objects.get(id = org_id)
    return HttpResponse(organizm.nazwa);