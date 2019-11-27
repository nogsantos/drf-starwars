from django.contrib import admin

from starwars.planets.models import Planet, Film

admin.site.register(Planet)
admin.site.register(Film)
