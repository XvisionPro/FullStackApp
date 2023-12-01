from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name='Имя пользователя',max_length=50)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    password = models.CharField(verbose_name='Пароль', max_length=50)
    isAdmin = models.BooleanField(verbose_name='Администратор', default=False)
    welcomeCode = models.CharField(verbose_name='Код приглашения',max_length=50, null=True)

