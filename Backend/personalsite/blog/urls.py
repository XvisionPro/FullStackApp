
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('portfolio/', Portfolio.as_view(), name="portfolio"),
    path('portfolio/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('about/', about, name="about"),
    path('login/', LoginUser.as_view(), name="Applogin"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('addpost/', addpost, name="addpost"),
    path('logout/', logout_user, name="Applogout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)