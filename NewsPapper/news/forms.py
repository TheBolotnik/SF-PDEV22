from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from allauth.account.forms import SignupForm

from .models import *

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'date', 'description', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Длина превышает 255 символов')
        else:
            return title

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and len(description) < 20:
            raise ValidationError({'description': 'Описание не может быть менее 20 символов'})
        return cleaned_data


class SignInForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')
    #     widgets = {
    #             'username': forms.TextInput(attrs={'class': 'form-input'}),
    #             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
    #             'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
    #     }


''' Если нужно, чтобы заработал класс Мета нужно заменить модель User из .models на django.contrib.auth.models,
раскомментировать класс'''


class UserSignUpForm(SignupForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)

    def save(self, request):
        user = super(UserSignUpForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))