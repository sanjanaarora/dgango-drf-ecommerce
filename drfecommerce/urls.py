"""drfecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from drfecommerce.apps.store import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(
            permission_classes=[]  # This endpoint is available for everyone
        ),
        name="schema",
    ),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
            permission_classes=[],  # This endpoint is available for everyone
        ),
        name="swagger",
    ),
    path(
        "api/docs/",
        SpectacularRedocView.as_view(
            url_name="schema",
            permission_classes=[],  # This endpoint is available for everyone
        ),
        name="redoc",
    ),
]
