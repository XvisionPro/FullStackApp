from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name='Имя пользователя',max_length=50)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    password = models.CharField(verbose_name='Пароль', max_length=50)
    isAdmin = models.BooleanField(verbose_name='Администратор', default=False)
    welcomeCode = models.CharField(verbose_name='Код приглашения',max_length=50, null=True)
    
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField(verbose_name='Содержание', null=True, max_length=1000)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True, db_index=True)
    user = models.ForeignKey(User, verbose_name=("ID пользователя"), on_delete=models.CASCADE)
    
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
    user = models.ForeignKey(User, verbose_name=("ID пользователя"), on_delete=models.CASCADE)
    

# Тест Gallery_file (не мигрирован)

class GalleryFile(models.Model):
    gallery = models.ForeignKey(Gallery, verbose_name=("ID галереи"), on_delete=models.CASCADE)
    file = models.FileField(verbose_name=("Файл"), upload_to=None, max_length=100)
    favorite = models.BooleanField(verbose_name="Избранное?", default=False)


