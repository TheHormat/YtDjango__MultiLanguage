from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    author = models.CharField(verbose_name="Author", max_length=30)
    description = models.TextField(verbose_name="Description", max_length=500)
    price = models.PositiveIntegerField()