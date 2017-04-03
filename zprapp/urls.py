from django.conf.urls import patterns, url, include
from django.shortcuts import render_to_response
from zprapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    # url(r'organizmy', views.organizmy),
    url(r'ajax_orgs', views.ajaxOrganizmy),
    # url(r'chromosomy', views.chromosomy),
    url(r'ajax_chrmy', views.ajaxChromosomy),
    # url(r'scaffoldy', views.scaffoldy),
    url(r'ajax_scfldy', views.ajaxScaffoldy),
    # url(r'sekwencje', views.sekwencja),
    url(r'ajax_scs', views.ajaxSekwencja),
    url(r'ajax_markers', views.ajaxMarkers),
    url(r'test', views.test),
    url(r'ajax_post', views.ajaxPost),
    url(r'templates/(?P<template>[a-z]*\.html)', lambda request, template: render_to_response('zprapp/'+template)),
    url(r'ajax_newOrganism', views.ajaxNewOrganism),
    url(r'ajax_deleteOrganism', views.ajaxDeleteOrganism),
    url(r'ajax_seqSection', views.ajaxSeqSection),
    url(r'ajax_searchSeq', views.ajaxSearchSeq)
)