from django.urls import path
from .views import AtividadeAPIView, TipoAtividadeAPIViews, PublicacaoAPIViews, MidiaAPIViews, \
    DetailAtividade,  DetailTipoAtividade, RegionalAPIViews, DetailRegional, \
    DetailPublicacao, DetailMidia, RankingAPIViews, DetailRanking, ComentarioAPIViews,\
    DetailComentario,  PremioAPIViews, DetailPremio, InteracaoAPIViews, DetailInteracao, ViewPerfilAPIViews


urlpatterns = [
    path('atividades', AtividadeAPIView.as_view()),
    path('atividades/<int:pk>', DetailAtividade.as_view()),

    # path('cidade', CidadeAPIViews.as_view()),
    # path('cidade/<int:pk>', DetailCidade.as_view()),

    # path('estado', EstadoAPIViews.as_view()),
    # path('estado/<int:pk>', DetailEstado.as_view()),

    path('regional', RegionalAPIViews.as_view()),
    path('regional/<int:pk>', DetailRegional.as_view()),

    path('tipoAtividade', TipoAtividadeAPIViews.as_view()),
    path('tipoAtividade/<int:pk>', DetailTipoAtividade.as_view()),

    path('publicacao', PublicacaoAPIViews.as_view()),
    path('publicacao/<int:pk>', DetailPublicacao.as_view()),

    path('midia', MidiaAPIViews.as_view()),
    path('midia/<int:pk>', DetailMidia.as_view()),

    path('ranking', RankingAPIViews.as_view()),
    path('ranking/<int:pk>', DetailRanking.as_view()),

    path('comentario', ComentarioAPIViews.as_view()),
    path('comentario/<int:pk>', DetailComentario.as_view()),

    path('from', PremioAPIViews.as_view()),
    path('premio/<int:pk>', DetailPremio.as_view()),

    path('interacao', InteracaoAPIViews.as_view()),
    path('interacao/<int:pk>', DetailInteracao.as_view()),

    path('viewperfil', ViewPerfilAPIViews.as_view()),
]


