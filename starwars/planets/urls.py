from django.conf.urls import url, include
from rest_framework import routers

from starwars.planets.views import PlanetView

router = routers.DefaultRouter()
router.register(
    '',
    PlanetView,
    base_name='starwars-planets'
)

urlpatterns = [
    url(r'^', include(router.urls)),
]
