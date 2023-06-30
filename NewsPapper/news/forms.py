from django import forms
from django.core.exceptions import ValidationError

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
