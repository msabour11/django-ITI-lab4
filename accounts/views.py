from django.shortcuts import render,redirect,reverse
from django.views.generic import DetailView
from django.views.generic.edit import  CreateView
from django.http import HttpResponse
from accounts.forms import AccountForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.views.generic.edit import DeleteView


def profile (request):

    url=reverse('index_db')
    return HttpResponse('profile')
    return redirect(url)

# @login_required
# def profile(request):
#     user = request.user  # Get the currently logged-in user
#     # You can access user properties like user.username, user.first_name, user.email, etc.
    
#     return render(request, 'accounts/profile.html', {'user': user})

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to the profile page

    else:
        form = EditProfileForm(instance=user)

    return render(request, 'accounts/profile.html', {'form': form})
class AccountCreateView(CreateView):
    form_class = AccountForm
    template_name = 'accounts/create.html'
    success_url = '/accounts/login/'



def profile_delete(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        return redirect('index_db')  # Redirect to your home page or any other appropriate page after deletion

    return render(request, 'accounts/profile_delete.html', {'user': user})