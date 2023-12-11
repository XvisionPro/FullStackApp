
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio/<slug:post_slug>/', post, name="post"),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('addpost/', addpost, name="addpost"),
]