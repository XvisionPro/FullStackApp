from django.http import HttpResponse
from django.shortcuts import render

from .models import *

nav_list =[{'title': "Главная", 'url_name': 'main'},
            {'title': "Обо мне", 'url_name': 'about'},
            {'title': 'Портфолио', 'url_name': 'portfolio'},
            {'title': 'Войти', 'url_name': 'login'},]

posts = Post.objects.all()
# Create your views here.
def main(request):
    
    context = {
        'title': "Главная старница", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/index.html', context=context)

def portfolio(request):
    context = {
        'title': "Портфолио", 
        'nav_list': nav_list,
        'posts': posts,
    }
    return render(request, 'blog/portfolio.html', context=context)

def about(request):
    context = {
        'title': "Обо мне", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/about.html', context=context)

def login(request):
    context = {
        'title': "Авторизация", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/login.html', context=context)

def post(request, post_id):
    context = {
        'title': "Пост", 
        'nav_list': nav_list,
        'post_id': post_id
    }
    return render(request,'blog/post.html', context=context)