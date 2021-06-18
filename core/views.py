from rest_framework import generics, filters
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS,\
    IsAuthenticated, DjangoModelPermissions
import json
import requests

from .utils import get_client_ip

from .models import Atividade, TipoAtividade, Publicacao, Midia, \
    Ranking, Comentario, Premio, Interacao, Regional, Referencia

from users.models import NewUser

from .serializers import AtividadeSerializers, TipoAtividadeSerializers, PublicacaoSerializers, \
    MidiaSerializers, RankingSerializers, ComentarioSerializers, \
    PremioSerializers, InteracaoSerializers, RegionalSerializers, ReferenciaSerializers, \
    UserSerializers


class OwnerPermission(BasePermission):
    message = 'Ação restrita ao autor da postagem.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class TipoAtividadeAPIViews(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter, )
    queryset = TipoAtividade.objects.filter(ativo=True)
    serializer_class = TipoAtividadeSerializers


class DetailTipoAtividade(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAdminUser]
    queryset = TipoAtividade.objects.filter(ativo=True)
    serializer_class = TipoAtividadeSerializers


class UserAPIView(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    queryset = NewUser.objects.filter(is_active=True)
    serializer_class = UserSerializers


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    queryset = NewUser.objects.filter(is_active=True)
    serializer_class = UserSerializers


class AtividadeAPIView(generics.ListCreateAPIView):
    queryset = Atividade.objects.filter(ativo=True)
    serializer_class = AtividadeSerializers


class DetailAtividade(generics.RetrieveUpdateDestroyAPIView, OwnerPermission):
    # permission_classes = [OwnerPermission]
    queryset = Atividade.objects.filter(ativo=True)
    serializer_class = AtividadeSerializers


class ReferenciaAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    filter_backends = (filters.SearchFilter, )
    queryset = Referencia.objects.filter(ativo=True)
    serializer_class = ReferenciaSerializers


class DetailReferencia(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Referencia.objects.filter(ativo=True)
    serializer_class = ReferenciaSerializers



class RegionalAPIViews(generics.ListCreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    filter_backends = (filters.SearchFilter, )
    queryset = Regional.objects.filter(ativo=True)
    serializer_class = RegionalSerializers


class DetailRegional(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Regional.objects.filter(ativo=True)
    serializer_class = RegionalSerializers


class PublicacaoAPIViews(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter, )
    queryset = Publicacao.objects.filter(ativo=True)
    serializer_class = PublicacaoSerializers


class DetailPublicacao(generics.RetrieveUpdateDestroyAPIView, OwnerPermission):
    # permission_classes = [OwnerPermission]
    queryset = Publicacao.objects.filter(ativo=True)
    serializer_class = PublicacaoSerializers


class MidiaAPIViews(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter, )
    queryset = Midia.objects.filter(ativo=True)
    serializer_class = MidiaSerializers


class DetailMidia(generics.RetrieveUpdateDestroyAPIView, OwnerPermission):
    # permission_classes = [IsAuthenticated]
    permission_classes = [OwnerPermission, IsAuthenticated]
    queryset = Midia.objects.filter(ativo=True)
    serializer_class = MidiaSerializers


class RankingAPIViews(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter, )
    queryset = Ranking.objects.filter(ativo=True)
    serializer_class = RankingSerializers


class DetailRanking(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Ranking.objects.filter(ativo=True)
    serializer_class = RankingSerializers


class ComentarioAPIViews(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    queryset = Comentario.objects.filter(ativo=True)
    serializer_class = ComentarioSerializers


class DetailComentario(generics.RetrieveUpdateDestroyAPIView, OwnerPermission):
    # permission_classes = [OwnerPermission, IsAuthenticated]
    queryset = Comentario.objects.filter(ativo=True)
    serializer_class = ComentarioSerializers


class PremioAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Premio.objects.filter(ativo=True)
    serializer_class = PremioSerializers


class DetailPremio(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Premio.objects.filter(ativo=True)
    serializer_class = PremioSerializers


class InteracaoAPIViews(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    queryset = Interacao.objects.filter(ativo=True)
    serializer_class = InteracaoSerializers


class DetailInteracao(generics.RetrieveUpdateDestroyAPIView, OwnerPermission):
    # permission_classes = [IsAuthenticated, OwnerPermission]
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

