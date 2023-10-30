

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


# form for registering anew a user
class AccountForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


# form for updating profile use name fieldand first_name field and last_name field and email field
# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = User  # we are you're using the default User model
#         fields = ('username', 'first_name', 'last_name', 'email')


# form for editing all profile information
class EditProfileForm(UserChangeForm):
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return password
