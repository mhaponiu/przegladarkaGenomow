from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework_extensions.routers import ExtendedDefaultRouter
from zprapp.views_rest import *

# router = routers.DefaultRouter()
# szczegoly o zagniezdzonych widokach http://chibisov.github.io/drf-extensions/docs/#nested-routes
router = ExtendedDefaultRouter()

###### bezposrednie api ######
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'annotation_types', AnnotationTypeViewSet)
router.register(r'aggregations', PaginatedAggregationViewSet)

router.register(r'chromosomes', ChromosomeViewSet)\
      .register(r'annotations', AnnotationViewSet, base_name='chromosome-annotations',
                                               parents_query_lookups=['chromosome'])

router.register(r'annotations', PaginatedAnnotationViewSet)\
      .register(r'aggregations', PaginatedAnnotationAggregationViewSet, base_name='annotation-aggreations',
                                                    parents_query_lookups=['aggregated_by__annotation_master'])


###### posrednie api od organizmu ######

chromosome_routes = router.register(r'organisms', OrganismViewSet, base_name='organism')\
                          .register(r'chromosomes', ChromosomeViewSet, base_name='organism-chromosomes',
                                             parents_query_lookups=['organism'])

chromosome_routes.register(r'annotations', AnnotationViewSet, base_name='organism-chromosome-annotations',
                                               parents_query_lookups=['chromosome__organism', 'chromosome'])\
                 .register(r'aggregations', AnnotationAggregationViewSet, base_name='organism-chromosome-annotation-aggreations',
                                                    parents_query_lookups=['chromosome__organism', 'chromosome', 'aggregated_by__annotation_master'])
chromosome_routes.register(r'paginated_annotations', PaginatedAnnotationViewSet, base_name='organism-chromosome-paginated_annotations',
                                               parents_query_lookups=['chromosome__organism', 'chromosome'])\
                 .register(r'aggregations', PaginatedAnnotationAggregationViewSet, base_name='organism-chromosome-paginated_annotations-paginated_aggregations',
                                                    parents_query_lookups=['chromosome__organism', 'chromosome', 'aggregated_by__annotation_master'])
chromosome_routes.register(r'annotation_types', AnnotationTypeViewSet, base_name='organism-chromosome-annotation_types',
                                               parents_query_lookups=['annotation__chromosome__organism', 'annotation__chromosome'])


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

    # url(r'^api/annotations/$', AnnotationList.as_view()),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('zprapp.urls')),
)



