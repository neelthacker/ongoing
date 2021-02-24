from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from datetime import datetime

class CreatePost(forms.ModelForm):
    def __init__(self, data=None,  *args, **kwargs):
            super(CreatePost, self).__init__(data, *args, **kwargs)
            
            self.fields['slug']=forms.CharField(
                widget=forms.TextInput(
                attrs={
                    'placeholder': "slug",
                    'class': 'form-control ',
                    'value':datetime.now().strftime("%S%f"),
                    }
                ),
            )

    class Meta:
        model = Post
        fields = ['title','author','content','slug']

        
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email'}

