from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, User
from .models import *


class User_Sing_Up_Form(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=20, label='Username')
    password1 = forms.CharField(min_length=8, max_length=20, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, max_length=20, label='Password confirm', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class User_Sing_In_Form(AuthenticationForm):
    username = forms.CharField(min_length=5, max_length=20, label='Username')
    password = forms.CharField(min_length=8, max_length=20, label='Password', widget=forms.PasswordInput())


class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['parent_id', 'title']


class Article_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'category_id']
