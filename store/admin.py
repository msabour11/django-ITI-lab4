from django.contrib import admin

# Register your models here to dispaly in panel admin 
from store.models import Product
admin.site.register(Product)