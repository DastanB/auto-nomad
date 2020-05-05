from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import permissions


api_url_patterns = [
    path("users/", include("nomad_auto_advert.users.urls", namespace="users")),
    path("microservices/", include("nomad_auto_advert.microservices.urls", namespace="microservcies")),
    path(r'advert/', include('nomad_auto_advert.advert.urls', namespace='advert')),
    path(r"cars/", include('nomad_auto_advert.cars.urls', namespace='cars')),
    path(r"characteristics/", include('nomad_auto_advert.characteristics.urls', namespace="characteristics")),
]

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("api/", include(api_url_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        from drf_yasg.views import get_schema_view
        from drf_yasg import openapi

        schema_view = get_schema_view(
            openapi.Info(
                title="Snippets API",
                default_version='v1',
                description="Test description",
                terms_of_service="https://www.google.com/policies/terms/",
                contact=openapi.Contact(email="contact@snippets.local"),
                license=openapi.License(name="BSD License"),
            ),
            public=True,
            permission_classes=(permissions.AllowAny,),
        )
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
        urlpatterns += [
            # Your stuff: custom urls includes go here
            url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                name='schema-json'),
            url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
            url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        ]
