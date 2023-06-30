from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category
from .forms import *
from .utils import *
from .filters import NewsFilter




class NewsHome(DataMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class NewsList(DataMixin, ListView):
    paginate_by = 3
    model = News
    template_name = 'news/NewsList.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Список новостей')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'news/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class NewsCategory(DataMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        pass


class AddNews(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy ('home')
    login_url = reverse_lazy ('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить новость')
        return dict(list(context.items()) + list(c_def.items()))

class Search(DataMixin, ListView):
    model = News
    template_name = 'news/search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())


    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter()
        }
        c_def = self.get_user_context(title='Поиск новостей')
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('Войти')


def PageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




'''class NewsList(ListView):
    model = News
    template_name = 'NewsList.html'
    extra_context = {'title' : 'Новости'}'''
