from django_filters import FilterSet, CharFilter
from django.core.exceptions import ValidationError

from .models import News, Category

class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'cat': ['exact'],
            'title': ['icontains'],
            'date': ['gt'],
           # 'auth': ['exact'],
        }
