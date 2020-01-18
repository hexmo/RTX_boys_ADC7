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
    #abstract model which allows inheritance and the table is not created
    class Meta:
        abstract = True
        # ordering = ["name","price","stockNo","releaseDate","specs","brand","image"]

# phone class model that inherits Product model
class Phones(Product):
    screenSize = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    RAM = models.CharField(max_length=255)
    ROM = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)
    description = models.CharField(max_length=255) 

    def __str__(self):
        return str(self.id)

# accessories model that inherits Product model
class Accessories(Product):
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)
