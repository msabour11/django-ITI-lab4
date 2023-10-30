from django.shortcuts import render,redirect
from category.forms import CategoryForm
from category.models import Category
from django.views import View
from store.models import Product
from django.contrib.auth.decorators import  login_required


# Create your views here.
def home(request):

    # category=Category.objects.all()
    categories=Category.get_all_category()


    return render(request, 'category/home.html', {'categories': categories})



@login_required()
def create(request):
    form=CategoryForm()
    if request.method == 'POST':
        form=CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('home')  # redirect to home page with using the name of url
            return redirect(Category.get_home_url()) # redirect to home page using method name in model
        
        



    return render(request, 'category/create.html', {'form': form})



def edit(request,id):
    category=Category.get_specific_category(id)


    form=CategoryForm(instance=category)
    if request.method == 'POST':
        form=CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            category.save()
            # return redirect(Category.get_home_url())
            return redirect('home')
    

    return render(request, 'category/edit.html', {'form':form})




# create view for category using class 

class ShowDetail(View):
    def get(self, request, id):
        category=Category.get_specific_category(id)

        return render(request, 'category/show.html', {'category':category})


# class AllProductsCategory(View): 
#     def get(self, request, category_id):
#         category = Category.objects.get(pk=category_id)
#         products = category.product_set.all() 

#         return render(request, 'category/all_products.html', {'products': products, 'category': category})

