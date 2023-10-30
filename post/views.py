from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from post.forms import PostForm
from post.models import Post


# Create your views here.

class CreatePostView(CreateView):
    template_name='post/create.html'
    form_class = PostForm
    # success_url='/post/list' 
    success_url= reverse_lazy('list') 


    def form_validate(self,form):
        request = self.request
        user=request.user
        form.instance.author=request.user
        return sum().form_validate(form)


   



# list posts

class ListPostView(ListView):
    model = Post
    template_name='post/list.html'
    context_object_name='posts'


# edit posts

class EditPostView(UpdateView):

    template_name='post/edit.html'
    form_class = PostForm
    success_url='/post/list'
    # queryset=Post.objects.all()
    queryset=Post.get_all_objects()


class DetailPostView(DetailView):
    model=Post
    template_name='post/detail.html'
    context_object_name='post'


class DeletePostView(DeleteView):
    template_name='post/delete.html'
    success_url='/post/list'
    queryset=Post.get_all_objects()

