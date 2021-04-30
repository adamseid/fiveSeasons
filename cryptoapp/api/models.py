from django.db import models

# Create your models here.

class Data(models.Model):
    bitcoin = models.CharField(max_length=10, default='', unique=True)

 