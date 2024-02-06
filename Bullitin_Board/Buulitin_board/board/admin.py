from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'post_img', 'post_img', 'date', 'cat')
    fields = ['title', 'content', 'images', 'cat']
    readonly_fields = ['post_img']

    @admin.display(description='Медиафайлы', ordering='content')
    def post_img(self, post:Post):
        if post.images:
            return mark_safe(f"<img src='{post.images.url}' width=50>")
        return 'Без фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)