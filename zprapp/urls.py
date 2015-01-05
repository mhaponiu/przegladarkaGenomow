from django.conf.urls import patterns, url
from zprapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'organizm/chromosomy', views.chromosomy),
    url(r'markery', views.markery),
    #url(r'organizm/3/zprapp/ajax/$', views.odpowiedz),
    url(r'ajax_organizm', views.ajaxOrganizm),
    url(r'ajax_nowyOrganizm', views.ajaxNowyOrganizm),
    url(r'ajax_usunOrganizm', views.ajaxUsunOrganizm),
    url(r'ajax_edytujOrganizm', views.ajaxEdytujOrganizm),

    url(r'ajax_chromosom', views.ajaxChromosom),

    #nizej do pierwszych prob
    url(r'organizm/(?P<org_id>\d+)/$', views.organizm),
    url(r'ajax/$', views.odpowiedz),
)