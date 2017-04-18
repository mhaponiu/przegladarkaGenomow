from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from zprapp.views_rest import UserViewSet, GroupViewSet, OrganismViewSet\
    , ChromosomeViewSet, AnnotationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'organisms', OrganismViewSet)
router.register(r'chromosomes', ChromosomeViewSet)
router.register(r'annotations', AnnotationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zpr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('zprapp.urls')),
)



