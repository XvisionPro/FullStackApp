from typing import Any
from django import forms
from blog.models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# class AddPostForm2(forms.Form):
#     title = forms.CharField(label='Название поста', max_length=100)
#     thubnail = forms.ImageField(label='Обложка',initial=None)
#     text = forms.CharField(label='Текст поста', max_length=1000)
    
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'text', 'user','slug')
        
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', 
    widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', 
    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', 
    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
class FilterPostsForm(forms.Form):
    title = forms.CharField(label='Название поста', max_length=50, required=False)

