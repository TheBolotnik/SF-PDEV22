from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

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
    paginate_by = 10
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


class NewsCategory(ListView, DataMixin):
    model = News
    template_name = 'news/category_list2.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(cat__id=self.kwargs['cat_id']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscribers'] = self.request.user not in self.categories.all()



        c = Category.objects.get(id=self.kwargs['cat_id'])
        c_def = self.get_user_context(
            title='Категория - ' + str(c.name),
            cat_selected=c.pk
        )
        return dict(list(context.items()) + list(c_def.items()))


    #def get_queryset(self):
        # self.category = get_object_or_404(Category, id=self.kwargs['cat_id'])
        # queryset = News.objects.filter(category=self.category)
        # return queryset



@login_required
def subscribe(requests, cat_id):
    user = requests.user
    category = Category.objects.get(id=cat_id)
    category.subscriber.add(user)

    message = 'Вы подписаны на рассылку'
    return render(requests, 'news/subscribe.html', {'category': category, 'message': message})


class AddNews(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, CreateView):
    permission_required = ('news.add_news')
    form_class = AddNewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        c_def = self.get_user_context(title='Добавить новость')
        return dict(list(context.items()) + list(c_def.items()))


@login_required
def upgrade_authors(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

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


class Login(DataMixin, LoginView):
    form_class = LogInForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(requests):
    logout(requests)
    return redirect('login')


class SignIn(DataMixin, CreateView):
    form_class = SignInForm
    template_name = 'news/signin.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def PageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



