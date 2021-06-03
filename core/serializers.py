from rest_framework import serializers

from .models import Atividade,  Regional, Referencia, \
    TipoAtividade, Publicacao, Midia, Ranking, Comentario, Premio, Interacao

from users.models import NewUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"


class AtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = "__all__"


class TipoAtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = "__all__"


class ReferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Referencia
        fields = "__all__"


class RegionalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = "__all__"


class PublicacaoSerializers(serializers.ModelSerializer):
    atividade = AtividadeSerializers(many=True, read_only=True)

    class Meta:
        model = Publicacao
        fields = "__all__"
        depth = 3


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



