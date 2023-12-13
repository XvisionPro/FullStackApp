from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post
class PostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='contains', label='Название статьи')
    
    class Meta:
        model = Post
        fields = ['title']
