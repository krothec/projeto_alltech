# from rest_framework import viewsets
#
# from .models import Atividade, TipoAtividade, \
#     Publicacao, Midia, Ranking, Comentario, Premio, Interacao, \
#     ViewPerfil, ViewInteracao, ViewAtividades, ViewPublicacao, ViewComentario
#
#
# from .serializers import AtividadeSerializers, TipoAtividadeSerializers, \
#     PublicacaoSerializers, MidiaSerializers, RankingSerializers, \
#     ComentarioSerializers, PremioSerializers, InteracaoSerializers, \
#     ViewPerfilSerializers, ViewComentarioSerializers, ViewInteracaoSerializers, \
#     ViewPublicacaoSerializers, ViewAtividadesSerializers
#
#
# class AtividadeViewSet(viewsets.ModelViewSet):
#     queryset = Atividade.objects.all()
#     serializer_class = AtividadeSerializers
#
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
#
# class InteracaoViewSet(viewsets.ModelViewSet):
#     queryset = Interacao.objects.all()
#     serializer_class = InteracaoSerializers
#
#
# class ViewPerfilViewSet(viewsets.ModelViewSet):
#     queryset = ViewPerfil.objects.all()
#     serializer_class = ViewPerfilSerializers
#
#
# class ViewInteracaoViewSet(viewsets.ModelViewSet):
#     queryset = ViewInteracao.objects.all()
#     serializer_class = ViewInteracaoSerializers
#
#
# class ViewAtividadesViewSet(viewsets.ModelViewSet):
#     queryset = ViewAtividades.objects.all()
#     serializer_class = ViewAtividadesSerializers
#
#
# class ViewPublicacaoViewSet(viewsets.ModelViewSet):
#     queryset = ViewPublicacao.objects.all()
#     serializer_class = ViewPublicacaoSerializers
#
#
# class ViewComentarioViewSet(viewsets.ModelViewSet):
#     queryset = ViewComentario.objects.all()
#     serializer_class = ViewComentarioSerializers
#
