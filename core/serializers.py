from rest_framework import serializers

from .models import Atividade,  Regional, Referencia, \
    TipoAtividade, Publicacao, Midia, Ranking, Comentario, Premio, Interacao

from users.models import NewUser


class TipoAtividadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoAtividade
        fields = "__all__"
        depth = 4


class AtividadeSerializers(serializers.ModelSerializer):
    tipo_atividade = TipoAtividadeSerializers(many=True, read_only=True)

    class Meta:
        model = Atividade
        fields = "__all__"
        depth = 4


class ReferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Referencia
        fields = "__all__"
        depth = 4


class RegionalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = "__all__"
        depth = 4


class MidiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Midia
        fields = "__all__"
        depth = 4


class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
        depth = 4


class InteracaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interacao
        fields = "__all__"
        depth = 4


class PublicacaoSerializers(serializers.ModelSerializer):
    atividade = AtividadeSerializers(many=True, read_only=True)
    midia = MidiaSerializers(many=True, read_only=True)
    comentario = ComentarioSerializers(many=True, read_only=True)
    interacao = InteracaoSerializers(many=True, read_only=True)

    class Meta:
        model = Publicacao
        fields = "__all__"
        depth = 4


class UserSerializers(serializers.ModelSerializer):
    publicacao = PublicacaoSerializers(many=True, read_only=True)

    class Meta:
        model = NewUser
        fields = "__all__"
        depth = 4


class RankingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = "__all__"
        depth = 4


class PremioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Premio
        fields = "__all__"
        depth = 4






