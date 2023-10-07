from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_api.views import DataFileViewSet

router = DefaultRouter()
router.register(r'files', DataFileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]