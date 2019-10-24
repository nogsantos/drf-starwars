from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from . import models


class PlanetsViewSet(viewsets.ModelViewSet):
    """
    # Planets

    - Add a new planet by name, climate and terrain
    - List planets
    - Search by name
    - Search by ID
    - Remove a planet
    """
    queryset = models.Planet.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    serializer_class = serializers.PlanetSerializer
    ordering = '-id'

    def get_queryset(self, *args, **kwargs):
        name = self.request.query_params.get('name', None)

        return models.Planet.objects.filter(name=name)
