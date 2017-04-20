from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from zprapp.views_rest import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'annotation_types', AnnotationTypeViewSet)
router.register(r'organisms', OrganismViewSet)
# router.register(r'chromosomes', ChromosomeSet)
# router.register(r'annotations', AnnotationList)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zpr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/chromosomes/$', ChromosomeList.as_view()),
    url(r'^api/chromosomes/(?P<pk>[0-9]+)/$', ChromosomeDetail.as_view()),
    url(r'^api/annotations/$', AnnotationList.as_view()),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('zprapp.urls')),
)



