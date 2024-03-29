from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    location = forms.CharField(max_length=100)
    address = forms.TextInput()

    class Meta:
        model = Profile
        fields = ['location', 'address', 'image']


class sell_check_form(forms.Form):
    email = forms.EmailField()
