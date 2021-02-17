from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    genre = models.CharField(max_length=90)
    video = models.FileField()
    poster = models.ImageField()

