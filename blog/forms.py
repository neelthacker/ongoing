from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Category, Comments
from datetime import datetime


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Username', 'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email'}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
