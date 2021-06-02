from django.shortcuts import render
from rest_framework import generics, filters
from django import forms

from .models import Atividade, TipoAtividade, Publicacao, Midia, \
    Ranking, Comentario, Premio, Interacao, Regional, Referencia, \
    ViewPerfil, ViewComentario, ViewInteracao, ViewAtividades, ViewPublicacao

from .serializers import AtividadeSerializers, TipoAtividadeSerializers, PublicacaoSerializers, \
    MidiaSerializers, RankingSerializers, ComentarioSerializers, \
    PremioSerializers, InteracaoSerializers, RegionalSerializers, \
    ViewPerfilSerializers, ViewComentarioSerializers, ViewInteracaoSerializers, \
    ViewAtividadesSerializers, ViewPublicacaoSerializers, ReferenciaSerializers


class AtividadeAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, )
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


class TipoAtividadeAPIViews(generics.ListCreateAPIView):
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


class ViewPerfilAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = ViewPerfil.objects.all()
    serializer_class = ViewPerfilSerializers


class ViewComentarioAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = ViewComentario.objects.all()
    serializer_class = ViewComentarioSerializers


class ViewInteracaoAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = ViewInteracao.objects.all()
    serializer_class = ViewInteracaoSerializers


class ViewAtividadesAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = ViewAtividades.objects.all()
    serializer_class = ViewAtividadesSerializers


class ViewPublicacaoAPIViews(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = ViewPublicacao.objects.all()
    serializer_class = ViewPublicacaoSerializers