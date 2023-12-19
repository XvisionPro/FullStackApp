from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.models import Group 

from .utils import nav_list, DataMixin
from .forms import AddPostForm, CustomUserCreationForm, RegisterUserForm, LoginUserForm, FilterPostsForm, AddPostFileForm
from .filters import PostFilter

from .models import *

# nav_list =[{'title': "Главная", 'url_name': 'main'},
#             {'title': "Обо мне", 'url_name': 'about'},
#             {'title': 'Портфолио', 'url_name': 'portfolio'},
#             {'title': 'Войти', 'url_name': 'login'},]


class Portfolio(DataMixin, ListView):
    model = Post
    template_name = 'blog/portfolio.html'
    context_object_name = 'posts'
    paginate_by = 4
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        st_filter = PostFilter(self.request.GET, queryset)
        c_def = self.get_user_context(title='Портфолио', auth=auth, st_filter=st_filter)
        posts = Post.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Портфолио'
        context['nav_list'] = nav_list
        context['posts'] = posts
        return {**context, **c_def}
    
    def get_queryset(self):
        queryset = super().get_queryset()
        st_filter = PostFilter(self.request.GET, queryset)
        return st_filter.qs



# def portfolio(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts,4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         'title': "Портфолио", 
#         'nav_list': nav_list,
#         'posts': posts
#     }
#     return render(request, 'blog/portfolio.html', context=context)

class ShowPost(DataMixin,DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list=None, **kwargs): 
        context = super().get_context_data(**kwargs)
        images = PostFile.objects.filter(post=context['post'].id)
        c_def=self.get_user_context(title=context['post'].title)
        context['nav_list'] = nav_list
        context['images'] = images
        return dict(list(context.items())+list(c_def.items()))


# Create your views here.
def main(request):
    
    context = {
        'title': "Главная страница", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/index.html', context=context)

def about(request):
    context = {
        'title': "Обо мне", 
        'nav_list': nav_list,
    }
    return render(request, 'blog/about.html', context=context)



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
        formfile = AddPostFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid() and formfile.is_valid():
            #print(form.cleaned_data)
            try:
                form.instance.user = request.user
                post_instance = form.save(commit=False)
                post_instance.save()
                for f in files:
                    file_instance = PostFile(file=f, post=post_instance)
                    file_instance.save()
                return redirect('main')
            except:
                form.add_error(None, "Лох!")
                formfile.add_error(None, "Лох2!")
    else:
        form = AddPostForm()
        formfile = AddPostFileForm()
    context = {
        'title': "Добавить пост", 
        'nav_list': nav_list,
        'form': form,
        'formfile': formfile,
    }
    return render(request, 'blog/addpost.html', context=context)

class RegisterUser(DataMixin, CreateView):
    # form_class = RegisterUserForm
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        
        user_group = Group.objects.get(name=form.cleaned_data['groups'])
        user.groups.add(user_group)
        # for form_ug in form.cleaned_data['groups']:
        #     user_group = Group.objects.get(name=form_ug.name)
        #     user.groups.add(user_group)
        login(self.request, user)
        return redirect('main')

    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('login')
