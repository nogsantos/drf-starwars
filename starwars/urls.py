from django.urls import path, include
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .planets import urls as planets_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Star Wars Planets - API",
        default_version='v1',
    ),
    public=True,
)


urlpatterns = [
    path('planets/', include(planets_urls)),
    path('admin/', admin.site.urls),
    path('docs/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
