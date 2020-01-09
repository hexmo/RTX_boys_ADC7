from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    stockNo = models.IntegerField()
    releaseDate = models.DateField(auto_now=False)
    specs = models.FileField()
    # image = models.ImageField()
    brand = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)


class Phones(models.Model):
    screenSize = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    RAM = models.CharField(max_length=255)
    ROM = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)
    description = models.CharField(max_length=255) 

    def __str__(self):
        return str(self.id)