from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    '',
    views.PlanetsViewSet,
    base_name='starwars-planets'
)

urlpatterns = [
    url(r'^', include(router.urls)),
]
