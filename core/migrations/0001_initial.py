# Generated by Django 3.2.1 on 2021-05-24 15:32

import core.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome_premio', models.CharField(max_length=100, verbose_name='Nome prêmio')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('midia', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('vigencia', models.DateTimeField(default=datetime.datetime.now)),
                ('data_premiacao', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Prêmio',
                'verbose_name_plural': 'Prêmios',
            },
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('localizacao', models.FloatField(max_length=10000, verbose_name='Localização')),
                ('data_atividade', models.DateField(auto_now_add=True, verbose_name='Data Atividade')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
            },
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome_regional', models.CharField(max_length=100, verbose_name='Nome regional')),
            ],
            options={
                'verbose_name': 'Regional',
                'verbose_name_plural': 'Regionais',
            },
        ),
        migrations.CreateModel(
            name='TipoAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('descricao_atividade', models.CharField(max_length=100, verbose_name='Tipo Atividade')),
                ('pontos', models.IntegerField(blank=True, null=True, verbose_name='Pontuação')),
            ],
            options={
                'verbose_name': 'Tipo Atividade',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
            ],
            options={
                'verbose_name': 'Ranking',
            },
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('midia', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('descricao_midia', models.CharField(default='NULL', max_length=500, verbose_name='Descrição')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
            ],
            options={
                'verbose_name': 'Mídia',
            },
        ),
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
            ],
            options={
                'verbose_name': 'Interação',
                'verbose_name_plural': 'Interações',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('comentario', models.TextField(max_length=500, verbose_name='Comentário')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
                ('cd_tipo_atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoatividade')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
    ]
