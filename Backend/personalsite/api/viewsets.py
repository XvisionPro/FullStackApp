from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveUpdateAPIView

from .utils import PostAPIPagination
from .models import Post
from .serializer import PostDetailSerializer, PostSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, UserPermission
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    pagination_class = PostAPIPagination
    queryset = Post.objects.all()
    # serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.GET.get('user','')
        if user:
            return Post.objects.filter(user_id=user)
        else:
            return Post.objects.all()
        
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
    

class PostAPIView(ListCreateAPIView):
    permission_classes = (UserPermission, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostAPIDetailView(RetrieveUpdateAPIView):
    permission_classes = (UserPermission, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer