from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post, PostFile

class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='contains', label='Название статьи')
    
    class Meta:
        model = Post
        fields = ['title']
        
class PostFileFilter(FilterSet):
    
    class Meta:
        model: PostFile
        fields = ['file']
        
        
