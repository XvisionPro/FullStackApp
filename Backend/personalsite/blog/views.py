from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView

from .utils import nav_list, DataMixin
from .forms import AddPostForm

from .models import *

# nav_list =[{'title': "Главная", 'url_name': 'main'},
#             {'title': "Обо мне", 'url_name': 'about'},
#             {'title': 'Портфолио', 'url_name': 'portfolio'},
#             {'title': 'Войти', 'url_name': 'login'},]


class Portfolio(DataMixin, ListView):
    model = Post
    template_name = 'blog/portfolio.html'
    context_object_name = 'students'
    def get_context_data(self, *, object_list=None, **kwargs):
        posts = Post.objects.all() 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Портфолио'
        context['nav_list'] = nav_list
        context['posts'] = posts
        return context

class ShowPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'st'
    def get_context_data(self, *, object_list=None, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Портфолио'
        context['nav_list'] = nav_list
        return context


# Create your views here.
def main(request):
    
    context = {
        'title': "Главная старница", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/index.html', context=context)

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

# def post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     context = {
#         'title': "Пост", 
#         'nav_list': nav_list,
#         'slug_id': post_slug,
#         'text': post.text,
#     }
#     return render(request,'blog/post.html', context=context)

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST,  request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                form.save()
                return redirect('main')
            except:
                form.add_error(None, "Лох!")
    else:
        form = AddPostForm()
    context = {
        'title': "Добавить пост", 
        'nav_list': nav_list,
        'form': form,
    }
    return render(request, 'blog/addpost.html', context=context)