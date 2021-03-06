# Generated by Django 3.1.6 on 2021-02-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('horror', 'horror'), ('classic', 'classic'), ('fantasy', 'fantasy'), ('distopia', 'distopia'), ('detectiv', 'detectiv'), ('crime', 'crime'), ('thriller', 'thriller'), ('drama', 'drama')], max_length=90),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(),
        ),
    ]
