from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from starwars.planets.views import PlanetViewSet

router = routers.DefaultRouter()
router.register('', PlanetViewSet, base_name='planets')

urlpatterns = [
    path('', include(router.get_urls())),
]
