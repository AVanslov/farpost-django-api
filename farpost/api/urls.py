from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import AddViewSet

router = SimpleRouter()
router.register('adds', AddViewSet, basename='add')

urlpatterns = [
    path('', include(router.urls)),
]
