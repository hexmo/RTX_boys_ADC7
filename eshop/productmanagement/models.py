from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    stockNo = models.IntegerField()
    releaseDate = models.DateField(auto_now=False)
    specs = models.FileField(upload_to='media/documents/')
    image = models.ImageField(upload_to='media/images/')
    brand = models.CharField(max_length=255)
    
    def __str__(self):
        return (self.name)

    class Meta:
        abstract = True
        # ordering = ["name","price","stockNo","releaseDate","specs","brand","image"]


class Phones(Product):
    screenSize = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    RAM = models.CharField(max_length=255)
    ROM = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)
    description = models.TextField() 

    def __str__(self):
        return str(self.id)+' '+self.name

class Accessories(Product):
    category = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return str(self.id)+' '+self.name
