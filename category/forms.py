from django import forms
from category.models import Category

class CategoryForm(forms.ModelForm):
    # ask jango to create a category based on the database model
    class Meta:
        #define form architecture
        model=Category
        fields='__all__'
        

