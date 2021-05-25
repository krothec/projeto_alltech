from rest_framework import viewsets

from .models import Atividade, TipoAtividade, \
    Publicacao, Midia, Ranking, Comentario, Premio, Interacao, \
    ViewPerfil


from .serializers import AtividadeSerializers, TipoAtividadeSerializers, \
    PublicacaoSerializers, MidiaSerializers, RankingSerializers, \
    ComentarioSerializers, PremioSerializers, InteracaoSerializers, \
    ViewPerfilSerializers, ViewComentarioSerializers


# class AtividadeViewSet(viewsets.ModelViewSet):
#     queryset = Atividade.objects.all()
#     serializer_class = AtividadeSerializers
#
#
# # class CidadeViewSet(viewsets.ModelViewSet):
# #     queryset = Cidade.objects.all()
# #     serializer_class = CidadeSerializers
# #
# #
# # class EstadoViewSet(viewsets.ModelViewSet):
# #     queryset = Estado.objects.all()
# #     serializer_class = EstadoSerializers
# #
# #
# # class RegionalViewSet(viewsets.ModelViewSet):
# #     queryset = Regional.objects.all()
# #     serializer_class = RegionalSerializers
#
# class TipoAtividadeViewSet(viewsets.ModelViewSet):
#     queryset = TipoAtividade.objects.all()
#     serializer_class = TipoAtividadeSerializers
#
#
# class PublicacaoViewSet(viewsets.ModelViewSet):
#     queryset = Publicacao.objects.all()
#     serializer_class = PublicacaoSerializers
#
#
# class MidiaViewSet(viewsets.ModelViewSet):
#     queryset = Midia.objects.all()
#     serializer_class = MidiaSerializers
#
#
# class RankingViewSet(viewsets.ModelViewSet):
#     queryset = Ranking.objects.all()
#     serializer_class = RankingSerializers
#
#
# class ComentarioViewSet(viewsets.ModelViewSet):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializers
#
#
# class PremioViewSet(viewsets.ModelViewSet):
#     queryset = Premio.objects.all()
#     serializer_class = PremioSerializers
#
# class InteracaoViewSet(viewsets.ModelViewSet):
#     queryset = Interacao.objects.all()
#     serializer_class = InteracaoSerializers
#
# class ViewPerfilViewSet(viewsets.ModelViewSet):
#     queryset = Interacao.objects.all()
#     serializer_class = ViewPerfilSerializers
