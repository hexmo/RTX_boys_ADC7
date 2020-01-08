from django.db import models

# Create your models here.
class Phones(models.Model):
    brand = models.CharField(max_length=255)
    phoneModel = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    price = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id)