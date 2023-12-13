
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('portfolio/', Portfolio.as_view(), name="portfolio"),
    path('portfolio/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('about/', about, name="about"),
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('addpost/', addpost, name="addpost"),
    path('logout/', logout_user, name="logout"),
]