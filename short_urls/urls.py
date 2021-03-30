from django.urls import path, include
from rest_framework import routers

from .views import ShortUrlViewSet

app_name = 'short_urls'
router = routers.DefaultRouter()
router.register(r'short', ShortUrlViewSet, 'short')
urlpatterns = [
    path('', include(router.urls)),
]
