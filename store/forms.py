

from django import forms
from store.models import Product
from category.models import Category

class ProductForm(forms.Form):
    title = forms.CharField(required=True, label='Product Name')
    description = forms.CharField(required=True, label='Description Name')
    price = forms.IntegerField(required=True)
    image = forms.ImageField(required=True)
    in_stock = forms.ChoiceField(
        choices=[('y', 'Yes'), ('n', 'NO')])
    
    cat  =  forms.ModelChoiceField(
        Category.objects.all(), label='Category'
    )


    # cat = forms.ModelChoiceField(
    # queryset=Category.objects.all(),
    # label='Category',
    # required=False,  # Add this line if you want the field to be optional
    #             )