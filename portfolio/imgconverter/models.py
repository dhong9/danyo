from django.db import models

# Create your models here.
class ImgConverter(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()