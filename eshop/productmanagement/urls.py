from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('addProductForm/',view_product_form),
    # path('addProductForm/save',save_product_database),
    path('manageProduct/',view_manage_page,name='product'),
    path('manageProduct/addPhoneForm',view_phone_form, name='phone'),
    path('manageProduct/addPhoneForm/save',save_phone_database),
    path('manageProduct/accessoriesForm',view_accessories_form, name='accessories'),
    path('manageProduct/accessoriesForm/save',save_accessories),
    # path('manageProduct/phoneUpdate/edit/')
    # path('manageProduct/phoneUpdate/edit/update/<int:id>',view_phone_update, name='phoneUpdate'),
    path('manageProduct/accessoriesUpdate/edit/',get_acc_id),
    path('manageProduct/accessoriesUpdate/edit/update/<int:id>',update_accessories),

    path('manageProduct/delete',deleteProducts,name='deleteProducts'),
    path('manageProduct/confirmdelete/<int:ID>',confirmDeleteProducts),
]
