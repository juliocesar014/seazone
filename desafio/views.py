from rest_framework import viewsets
from desafio.models import Anuncio,Imovel,Reserva
from desafio.serializer import AnuncioSerializer,ImovelSerializer,ReservaSerializer

class ImoveisViewSet(viewsets.ModelViewSet):
    """ Exibindo todos Imóveis """
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    

class AnuncioViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os Anúncios """
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    
    
class ReservaViewSet(viewsets.ModelViewSet):
    """ Exibindo todas as Reservas """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer