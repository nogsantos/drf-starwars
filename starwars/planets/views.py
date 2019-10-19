from rest_framework import (
    viewsets,
    response,
    filters,
    status
)
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from . import (
    models,
    serializers
)


class PlanetsViewSet(viewsets.ModelViewSet):
    """
    # Planets

    - Adicionar um planeta (com nome, clima e terreno)
    - Listar planetas
    - Buscar por nome
    - Buscar por ID
    - Remover planeta
    """
    queryset = models.Planet.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    serializer_class = serializers.PlanetSerializer
    ordering = '-id'

    def get_queryset(self, *args, **kwargs):
        name = self.request.query_params.get("name", None)

        return models.Planet.objects.filter(name=name)
