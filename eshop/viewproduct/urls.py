from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('viewPhones/', seePhones),
    path('viewLaptops/', seeLaptops),
    path('viewAccessories/',seeAccessories),
]
