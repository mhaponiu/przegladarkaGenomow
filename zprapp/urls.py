from django.conf.urls import patterns, url
from zprapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'organizmy', views.organizmy),
    url(r'organizm/chromosomy', views.chromosomy),
    url(r'markery', views.markery),
    #url(r'organizm/3/zprapp/ajax/$', views.odpowiedz),
    url(r'ajax_organizm', views.ajaxOrganizm),
    url(r'ajax_wszystkieOrganizmy', views.ajaxOrganizmy),
    url(r'ajax_nowyOrganizm', views.ajaxNowyOrganizm),
    url(r'ajax_usunOrganizm', views.ajaxUsunOrganizm),
    url(r'ajax_edytujOrganizm', views.ajaxEdytujOrganizm),

    url(r'ajax_chromosomy', views.ajaxChromosomy),
    url(r'ajax_jedenchromosom', views.ajaxChromosom),
    url(r'ajax_usunChromosom', views.ajaxUsunChromosom),
    url(r'ajax_nowyChromosom', views.ajaxNowyChromosom),
    url(r'ajax_edytujChromosom', views.ajaxEdytujChromosom),

    url(r'ajax_wszystkieMarkery', views.ajaxMarkery),
    url(r'ajax_nowyMarker', views.ajaxNowyMarker),
    url(r'ajax_usunMarker', views.ajaxUsunMarker),
    url(r'ajax_edytujMarker', views.ajaxEdytujMarker),


    #nizej do pierwszych prob
    url(r'ajax/$', views.odpowiedz),
)