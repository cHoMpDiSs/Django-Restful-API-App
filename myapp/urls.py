from django.urls import include, path
from rest_framework import routers, viewsets
from rest_framework import renderers
from .views import *

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter( trailing_slash=False)


router.register(r'api/comics', ComicViewSet) 
router.register(r'api/publishers', PublisherViewSet) 
router.register(r'api/superheros', SuperheroViewSet)
router.register(r'api/toys', ToysViewSet)  

urlpatterns = [
  
    
    path('', home, name='home'),
    path('thankyou', thankyou, name='thankyou'),
    path('api', include(router.urls)),
    path('/api/comics',ComicApiView.as_view()),
    path('/api/comics/<int:comic_id>', ComicApiView.as_view()),
    path('/api/publishers',PublisherApiView.as_view()),
    path('/api/publishers/<int:publisher_id>', PublisherApiView.as_view()),
    path('/api/superheros',SuperheroApiView.as_view()),
    path('/api/superheros/<int:superhero_id>', SuperheroApiView.as_view()),
    path('/api/toys',ToysApiView.as_view()),
    path('/api/toys/<int:toy_id>', ToysApiView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls

