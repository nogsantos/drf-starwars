from django.urls import path, include
from django.contrib import admin

from .planets import urls as planets_urls

urlpatterns = [
    path('planets/', include(planets_urls)),
    path('admin/', admin.site.urls),
]
