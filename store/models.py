from django.db import models
from django.shortcuts import reverse,redirect
from category.models import Category

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField(default=123, null=True)
    # image=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='store/images',max_length=200,null=True)

    in_stock=models.CharField(
        choices=[('y','Yes'), ('n','No')]
    )

    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='products')

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self) : 
        return f'{self.title}'
    
    def get_image(self):
        return f'/static/store/images/{self.image}'
    

    #upload image to server
    def get_image(self):
        return f'/media/{self.image}'
    

    # def more_details(self):
    #     url=reverse('detail', args=(self.id,))
    #     return url
    
    def get_show_url(self):
        url = reverse('product.detail', args=[self.id])
        return url


    def go_back(self):
         url = 'index_db'
         return redirect(url)
    


    def delete_product(self):
        url=reverse('delete', args=[self.id])
        return url
    

    def get_edit_url(self):
        return reverse('edit_product', args=[self.id])
    

    @classmethod
    # get all products in category

    def get_specific_product(cls,id):
        return cls.objects.get(id=id)
          
     

