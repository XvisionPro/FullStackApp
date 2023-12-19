from rest_framework.generics import ListAPIView
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response

class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer