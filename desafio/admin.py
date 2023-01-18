from django.contrib import admin
from desafio.models import Anuncio,Imovel,Reserva

# Register your models here.
class Imoveis(admin.ModelAdmin):
    list_display = ('id','limite_hospedes','qtd_banheiros','aceita_animal','valor_limpeza','data_ativacao','criado_em','atualizado_em')
    list_display_links = ('id','limite_hospedes','qtd_banheiros','aceita_animal','valor_limpeza','data_ativacao')
    search_fields = ('id',)
    list_per_page = 20
    
    
admin.site.register(Imovel, Imoveis)



class Anuncios(admin.ModelAdmin):
    list_display = ('id','imovel','nome_plataforma','taxa_plataforma','criado_em','atualizado_em')
    list_display_links = ('id','imovel','nome_plataforma','taxa_plataforma')
    search_fields = ('id',)
    list_per_page = 20
    
    
admin.site.register(Anuncio,Anuncios)



class Reservas(admin.ModelAdmin):
    list_display = ('id', 'anuncio','data_checkin','data_checkout','preco_total','comentario','numero_hospedes','criado_em','atualizado_em' )
    list_display_links = ('id','anuncio','data_checkin','data_checkout','preco_total','comentario','numero_hospedes')
    search_fields = ('id',)
    list_per_page = 20
    
    
admin.site.register(Reserva,Reservas)