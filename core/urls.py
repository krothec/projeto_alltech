from django.urls import path
from .views import AtividadeAPIView, TipoAtividadeAPIViews, PublicacaoAPIViews, MidiaAPIViews, \
    DetailAtividade,  DetailTipoAtividade, RegionalAPIViews, DetailRegional, \
    DetailPublicacao, DetailMidia, RankingAPIViews, DetailRanking, ComentarioAPIViews,\
    DetailComentario,  PremioAPIViews, DetailPremio, InteracaoAPIViews, DetailInteracao, ReferenciaAPIView,\
    DetailReferencia, UserAPIView, DetailUser, \
    IndexView


urlpatterns = [
    path('atividades', AtividadeAPIView.as_view()),
    path('atividades/<int:pk>', DetailAtividade.as_view()),

    path('referencia', ReferenciaAPIView.as_view()),
    path('referencia/<int:pk>', DetailReferencia.as_view()),

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

    path('premio', PremioAPIViews.as_view()),
    path('premio/<int:pk>', DetailPremio.as_view()),

    path('interacao', InteracaoAPIViews.as_view()),
    path('interacao/<int:pk>', DetailInteracao.as_view()),

    path('usuario', UserAPIView.as_view()),
    path('usuario/<int:pk>', DetailUser.as_view()),

    path('', IndexView.as_view(), name='index'),

]




