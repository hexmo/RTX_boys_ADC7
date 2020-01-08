from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('addPhoneForm/',view_phone_form),
    path('addPhoneForm/save',save_in_database),
]
