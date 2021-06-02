from rest_framework import viewsets

from .models import Atividade, TipoAtividade, Referencia, \
    Publicacao, Midia, Ranking, Comentario, Premio, Interacao


from .serializers import AtividadeSerializers, TipoAtividadeSerializers, \
    PublicacaoSerializers, MidiaSerializers, RankingSerializers, \
    ComentarioSerializers, PremioSerializers, InteracaoSerializers, ReferenciaSerializers


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializers


class ReferenciaViewSet(viewsets.ModelViewSet):
    queryset = Referencia.objects.all()
    serializer_class = ReferenciaSerializers


class TipoAtividadeViewSet(viewsets.ModelViewSet):
    queryset = TipoAtividade.objects.all()
    serializer_class = TipoAtividadeSerializers


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializers


class MidiaViewSet(viewsets.ModelViewSet):
    queryset = Midia.objects.all()
    serializer_class = MidiaSerializers


class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializers


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializers


class PremioViewSet(viewsets.ModelViewSet):
    queryset = Premio.objects.all()
    serializer_class = PremioSerializers


class InteracaoViewSet(viewsets.ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializers




