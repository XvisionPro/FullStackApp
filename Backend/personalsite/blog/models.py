from django.db import models
from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse 
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True,verbose_name='Имя пользователя')
    welcomeCode = models.CharField(verbose_name='Код приглашения',unique=True, max_length=50, null=True)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})
    
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField(verbose_name='Содержание', null=True, max_length=1000)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering= ['title']
    
    
    
