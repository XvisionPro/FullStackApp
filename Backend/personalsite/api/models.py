from django.db import models
from django.urls import reverse
from blog.models import CustomUser

# Create your models here.
    
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField(verbose_name='Содержание', null=True, max_length=1000)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True, db_index=True)
    user = models.ForeignKey(CustomUser, verbose_name=("ID пользователя"), on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering= ['title']
        
class Gallery(models.Model):
    name = models.CharField(("Название статьи"), max_length=100)
    theme = models.BooleanField(verbose_name="Тёмная тема", default=False)
    filmed_at = models.DateTimeField(("Дата съёмки"), auto_now=False, auto_now_add=False)
    user = models.ForeignKey(CustomUser, verbose_name=("ID пользователя"), on_delete=models.CASCADE)
    

# Тест Gallery_file

class GalleryFile(models.Model):
    gallery = models.ForeignKey(Gallery, verbose_name=("ID галереи"), on_delete=models.CASCADE)
    file = models.FileField(verbose_name=("Файл"), upload_to=None, max_length=100)
    favorite = models.BooleanField(verbose_name="Избранное?", default=False)

