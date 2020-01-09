from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('addProductForm/',view_product_form),
    path('addProductForm/save',save_product_database),
    path('addPhoneForm/',view_phone_form),
    path('addPhoneForm/save',save_phone_database),
]
