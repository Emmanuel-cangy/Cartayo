from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.ImageField(default='item2.png')


    def __str__(self):
        return self.name
