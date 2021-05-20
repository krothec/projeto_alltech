# Generated by Django 3.2.1 on 2021-05-13 00:47

import core.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_midia_descricao_midia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midia',
            name='flag_foto_perfil',
            field=models.BooleanField(default=False, verbose_name='Foto Perfil'),
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateField(auto_now_add=True, verbose_name='Data Criação')),
                ('dt_alteracao', models.DateField(auto_now=True, verbose_name='Data Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cd_publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacao')),
                ('usuario_criacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ranking',
            },
        ),
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
                ('vigencia', models.DateTimeField(default=datetime.date.today)),
                ('data_premiacao', models.DateTimeField(default=datetime.date.today)),
                ('usuario_criacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prêmio',
                'verbose_name_plural': 'Prêmios',
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
                ('usuario_criacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
    ]
