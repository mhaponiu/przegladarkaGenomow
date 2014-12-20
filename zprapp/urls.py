from django.conf.urls import patterns, url
from zprapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'organizm/(?P<org_id>\d+)/$', views.organizm),
    url(r'ajax/(?P<org_id>\d+)/$', views.odpowiedz),
)