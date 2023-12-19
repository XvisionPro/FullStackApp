
from django.urls import path
from .views import main
from .viewsets import PostAPIView

urlpatterns = [
    path('', main),
    path('v1/posts/', PostAPIView.as_view()),
]