# Generated by Django 3.2.1 on 2021-06-03 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210602_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='cd_tipo_atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_atividade', to='core.tipoatividade'),
        ),
    ]
