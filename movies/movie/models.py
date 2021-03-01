from django.db import models
from django.contrib.auth.models import User
from datetime import date




class Movies(models.Model):
    genre = (
        ('horror','horror'),
        ('classic','classic'),
        ('fantasy','fantasy'),
        ('distopia','distopia'),
        ('detectiv','detectiv'),
        ('crime','crime'),
        ('thriller','thriller'),
        ('drama','drama'),

    )

    name = models.CharField(max_length=90)
    description = models.TextField()
    genre = models.CharField(max_length=90,choices=genre)
    video = models.FileField()
    poster = models.ImageField()
    year = models.IntegerField()
    country = models.CharField(max_length=70)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

# Create your models here.
class Comments(models.Model):
    text = models.TextField()
    film = models.ForeignKey(Movies,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Rate(models.Model):
    film = models.ForeignKey(Movies,on_delete=models.CASCADE)
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)




