from django.db import models
from django.shortcuts import  reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    body = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True,upload_to='post/images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'
    

    def get_image_url(self):
        return f'/media/{self.image}'
    

    def get_edit_url(self):
        # get the edit url
        return reverse('edit', args=[self.id])
    
    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()
    

    def get_detail_url(self):
        # get the detail url
        return reverse('detail', args=[self.id])
    
    def get_list_url(self):
        # get the list of all posts url
        return reverse('list')
    

    def get_delete_url(self):
        return reverse('delete', args=[self.id])
    

