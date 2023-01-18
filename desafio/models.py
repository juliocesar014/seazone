from django.db import models

# Create your models here.

class Imovel(models.Model):
    limite_hospedes = models.CharField(help_text="Ex.: Máximo 05 hóspedes", verbose_name=u"Limite de Hóspedes", max_length=25)
    qtd_banheiros = models.CharField(help_text="Ex.: 02 Banheiros", verbose_name=u"Quantidade de Banheiros", max_length=25)
    aceita_animal = models.BooleanField(default=True)
    valor_limpeza = models.CharField(help_text="Ex.: R$250,00", verbose_name=u"Valor da Limpeza", max_length=25)
    data_ativacao = models.DateField(verbose_name=u"Data da ativação")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    
    def __int__(self):
        return self.id_imovel
    
    
    
class Anuncio(models.Model):
    
    imovel = models.ForeignKey(
        'Imovel',
        on_delete=models.CASCADE,
    )
    
    nome_plataforma = models.CharField(help_text="Ex.: AirBNB", verbose_name=u"Nome da plataforma de anúncio" , max_length=100)
    taxa_plataforma = models.CharField(help_text="Ex.: R$100,00", verbose_name=u"Taxa da Plataforma de anúncio", max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        return self.id_anuncio
    
    
    
class Reserva(models.Model):
    
    anuncio = models.ForeignKey(
        'Anuncio',
        on_delete=models.CASCADE,
    )
    
    data_checkin = models.DateTimeField(help_text="Momento em que inicia o checkIN", verbose_name=u"Check-in inicia em")
    data_checkout = models.DateTimeField(help_text="Momento em que ocorre o checkOUT", verbose_name=u"Check-out ocorre em")
    preco_total = models.CharField(help_text="Ex.: R$1.000,00", verbose_name=u"Valor total da reserva", max_length=100)
    comentario = models.TextField(max_length=400, help_text="Incluir comentários sobre a reserva", verbose_name=u"Comentário da reserva")
    numero_hospedes = models.BigIntegerField(help_text="Ex.: 5", verbose_name=u"Quantidade de hóspede da reserva")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        return self.id_reserva