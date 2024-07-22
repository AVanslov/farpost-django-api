from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import AddViewSet

router = SimpleRouter()
router.register('adds', AddViewSet, basename='add')

urlpatterns = [
    path('', include(router.urls)),
]
