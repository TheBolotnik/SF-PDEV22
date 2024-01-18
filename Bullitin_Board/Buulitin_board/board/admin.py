from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)