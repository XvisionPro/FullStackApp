from typing import Any
from django import forms
from blog.models import Post, PostFile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UserCreationForm
from .models import CustomUser
from django.template.defaultfilters import slugify
from django.forms import ClearableFileInput
from django.contrib.auth.models import User, Group

# class AddPostForm2(forms.Form):
#     title = forms.CharField(label='Название поста', max_length=100)
#     thubnail = forms.ImageField(label='Обложка',initial=None)
#     text = forms.CharField(label='Текст поста', max_length=1000)
    
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'text','slug',)
        
class AddPostFileForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ('file',)
        widgets= {
            'file': forms.FileInput(attrs={'multiple': True, 'type': 'file'})
        }

                
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


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())
    
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['username','first_name','last_name', 'email', 'welcomeCode', 'groups']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['username','first_name','last_name', 'email', 'welcomeCode', 'groups']
