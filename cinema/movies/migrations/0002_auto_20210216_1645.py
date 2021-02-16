# Generated by Django 3.1.6 on 2021-02-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='poster',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]