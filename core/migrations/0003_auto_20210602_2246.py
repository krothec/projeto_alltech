# Generated by Django 3.2.1 on 2021-06-03 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_viewatividades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='cd_publicacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividade', to='core.publicacao'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='cd_tipo_atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividade', to='core.tipoatividade'),
        ),
    ]