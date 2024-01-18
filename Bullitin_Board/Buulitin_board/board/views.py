from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, DetailView, FormView

from .models import *
from .utils import DataMixin

#menu = ['Главная страница', 'Категории объявлений', 'Добавить объявление', 'Войти', 'Регистрация', 'Профиль']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Категории объявлений", 'url_name': 'category'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},

]

profile_menu = [
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Регистрация", 'url_name': 'signin'},
    {'title': "Профиль", 'url_name': 'profile'},
]

list_categories = [
    {'id': 1, 'name': 'Танки'},
    {'id': 2, 'name': 'Хилеры'},
    {'id': 3, 'name': 'Гилдмастеры'},
    {'id': 4, 'name': 'Квестгиверы'},
    {'id': 5, 'name': 'Кузнецы'},

]


class HomeView(ListView):
    template_name = 'board/home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['profile_menu'] = profile_menu
        return context

# def home(request):
#
#     posts = Post.objects.all()
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'profile_menu': profile_menu,
#         'posts': posts
#     }
#     return render(request=request, template_name='board/home.html', context=data)


# def show_category(request, cat_id):
#     category = get_object_or_404(Category, id=cat_id)
#     posts = Post.objects.filter(cat_id=category.pk)
#
#     data = {
#         'title': f'Категория - {category.name}',
#         'menu': menu,
#         'profile_menu': profile_menu,
#         'posts': posts,
#     }
#     return render(request, template_name='board/home.html', context=data)


class PostCategory(ListView, DataMixin):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context


def show_post(request, post_id):
    return HttpResponse(f'<H1>Показать пост с id {post_id}</H1>')


def add_post(request):
    data = {
        'title': 'Добавить объявление',
        'menu': menu,
        'profile_menu': profile_menu
    }
    return render(request=request, template_name='board/add_post.html', context=data)


def login(request):
    data = {
        'title': 'Вход',
        'menu': menu,
        'profile_menu': profile_menu
    }
    return render(request=request, template_name='board/login.html', context=data)


def logout(request):
    pass


def signin(request):
    data = {
        'title': 'Регистрация',
        'menu': menu,
        'profile_menu': profile_menu
    }
    return render(request=request, template_name='board/signin.html', context=data)

def profile(request):
    data = {
        'title': 'Ваш профиль',
        'menu': menu,
        'profile_menu': profile_menu
    }
    return render(request=request, template_name='board/profile.html', context=data)