"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_TITLE = "Rent A Car"
API_DESCRIPTION = "Araba kiralamak içi bir Wb APİ'si"

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="API Documentation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("", include("users.api.urls"), name="users"),
    path("contactmessage/", include("contactmessages.api.urls"), name="contactmessages"),
    path("files/", include("imagess.api.urls"), name="imagess"),
    path("car/", include("cars.api.urls"), name="cars"),
    path("reservations/", include("reservations.api.urls"), name="reservations"),
    path("excel/", include("excel.urls"), name="excel"),
    path("docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    #path("schema/", schema_view),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)