import uuid
from django.db import models
from datetime import datetime

from django_db_views.db_view import DBView

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    dt_criacao = models.DateField('Data Criação', auto_now_add=True)
    dt_alteracao = models.DateField('Data Alteração', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    usuario_criacao = models.ForeignKey('users.NewUser', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class Regional(Base):
    nome_regional = models.CharField('Nome regional', max_length=100)

    class Meta:
        verbose_name = 'Regional'
        verbose_name_plural = 'Regionais'

    def __str__(self):
        return self.nome_regional


class TipoAtividade(Base):
    descricao_atividade = models.CharField('Tipo Atividade', max_length=100)
    pontos = models.IntegerField('Pontuação', blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo Atividade'

    def __str__(self):
        return self.tipo_atividade


class Publicacao(Base):
    localizacao = models.FloatField('Localização', max_length=10000)
    data_atividade = models.DateField('Data Atividade', auto_now_add=True)
    descricao = models.TextField('Descrição', max_length=500)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.descricao


class Atividade(Base):
    cd_publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    cd_tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.nome_atividade


class Midia(Base):
    cd_publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    midia = models.ImageField(upload_to=get_file_path, null=True)
    descricao_midia = models.CharField('Descrição', max_length=500, default='NULL')

    class Meta:
        verbose_name = 'Mídia'

    def __str__(self):
        return self.descricao_midia

class Ranking(Base):
    cd_publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ranking'

    def __int__(self):
        return self.cd_publicacao

class Comentario(Base):
    cd_publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    comentario = models.TextField('Comentário', max_length=500)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.comentario

class Premio(Base):
    nome_premio = models.CharField('Nome prêmio', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    midia = models.ImageField(upload_to=get_file_path, null=True)
    vigencia = models.DateTimeField(default=datetime.now)
    data_premiacao = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Prêmio'
        verbose_name_plural = 'Prêmios'

    def __str__(self):
        return self.descricao

class Interacao(Base):
    cd_publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Interação'
        verbose_name_plural = 'Interações'

    def __bool__(self):
        return self.interacao

class Referencia(Base):
    tipo_dado = models.CharField('Pontuação', max_length=100)
    nome_tabela = models.CharField('Nome tabela', max_length=100)
    nome_campo = models.CharField('Nome campo', max_length=100)
    valor = models.CharField('Valor', max_length=100)

    class Meta:
        verbose_name = 'Referência'
        verbose_name_plural = 'Referências'

    def __str__(self):
        return self.tipo_dado


class ViewAtividades(DBView):
    id_publicacao = models.ForeignKey(Publicacao, on_delete=models.DO_NOTHING)
    id_atividade = models.ForeignKey(Atividade, on_delete=models.DO_NOTHING)
    descricao_atividade = models.CharField(max_length=100)
    ativo = models.BooleanField('Ativo', default=True)

    view_definition = """
        select 
            publi.id as id_publicacao,
            atv.id as id_atividade,
            tipoatv.descricao_atividade as descricao_atividade
            from core_tipoatividade tipoatv
            left join core_atividade atv on tipoatv.id = atv.cd_tipo_atividade_id
            join core_publicacao publi on atv.cd_publicacao_id = publi.id 
            where publi.ativo = true
            and tipoatv.ativo = true
        """

    class Meta:
        managed = False
        db_table = 'viewAtividades'

