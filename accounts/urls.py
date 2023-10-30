from django.urls import include,path
from accounts.views import profile,AccountCreateView,profile_delete

urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('profile/',profile,name='profile'),
     path('register', AccountCreateView.as_view(), name='register'),
     path('profile_delete', profile_delete, name='profile_delete')


]