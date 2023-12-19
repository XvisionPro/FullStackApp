from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    add_fieldsets= (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'welcomeCode',
                )
            }
        )
    )
    
    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'welcomeCode',
                )
            }
        )
    )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostFile)
admin.site.register(CustomUser, CustomUserAdmin)


# Classes
