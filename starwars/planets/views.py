from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from starwars.planets.helpers import GetFilmByPlanet
from starwars.planets.models import Planet
from starwars.planets.serializers import PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    """
    # Planets

    - Add a new planet
    - List planets
    - Search by name
    - Search by ID
    - Remove a planet
    """
    queryset = Planet.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    serializer_class = PlanetSerializer

    def get_queryset(self, *args, **kwargs):
        name = self.request.query_params.get('name', None)
        pk = self.request.query_params.get('id', None)

        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        if pk:
            self.queryset = self.queryset.filter(pk=pk)

        return self.queryset

    def create(self, request, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        res = GetFilmByPlanet(instance)
        res.search()

        return response.Response(serializer.data, status.HTTP_200_OK)
