from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostFile)


# Classes
