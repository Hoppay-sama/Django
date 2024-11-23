from django.db import models

# Create your models here.
class Album(models.Model):
    image = models.ImageField(default='0.png', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date = models.DateField()