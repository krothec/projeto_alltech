# Generated by Django 3.2.1 on 2021-07-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210710_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='localizacao',
            field=models.FloatField(blank=True, max_length=10000, null=True, verbose_name='Localização'),
        ),
    ]