
from django.contrib import admin
from django.urls import path, include
from desafio.views import AnuncioViewSet,ImoveisViewSet,ReservaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('imoveis',ImoveisViewSet, basename='Imóveis')
router.register('anuncios',AnuncioViewSet, basename='Anúncios')
router.register('reservas',ReservaViewSet, basename='Reservas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
