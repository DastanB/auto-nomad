from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_url_patterns = [
    path("users/", include("nomad_auto_advert.users.urls", namespace="users")),
    path("microservices/", include("nomad_auto_advert.microservices.urls", namespace="microservices")),
    path('adverts/', include('nomad_auto_advert.advert.urls', namespace='adverts')),
    path("cars/", include('nomad_auto_advert.cars.urls', namespace='cars')),
    path("filters/", include('nomad_auto_advert.filters.urls', namespace="filters")),
    path('geo/', include('nomad_auto_advert.geo.urls', namespace='geo')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="ADVERTS API",
        default_version='v1',
        description="Yare yare daze",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("api/", include(api_url_patterns)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

