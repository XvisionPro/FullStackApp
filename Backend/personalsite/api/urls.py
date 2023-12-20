
from django.urls import include, path, re_path
from .views import UserView
from .viewsets import PostAPIView, PostAPIDetailView, PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', UserView.as_view()),
    # path('v1/posts/', PostViewSet.as_view({'get': 'list'})),
    # path('v1/posts/<int:pk>', PostAPIDetailView.as_view()),
    path('v1/',include(router.urls)),
    path('v1/auth-session/', include('rest_framework.urls')),
]