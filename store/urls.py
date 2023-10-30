
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import home,product_detail,index_db,detail,delete,search,create,create_form,edit_product

urlpatterns = [
    
    path('home/',home, name='home'),
    path('products/<int:id>/',product_detail , name='product_detail'),
    path('',index_db, name='index_db'),
    # path('db/<int:id>', detail, name='detail'),
    path('show/<int:id>', detail, name='product.detail'),

    path('db/<int:id>/delete',delete, name='delete'),
    path('search/', search, name='search'),
    path('create/',create, name='create'),
    path('createform/',create_form, name='create_form'),
    path('edit/<int:id>',edit_product, name='edit_product'),
   
]



