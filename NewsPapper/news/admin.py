from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
