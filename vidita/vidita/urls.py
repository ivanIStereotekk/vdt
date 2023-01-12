from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="OpenAPI - Тестовой работы Гончарова Ивана",
        default_version='v1',
        description="Приложение для загрузки фотографий: telegram: @EwanPotterman",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ivan.stereotekk@gmail.com"),
        license=openapi.License(name="Global Communication license BSD "),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


openapi_patterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('authentication/', include('djoser.urls')),
    path('auth_token/', include('djoser.urls.authtoken')),
    path('jaysonweb_token/', include('djoser.urls.jwt'))
]

urlpatterns += openapi_patterns


from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings



if settings.DEBUG:
    """That's how we do static files handling"""
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

