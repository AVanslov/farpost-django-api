from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import AddViewSet

router = SimpleRouter()
router.register('adds', AddViewSet, basename='add')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
