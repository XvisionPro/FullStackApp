from django import forms
from blog.models import Post

# class AddPostForm2(forms.Form):
#     title = forms.CharField(label='Название поста', max_length=100)
#     thubnail = forms.ImageField(label='Обложка',initial=None)
#     text = forms.CharField(label='Текст поста', max_length=1000)
    
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

