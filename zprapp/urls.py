from django.conf.urls import patterns, url
from zprapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    #url(r'organizm/3/zprapp/ajax/$', views.odpowiedz),
    url(r'ajax_organizm', views.ajaxOrganizm),

    #nizej do pierwszych prob
    url(r'organizm/(?P<org_id>\d+)/$', views.organizm),
    url(r'ajax/$', views.odpowiedz),
)