from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnderecoViewSet

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewSet,)

urlpatterns = [
    path('', include(router.urls)),
]