from django.db import models
from django.shortcuts import reverse, redirect

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='store/images',
                              max_length=200, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_image_url(self):
        return f'/media/{self.image}'

    @classmethod
    # method to get the all categories
    def get_all_category(cls):
        return cls.objects.all()

    @classmethod
    # method to get url for category homepage
    def get_home_url(cls):
        return reverse('home')

    @classmethod
    def get_specific_category(cls, id):
        return cls.objects.get(id=id)

    def get_edit_urls(self):
        return reverse('edit_category', args=[self.id])

    def get_detail_url(self):
        return reverse('ShowDetail', args=[self.id])
