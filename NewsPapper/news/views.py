from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import *

menu = ['Главная страница', 'Новости', 'Добавить новость', 'Войти']

def index(request):
    return render(request, 'news/index.html', {'menu': menu, 'title': 'Главная страница'})

def newslist(requests):
    posts = News.objects.all()
    return render(requests, 'news/NewsList.html', {'posts': posts, 'menu': menu, 'title': 'Список новостей'})


'''class NewsList(ListView):
    model = News
    template_name = 'NewsList.html'
    extra_context = {'title' : 'Новости'}'''
