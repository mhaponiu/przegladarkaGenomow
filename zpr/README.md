## API
REST FRAMEWORK **users**  
REST FRAMEWORK **groups**  
REST FRAMEWORK **annotation_types**  
REST FRAMEWORK **organisms**

GET r'^api/', router.urls  
GET r'^api/chromosomes/$'  
GET r'^api/chromosomes/(?P<pk>[0-9]+)/$'  
POST z danymi id=[1,2,3] r'^api/annotations/$'  
http --json POST localhost:8000/api/annotations/ "id=[7920,7921,7922]"  
