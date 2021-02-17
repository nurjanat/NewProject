from django.db import models
from django.contrib.auth.models import User




class Movies(models.Model):
    genre = (
        ('horror','horror'),
        ('classic','classic'),
        ('fantasy','fantasy'),
        ('distopia','distopia'),
        ('detectiv','detectiv'),
        ('crime','crime'),
        ('thriller','thriller'),

    )
    name = models.CharField(max_length=90)
    description = models.TextField()
    genre = models.CharField(max_length=90)
    video = models.FileField()
    poster = models.ImageField()




# Create your models here.
