from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django_filters import FilterSet

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .forms import *
from board.models import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class SigninUser(CreateView):
    form_class = SigninUserForm
    template_name = 'users/signin.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = Post.objects.filter(author=self.request.user)
        context['user_posts'] = user_posts

    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)


class PostFilter(FilterSet):

    class Meta:
        model = Reply
        fields = ['post']

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author_id=kwargs['request'])


class ProfileUserView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'users/profile2.html'
    context_object_name = 'replies'

    def get_queryset(self):
        queryset = Reply.objects.filter(post__author_id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Reply.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# def reply_status(request, pk, type):
#         return HttpResponse('Тест')


    # def user_replies(self, request):
    #     user = request.user
    #     replies = Reply.objects.id(pk=user.id)
    #     return replies