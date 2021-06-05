# Generated by Django 3.2.1 on 2021-06-05 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_alter_comentario_usuario_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
