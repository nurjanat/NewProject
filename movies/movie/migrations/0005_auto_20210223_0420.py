# Generated by Django 3.1.6 on 2021-02-23 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20210219_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]