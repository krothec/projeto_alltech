from rest_framework import serializers

from .models import Atividade, Cidade, Estado, Regional, \
    TipoAtividade, Publicacao, Midia, Ranking, Comentario, Premio, Interacao


class AtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = "__all__"


class CidadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = "__all__"


class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"


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