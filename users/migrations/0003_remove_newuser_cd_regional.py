# Generated by Django 3.2.1 on 2021-05-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_cd_regional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='cd_regional',
        ),
    ]
