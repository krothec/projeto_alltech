from rest_framework import serializers

from .models import Atividade,  Regional, \
    TipoAtividade, Publicacao, Midia, Ranking, Comentario, Premio, Interacao, \
    ViewPerfil, ViewComentario, ViewInteracao, ViewAtividades, ViewPublicacao


class AtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = "__all__"


# class CidadeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Cidade
#         fields = "__all__"


# class EstadoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Estado
#         fields = "__all__"


class RegionalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = "__all__"


class TipoAtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = "__all__"


class PublicacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = "__all__"


class MidiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Midia
        fields = "__all__"


class RankingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = "__all__"


class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


class PremioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Premio
        fields = "__all__"


class InteracaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interacao
        fields = "__all__"


class ViewPerfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewPerfil
        fields = "__all__"


class ViewComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewComentario
        fields = "__all__"


class ViewInteracaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewInteracao
        fields = "__all__"


class ViewAtividadesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewAtividades
        fields = "__all__"


class ViewPublicacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViewPublicacao
        fields = "__all__"