from django import forms
from django.forms import Textarea

from .models import *


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label='Название')
    # content = forms.CharField(widget=forms.Textarea, label='Описание')
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор')

    class Meta:
        model = Post
        fields = ['title', 'content', 'images', 'cat', 'author']


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Изображение')


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'row': 3})




