from rest_framework import generics, filters
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from django.views.generic import View, TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import requests

from .utils import get_client_data, get_random_ip, get_client_ip

from .models import Atividade, TipoAtividade, Publicacao, Midia, \
    Ranking, Comentario, Premio, Interacao, Regional, Referencia

from users.models import NewUser

from .serializers import AtividadeSerializers, TipoAtividadeSerializers, PublicacaoSerializers, \
    MidiaSerializers, RankingSerializers, ComentarioSerializers, \
    PremioSerializers, InteracaoSerializers, RegionalSerializers, ReferenciaSerializers, \
    UserSerializers


class UserAPIView(generics.ListCreateAPIView):
    queryset = NewUser.objects.filter(is_active=True)
    serializer_class = UserSerializers


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.filter(is_active=True)
    serializer_class = UserSerializers


class AtividadeAPIView(generics.ListCreateAPIView):
    queryset = Atividade.objects.filter(ativo=True)
    serializer_class = AtividadeSerializers


class ReferenciaAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Referencia.objects.filter(ativo=True)
    serializer_class = ReferenciaSerializers


class DetailReferencia(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referencia.objects.filter(ativo=True)
    serializer_class = ReferenciaSerializers


class DetailAtividade(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atividade.objects.filter(ativo=True)
    serializer_class = AtividadeSerializers


class RegionalAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Regional.objects.filter(ativo=True)
    serializer_class = RegionalSerializers


class DetailRegional(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regional.objects.filter(ativo=True)
    serializer_class = RegionalSerializers


class TipoAtividadeAPIViews(generics.ListCreateAPIView, APIView):
    filter_backends = (filters.SearchFilter, )
    queryset = TipoAtividade.objects.filter(ativo=True)
    serializer_class = TipoAtividadeSerializers


class DetailTipoAtividade(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoAtividade.objects.filter(ativo=True)
    serializer_class = TipoAtividadeSerializers


class PublicacaoAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Publicacao.objects.filter(ativo=True)
    serializer_class = PublicacaoSerializers


class DetailPublicacao(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacao.objects.filter(ativo=True)
    serializer_class = PublicacaoSerializers


class MidiaAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Midia.objects.filter(ativo=True)
    serializer_class = MidiaSerializers


class DetailMidia(generics.RetrieveUpdateDestroyAPIView):
    queryset = Midia.objects.filter(ativo=True)
    serializer_class = MidiaSerializers


class RankingAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
    queryset = Ranking.objects.filter(ativo=True)
    serializer_class = RankingSerializers


class DetailRanking(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ranking.objects.filter(ativo=True)
    serializer_class = RankingSerializers


class ComentarioAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Comentario.objects.filter(ativo=True)
    serializer_class = ComentarioSerializers


class DetailComentario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.filter(ativo=True)
    serializer_class = ComentarioSerializers


class PremioAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Premio.objects.filter(ativo=True)
    serializer_class = PremioSerializers


class DetailPremio(generics.RetrieveUpdateDestroyAPIView):
    queryset = Premio.objects.filter(ativo=True)
    serializer_class = PremioSerializers


class InteracaoAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Interacao.objects.filter(ativo=True)
    serializer_class = InteracaoSerializers


class DetailInteracao(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interacao.objects.filter(ativo=True)
    serializer_class = InteracaoSerializers


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user_ip = get_client_ip(request)
        url = f'http://api.ipstack.com/{user_ip}?access_key=e6d04720017effceba16529a86a93c2c'
        headers = {'Content-type': 'application/json'}
        response = requests.get(url, headers)
        parsed_json = (json.loads(response.text))

        context = {
            'parsed_json': parsed_json
        }

        return render(request, 'index.html', context)

