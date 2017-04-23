from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework_extensions.routers import ExtendedDefaultRouter
from zprapp.views_rest import *

# router = routers.DefaultRouter()
# szczegoly o zagniezdzonych widokach http://chibisov.github.io/drf-extensions/docs/#nested-routes
router = ExtendedDefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'annotation_types', AnnotationTypeViewSet)
router.register(r'organisms', OrganismViewSet)
# router.register(r'annotations', PaginatedAnnotationViewSet)
organism_routes = router.register(r'organisms', OrganismViewSet, base_name='organism')
chromosome_routes = organism_routes.register(r'chromosomes', ChromosomeViewSet, base_name='organism-chromosomes',
                                             parents_query_lookups=['organism'])

annotation_routes = chromosome_routes.register(r'annotations', AnnotationViewSet, base_name='organism-chromosome-annotations',
                                               parents_query_lookups=['chromosome__organism', 'chromosome'])
paginated_annotation_routes = chromosome_routes.register(r'paginated_annotations', PaginatedAnnotationViewSet, base_name='organism-chromosome-paginated_annotations',
                                               parents_query_lookups=['chromosome__organism', 'chromosome'])
chromosome_annotation_types_routes = chromosome_routes.register(r'annotation_types', AnnotationTypeViewSet, base_name='organism-chromosome-annotation_types',
                                               parents_query_lookups=['annotation__chromosome__organism', 'annotation__chromosome'])


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

    # url(r'^api/annotations/$', AnnotationList.as_view()),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('zprapp.urls')),
)



