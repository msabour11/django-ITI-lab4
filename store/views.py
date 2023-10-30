from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from store.models import  Product
# from django import forms
from store.forms import ProductForm
from category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.
products=[
    {'id': 1, 'title': 'Mobile', 'price':333,'image':'mobile.png','description':'Apple Iphone 5s 32gb Silver With Signs Of Wear - Iphone 5 S White'},
    {'id': 2, 'title': 'labtop', 'price':222,'image':'lab.png','description':'Star Labtop Mk Iii Linux Laptop Computer Open Left - Side Angle Laptop'},
    {'id': 3, 'title': 'watch', 'price':100,'image':'watch.png','description':'Bangalore Watch Company Mens Watches'},
    {'id': 4, 'title': 'Smart TV', 'price':500,'image':'tv2.png','description':'Ks Suhd K Smart - Tv 49 Pollici Samsung'},
     {'id': 5, 'title': 'storage', 'price':20,'image':'storage.png','description':'Alpha 5000 E Mount Camera And 16 50 Mm Zoom Lens With - Micro Sd'},
    {'id': 6, 'title': 'camera', 'price':250,'image':'camera.png','description':'Cameras & Optics,camera Accessory,point And Shoot Camera,camera,digital - Flir T840'},
    {'id': 7, 'title': 'Earphone', 'price':40,'image':'era.png','description':'Original Earphones For Nubia Mobile Phone - Headphones'},
    {'id': 8, 'title': 'Battery', 'price':70,'image':'charge.png','description':'Firefly Replacement Battery - Firefly 2 Battery'},
]

def home(request):
    return render(request, 'store/home.html',context={'products':products})




def product_detail(request, id):
    # retrieve the product details based on the product id
    id = int(id)
    product_detail = None

    for product in products:
        if product['id'] == id:
            product_detail = product
            break

    if product_detail:
        return render(request, 'store/product_details.html',context={'product_detail': product_detail})
    else:
        return HttpResponse('Product not found')
    
    # view to deal with database and model 


def index_db(request):
    products_db=Product.objects.all()


    return render(request, 'store/crud/index.html', context={'products_db': products_db})
    


def detail(request, id):
    # retrieve the product details based on the product id
    # id = int(id)
    # product_detail = None

    # for product in products_db:
    #     if product['id'] == id:
    #         product_detail = product
    #         break

    # if product_detail:
    #     return render(request, 'store/crud/details.html',context={'product_detail': product_detail})
    # else:
    #     return HttpResponse('Product not found')
    product_detail = get_object_or_404(Product, id=id)
    return render(request, 'store/crud/details.html',context={'product_detail': product_detail})

def delete( request, id):
    products_db=Product.objects.get(id=id)
    products_db.delete()
    url=reverse('index_db')
    return redirect(url)


from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'store/crud/search_results.html', {'products': products})

  

# create product
@login_required
def create(request):
    if request.method == 'POST':
        print(request.POST)
        title=request.POST['title']
        description=request.POST['description']
        price = request.POST['price']
        image=request.POST['image']
        in_stock=request.POST['in_stock']
        name=request.POST['name']


        product=Product()
        product.title = title
        product.description = description
        product.price = price
        product.image = image
        product.in_stock = in_stock
        product.name = name
        product.save()
        return redirect(product.get_show_url())


      
    return render(request, 'store/crud/create.html')

@login_required
def create_form(request):
    form =ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            price = form.cleaned_data['price']
            image=form.cleaned_data['image']
            in_stock=form.cleaned_data['in_stock']
            cat=form.cleaned_data['cat']

            product=Product()
            product.title = title
            product.description = description
            product.price = price
            product.image = image
            product.in_stock = in_stock
            product.cat = cat
            product.save()
            return redirect(product.get_show_url())
            #  print(request.POST)
        
            # return HttpResponse('success')
    return render(request, 'store/crud/createform.html',context={'form':form})



#edit product

# def edit_product(request, id):
#     form=ProductForm()
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect(product.get_show_url())
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'store/crud/edit.html', {'form': form})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Update the product fields
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            in_stock = form.cleaned_data['in_stock']
            cat=form.cleaned_data['cat']
            # return redirect('index_db')
            
            product.title = title
            product.description = description
            product.price = price
            product.image = image
            product.in_stock = in_stock
            product.cat = cat
            product.save()
            return redirect(product.get_show_url())
        
    else:
        form = ProductForm()
    return render(request, 'store/crud/edit.html', {'form': form, 'product': product})



