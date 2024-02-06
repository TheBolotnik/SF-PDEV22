from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

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


# def reply_status(request, pk, type):
#         return HttpResponse('Тест')


    # def user_replies(self, request):
    #     user = request.user
    #     replies = Reply.objects.id(pk=user.id)
    #     return replies