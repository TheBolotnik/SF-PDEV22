from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import *
from .utils import DataMixin
from .forms import *

#menu = ['Главная страница', 'Категории объявлений', 'Добавить объявление', 'Войти', 'Регистрация', 'Профиль']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Категории объявлений", 'url_name': 'category'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},

]

profile_menu = [
    # {'title': "Добавить объявление", 'url_name': 'add_post'},
    # {'title': "Войти", 'url_name': 'users:login'},
    # {'title': "Регистрация", 'url_name': 'signin'},
    # {'title': "Профиль", 'url_name': 'profile'},

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


class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'board/home.html'
    context_object_name = 'posts'
    pk_url_kwargs = 'cat_id'

    def get_queryset(self):
        post_category = get_object_or_404(Category, id=self.kwargs['cat_id'])
        queryset = Post.objects.filter(cat=post_category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['profile_menu'] = profile_menu
        return context


class ShowPost(FormMixin, DetailView):
    model = Post
    template_name = 'board/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    form_class = ReplyForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('post/', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'post'
        context['profile_menu'] = profile_menu
        return context


class Add_Post(LoginRequiredMixin, CreateView):

    '''Вариант №1'''

    #form_class = AddPostForm
    # success_url = reverse_lazy('home')
    # login_url = reverse_lazy('home')

    '''Варинт №2'''
    model = Post
    fields = ['title', 'content', 'images', 'cat']   # или '__all__' и любые другие поля модели
    template_name = 'board/add_post.html'
    raise_exception = True
    login_url = 'users:login'

    extra_context = {
        'title': 'Добавить объявление',
        'menu': menu,
        'profile_menu': profile_menu
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

class EditPost(UpdateView):
    model = Post
    fields = ['title', 'content', 'images', 'cat']
    template_name = 'board/add_post.html'
    raise_exception = True
    extra_context = {
        'title': 'Добавить объявление',
        'menu': menu,
        'profile_menu': profile_menu
    }



def profile(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadFileForm()

    data = {
        'title': 'Ваш профиль',
        'menu': menu,
        'profile_menu': profile_menu,
        'form': form
    }
    return render(request=request, template_name='board/profile.html', context=data)
