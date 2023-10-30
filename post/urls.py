
from django.contrib import admin
from django.urls import path,include
from post.views import CreatePostView,ListPostView,EditPostView,DetailPostView,DeletePostView
from django.contrib.auth.decorators import login_required



urlpatterns = [
   
    path('create/',login_required(CreatePostView.as_view()), name='create'),
    path('list/',ListPostView.as_view(), name='list'),
    path('edit/<int:pk>',EditPostView.as_view(), name='edit'),
    path('detail/<int:pk>',DetailPostView.as_view(), name='detail'),
    path('delete/<int:pk>',DeletePostView.as_view(), name='delete'),


    
]
