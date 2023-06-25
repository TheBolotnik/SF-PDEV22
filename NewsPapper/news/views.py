from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [
    {'title': 'Главная страница', 'url_name': 'home' },
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Добавить новость', 'url_name': 'add_news'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    return render(request, 'news/index.html', {'menu': menu, 'title': 'Главная страница'})

def newslist(requests):
    posts = News.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Список новостей',

    }

    return render(requests, 'news/NewsList.html', context=context)

def add_news(requests):
    return HttpResponse('Добавить новость')

def login(requests):
    return HttpResponse('Войти')

def post(requests, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def PageNotFound(requests, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


'''class NewsList(ListView):
    model = News
    template_name = 'NewsList.html'
    extra_context = {'title' : 'Новости'}'''
