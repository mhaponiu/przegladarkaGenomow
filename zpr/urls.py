from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.models import User, Group
from rest_framework import routers, viewsets

from serializers import UserSerializer, GroupSerializer

from rest_framework.schemas import get_schema_view

# ViewSets define the view behavior.
from views import UserViewSet, GroupViewSet
from zprapp.views import OrganismViewSet, ChromosomeViewSet, ScaffoldViewSet, SequenceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

router.register(r'organisms', OrganismViewSet)
router.register(r'chromosomes', ChromosomeViewSet)
router.register(r'scaffolds', ScaffoldViewSet)
router.register(r'sequences', SequenceViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('zprapp.urls')),
    url(r'^schema/$', get_schema_view(title='PrzegladarkaGenomow API')),
)



