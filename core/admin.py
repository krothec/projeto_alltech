from django.contrib import admin

from .models import Atividade, Estado, Cidade,\
    Regional, TipoAtividade, Publicacao, Midia, Ranking, \
    Comentario, Premio, Interacao

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome_atividade', 'descricao_atividade')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome_estado', 'sigla_estado')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_cidade', 'cd_estado')

@admin.register(Regional)
class RegionalAdmin(admin.ModelAdmin):
    list_display = ('nome_regional', 'cd_cidade')

@admin.register(TipoAtividade)
class TipoAtividadeAdmin(admin.ModelAdmin):
    list_display = ('tipo_atividade', 'pontos')

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'cd_tipo_atividade')

@admin.register(Midia)
class MidiaAdmin(admin.ModelAdmin):
    list_display = ('midia', 'cd_publicacao')

@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    display = ('cd_publicacao')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('cd_publicacao', 'comentario')

@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('nome_premio', 'descricao')

@admin.register(Interacao)
class Interacaodmin(admin.ModelAdmin):
    list_display = ('cd_publicacao', 'interacao')

