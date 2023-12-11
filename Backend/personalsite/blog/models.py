from django.db import models
from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse 
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)
    welcomeCode = models.CharField(verbose_name='Код приглашения',unique=True, max_length=50, null=True)
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})
    
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField(verbose_name='Содержание', null=True, max_length=1000)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
    
    
    
