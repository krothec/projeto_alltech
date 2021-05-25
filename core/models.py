import uuid
from django.db import models
from datetime import datetime
from dbview.models import DbView

from stdimage.models import StdImageField

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

# class Estado(Base):
#     nome_estado = models.CharField('Nome estado', max_length=100)
#     sigla_estado = models.CharField('Sigla', max_length=2)
#
#     class Meta:
#         verbose_name = 'Estado'
#         verbose_name_plural = 'Estados'
#
#     def __str__(self):
#         return self.nome_estado
#
# class Cidade(Base):
#     nome_cidade = models.CharField('Nome Cidade', max_length=100)
#     cd_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'Cidade'
#         verbose_name_plural = 'Cidades'
#
#     def __str__(self):
#         return self.nome_cidade

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
    midia = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
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
    midia = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
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


class ViewPerfil(DbView):
    id = models.OneToOneField('users.NewUser', on_delete=models.DO_NOTHING, primary_key=True)
    primeiro_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    biografia = models.TextField(max_length=200)
    foto = models.CharField(max_length=100)
    id_regional = models.ForeignKey(Regional, on_delete=models.DO_NOTHING)
    nome_regional = models.CharField(max_length=100)

    @classmethod
    def get_view_str(cls):
        return """
             CREATE VIEW viewPerfil AS
             select 
                u.id as id_usuario,
                u.first_name as primeiro_nome,
                u.last_name as sobrenome,
                u.about as biografia,
                u.photo as foto,
                regional.id as id_regional, 
                regional.nome_regional as nome_regional
                from users_newuser as u 
                join core_regional as regional on regional.id = u.cd_regional_id
                where u.is_active = true
             """

class ViewComentario(DbView):
    id_publicacao = models.ForeignKey(Publicacao, on_delete=models.DO_NOTHING)
    id_comentario = models.ForeignKey(Comentario, on_delete=models.DO_NOTHING)
    id_usuario_comentario = models.ForeignKey('users.NewUser', on_delete=models.DO_NOTHING)
    primeiro_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    comentario = models.TextField(max_length=500)
    id_regional = models.ForeignKey(Regional, on_delete=models.DO_NOTHING)
    nome_regional = models.CharField(max_length=100)

    @classmethod
    def get_view_str(cls):
        return """
             create view viewComentario as
                select 
                publi.id as id_publicacao,
                coment.id as id_comentario,
                coment.usuario_criacao_id as id_usuario_comentario,
                users.first_name as primeiro_nome,
                users.last_name as sobrenome,
                users.photo as foto,
                coment.comentario as comentario,
                reg.id as id_regional,
                reg.nome_regional as nome_regional
                from core_publicacao publi
                join core_comentario as coment on coment.cd_publicacao_id = publi.id
                join users_newuser users on users.id = coment.usuario_criacao_id 
                join core_regional reg on reg.id = users.cd_regional_id 
                where publi.ativo = true 
                and coment.ativo = true 
             """
