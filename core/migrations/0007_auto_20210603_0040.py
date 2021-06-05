# Generated by Django 3.2.1 on 2021-06-03 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_atividade_cd_tipo_atividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='interacao',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='midia',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='premio',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='referencia',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='regional',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
        migrations.AlterField(
            model_name='tipoatividade',
            name='dt_alteracao',
            field=models.DateField(null=True, verbose_name='Data Alteração'),
        ),
    ]